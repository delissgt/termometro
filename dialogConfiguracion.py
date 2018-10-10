from PyQt4.QtGui import (QDialog, QDialogButtonBox)
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
        self.checkBox_X.clicked.connect(self.funcionAplicarCambios)#senial que se activan usuaario solamente
        self.checkBox_Y.clicked.connect(self.funcionAplicarCambios)

        # conexiones de botones restore y cancel
        self.dialogButtonBox.button(QDialogButtonBox.RestoreDefaults).clicked.connect(self.funcionParametros)
        self.dialogButtonBox.button(QDialogButtonBox.Cancel).clicked.connect(self.reject)



    def funcionAplicarCambios(self):
        #grosor = self.doubleSpinBox.value()
        #opacidad = self.doubleSpinBox_2.value()

        self.configuraciones["color"] = unicode(self.comboBox.currentText())
        self.configuraciones["grosor"] = self.doubleSpinBox.value() #grosor
        self.configuraciones["opacidad"] = self.doubleSpinBox_2.value() #opacidad
        self.configuraciones["ejeX"] = self.checkBox_X.isChecked()
        self.configuraciones["ejeY"] = self.checkBox_Y.isChecked()
        #Manda a ejecutar la funcion en el MainWindow
        self.callback() # = self.refrescar    del app.py


    def funcionParametros(self):
        self.comboBox.setCurrentIndex(self.comboBox.findText("black"))
        self.doubleSpinBox.setValue(2)
        self.doubleSpinBox_2.setValue(0.5)
        self.checkBox_X.setChecked(True)
        self.checkBox_Y.setChecked(True)
        self.funcionAplicarCambios()

