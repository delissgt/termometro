from PyQt4.QtGui import QDialog
import DialogConfiguraciones

class ClassConfiguracion(QDialog, DialogConfiguraciones.Ui_Dialog):
    #recibir diccionario//
    #recibir 4 parametros(self, funcion, padre, DICCIONARIO)
    def __init__(self, callback, configuraciones, parent=None):
        super(ClassConfiguracion, self).__init__(parent)
        self.setupUi(self)

        self.configuraciones = configuraciones
        self.callback = callback

        self.comboBox.currentIndexChanged.connect(self.funcionAplicarCambios)
        self.doubleSpinBox.valueChanged.connect(self.funcionAplicarCambios)
        self.doubleSpinBox_2.valueChanged.connect(self.funcionAplicarCambios)
        self.checkBox_X.clicked.connect(self.funcionAplicarCambios)
        self.checkBox_Y.clicked.connect(self.funcionAplicarCambios)


    def funcionAplicarCambios(self):
        #grosor = self.doubleSpinBox.value()
        #opacidad = self.doubleSpinBox_2.value()

        self.configuraciones["color"] = unicode(self.comboBox.currentText())
        self.configuraciones["grosor"] = self.doubleSpinBox.value() #grosor
        self.configuraciones["opacidad"] = self.doubleSpinBox_2.value() #opacidad
        self.configuraciones["ejeX"] = self.checkBox_X.isChecked()
        self.configuraciones["ejeY"] = self.checkBox_Y.isChecked()
        #Manda a ejecutar la funcion en el MainWindow
        self.callback()
