from PyQt4.QtGui import QDialog
import Dialog_Informacion


class ClassInformacion(QDialog, Dialog_Informacion.Ui_Dialog):
    def __init__(self, parent=None):
        super(ClassInformacion, self).__init__(parent)
        self.setupUi(self)
