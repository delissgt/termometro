# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui-termometro.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(545, 452)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/recursos/thermometer.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.graphicsView = PlotWidget(self.centralwidget)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.verticalLayout_2.addWidget(self.graphicsView)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(15)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_temperatura = QtGui.QLabel(self.centralwidget)
        self.label_temperatura.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_temperatura.setAutoFillBackground(False)
        self.label_temperatura.setAlignment(QtCore.Qt.AlignCenter)
        self.label_temperatura.setObjectName(_fromUtf8("label_temperatura"))
        self.horizontalLayout_3.addWidget(self.label_temperatura)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_tempe_max = QtGui.QLabel(self.centralwidget)
        self.label_tempe_max.setObjectName(_fromUtf8("label_tempe_max"))
        self.horizontalLayout.addWidget(self.label_tempe_max)
        self.spinBox_tempe_max = QtGui.QSpinBox(self.centralwidget)
        self.spinBox_tempe_max.setObjectName(_fromUtf8("spinBox_tempe_max"))
        self.horizontalLayout.addWidget(self.spinBox_tempe_max)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.checkBox_alarma = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_alarma.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox_alarma.setObjectName(_fromUtf8("checkBox_alarma"))
        self.horizontalLayout_2.addWidget(self.checkBox_alarma)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.pushButton_Iniciar = QtGui.QPushButton(self.centralwidget)
        self.pushButton_Iniciar.setObjectName(_fromUtf8("pushButton_Iniciar"))
        self.horizontalLayout_3.addWidget(self.pushButton_Iniciar)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 545, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionAjustes = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/recursos/ajustes.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAjustes.setIcon(icon1)
        self.actionAjustes.setObjectName(_fromUtf8("actionAjustes"))
        self.actionInformacion = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/recursos/icons8-acerca-de-100.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionInformacion.setIcon(icon2)
        self.actionInformacion.setObjectName(_fromUtf8("actionInformacion"))
        self.actionRefresh = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/recursos/refrescar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRefresh.setIcon(icon3)
        self.actionRefresh.setObjectName(_fromUtf8("actionRefresh"))
        self.toolBar.addAction(self.actionAjustes)
        self.toolBar.addAction(self.actionInformacion)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionRefresh)
        self.label_tempe_max.setBuddy(self.spinBox_tempe_max)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_temperatura.setText(_translate("MainWindow", "0", None))
        self.label_tempe_max.setText(_translate("MainWindow", "&Temperatura: ", None))
        self.checkBox_alarma.setText(_translate("MainWindow", "&Alarma ", None))
        self.pushButton_Iniciar.setText(_translate("MainWindow", "&Start", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.actionAjustes.setText(_translate("MainWindow", "Ajustes", None))
        self.actionAjustes.setToolTip(_translate("MainWindow", "cambios de interfaz ", None))
        self.actionInformacion.setText(_translate("MainWindow", "Informacion", None))
        self.actionInformacion.setToolTip(_translate("MainWindow", "informacion acerca del programa", None))
        self.actionRefresh.setText(_translate("MainWindow", "Refresh", None))
        self.actionRefresh.setToolTip(_translate("MainWindow", "refrescar", None))

from pyqtgraph import PlotWidget
import recursosExternos_rc
