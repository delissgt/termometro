from PyQt4.QtGui import QDialog
import Dialog_Informacion
import sys
from PyQt4.Qt import PYQT_VERSION_STR

class ClassInformacion(QDialog, Dialog_Informacion.Ui_Dialog):
                #(instancia= yo mismo ,  variable, padre)
    def __init__(self, versionPrograma, parent=None):
        super(ClassInformacion, self).__init__(parent)
        self.setupUi(self)
        versionPython = " Python " + sys.version.split()[0]
        versionPyQt = ",  PyQt " + PYQT_VERSION_STR
        self.label_tecnologia.setText(self.label_tecnologia.text() + versionPython
                                      + versionPyQt)

        self.label_version.setText(self.label_version.text() +" "+ versionPrograma)






