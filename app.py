#CREACION DE UN TERMOMETRO QUE SUENA CUANDO LLEGA A CIERTA TEMPERATURA QUE INDICA EL USUARIO

from PyQt4.QtGui import (QFileDialog, QMainWindow, QApplication, QComboBox, QLabel, QMessageBox)
from PyQt4.QtCore import QThread, QTimer, QProcess, pyqtSignal as Signal
import serial.tools.list_ports
import sys
import uitermometro #arch interface creado con QTDesigner
import serial, time #se necesita para usar arduino
import re #expresion regular
import pyqtgraph as pg #para la grafica pintar
#from PyQt4.QtMultimedia import (QAudioDeviceInfo, QAudioOutput) para que hicera pip sonido ...
import dialogInformacion

class MainWindow(QMainWindow, uitermometro.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        #para jalar todos los componentes de la interfaz
        #con la linea de arriba se puede ver que jala los componentes, y que to-do salio bien

        miLabel = QLabel("Dispositivos: ")
        self.miComboBox = QComboBox(self)
        self.toolBar.addWidget(miLabel)
        self.toolBar.addWidget(self.miComboBox)

        #TODO botonces up
        self.actionInformacion.triggered.connect(self.funcionInformacion)

        self.actionRefresh.triggered.connect(self.funcionRefrescar)

        self.pushButton_Iniciar.clicked.connect(self.funcionStart)

        #linea para poder mostrar que dispositivos estan conectados
        dispositivos = serial.tools.list_ports.comports()

        #crear grafica y sus propiedades
        self.crear_grafica()  # funcion
        self.grafica_datos_x = []
        self.grafica_datos_y = []
        self.contador_x = 0

        for usb in dispositivos:
            print (usb.device)
            self.miComboBox.addItem(usb.device) #agrega un elemento al ComboBox

        #llamar
        self.funcionCurrentUsb()

        #senial para detectar el dispositivo deleccionado
        self.miComboBox.currentIndexChanged.connect(self.funcionCurrentUsb)



    def crear_grafica(self):
        self.pluma = pg.mkPen(width=2, color='y')
        self.graphicsView.plotItem.showGrid(True, True, 0.5)
        self.graphicsView.setXRange(0, 59)
        self.graphicsView.setYRange(0, 100)


    def actualizar_grafica(self, temperatura):
        if len(self.grafica_datos_y) == 60:
            self.grafica_datos_y.pop(0)

            #extend agrega dato a la lista, mas rapido que apend
        #self.grafica_datos_y.extend([psutil.virtual_memory().percent])
        self.grafica_datos_y.extend([temperatura])

        if len(self.grafica_datos_x) == 60:
            pass
        else:
            self.grafica_datos_x.extend([self.contador_x])
            self.contador_x += 1

        self.graphicsView.plot(self.grafica_datos_x, self.grafica_datos_y[::-1], pen=self.pluma, clear=True)


        self.label_temperatura.setText(str(temperatura))
        if temperatura >= self.spinBox_tempe_max.value():
            print("comparacion datos")

            if self.checkBox_alarma.isChecked():
                print("alarma!!!")
                #sonido = QAudioDeviceInfo.defaultOutputDevice()
                #alarma = QAudioOutput(sonido)
                #alarma.start()
                print('\a')


         #QAudioDeviceInfo info(QAudioDeviceInfo.defaultOutputDevice());


    def funcionCurrentUsb(self):
        self.currentusb = self.miComboBox.currentText()
        print("usb actual: ", self.currentusb)
        #print(type(self.currentusb))


    def funcionStart(self):
        #Boton funcionando
        self.contador_x = 0
        self.grafica_datos_x=[]
        self.grafica_datos_y =[]

        if self.pushButton_Iniciar.text() == "&Start":
            print("boton funcionando")
            self.pushButton_Iniciar.setText("Stop")
            #limpiar texto de temperatura
            self.label_temperatura.setText("")
            #limpiar grafica
            self.graphicsView.plot(self.grafica_datos_x, self.grafica_datos_y[::-1], pen=self.pluma, clear=True)
            #obtener texto temperatura maxima
            valorSpinBox = self.spinBox_tempe_max.value()
            self.spinBox_tempe_max.setDisabled(True)
            print("valor spin: ", valorSpinBox)
            #checkBox
            self.checkBox_alarma.setDisabled(True)

            try:
                #Leer arduino
                self.arduino = serial.Serial(str(self.currentusb), 9600)#abre puerto arduino

                #Hilo lee e imprime lo que recive del arduino, necesario para que no interfiera con interfaz
                self.mi_hilo = ClaseHilo(self.arduino, parent=self)

                self.mi_hilo.mi_senial_num.connect(self.actualizar_grafica)

                self.mi_hilo.start()

            except serial.serialutil.SerialException:
                QMessageBox.critical(self, 'Message', 'dispositivo desconectado', QMessageBox.Ok)


        #Boton detenido
        else:
            try:
                self.mi_hilo.terminate()
                self.arduino.close()
            except AttributeError:
                print("no se encuentra dispositivo")
            self.pushButton_Iniciar.setText("&Start")
            print("boton detenido")
            self.spinBox_tempe_max.setDisabled(False)
            self.checkBox_alarma.setDisabled(False)


    def funcionRefrescar(self):
        self.miComboBox.clear()
        dispositivos = serial.tools.list_ports.comports()
        for usb in dispositivos:
            print (usb.device)
            self.miComboBox.addItem(usb.device) #agrega un elemento al ComboBox


    def funcionInformacion(self):
        ventaInfo = dialogInformacion.ClassInformacion(self)
        ventaInfo.show()





class ClaseHilo(QThread):

    mi_senial_num = Signal(float)

    def __init__(self, arduino, parent=None):
        super(ClaseHilo, self).__init__(parent)
        self.arduino = arduino


    def run(self):
        while True:
            time.sleep(2)
            try:
                rawString = self.arduino.readline()
            except serial.serialutil.SerialException:
                print("dispositivo desconectado")
            else:
                #comparacion = re.search('A[0-9].[0-9]+A', rawString).group()
                comparacion = re.search('A[0-9]+\.[0-9]+A', str(rawString))

                if comparacion is not None:
                    #comparacion.group()
                    temperatura = comparacion.group()
                    #print("comparacion:", comparacion.group())

                    #se trata "comparacion" para que solo se mande el numero
                    #numTemperatura = comparacion[1:]
                    numTemperatura = temperatura[1:]
                    #print("numTemperatura: ", numTemperatura)

                    #print("1A", numTemperatura)
                    longitud = len(numTemperatura)
                    numTemperatura = numTemperatura[:longitud-1]
                    print("texto a enviar", numTemperatura)

                    #emito la senial
                    self.mi_senial_num.emit(float(numTemperatura))

            #self.arduino.close() quitar





#cuando comparo con None se utiliza:
# if variable is None
# if varible is not None
# No se utiliza == o !=



if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setOrganizationDomain("www.deliss.me")
    app.setOrganizationName("deliss")
    app.setApplicationVersion("1")
    app.setApplicationName("deliss_me")
    window = MainWindow()
    window.show()
    app.exec_()
