# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Datasoft\Desktop\Escritorio Edgardo\Programas\Python Dev\qtTestFormPy-master\MainWindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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
        MainWindow.resize(718, 439)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(350, 90, 16, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 90, 16, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.btn_CtoF = QtGui.QPushButton(self.centralwidget)
        self.btn_CtoF.setGeometry(QtCore.QRect(250, 120, 75, 23))
        self.btn_CtoF.setObjectName(_fromUtf8("btn_CtoF"))
        self.btn_FtoC = QtGui.QPushButton(self.centralwidget)
        self.btn_FtoC.setGeometry(QtCore.QRect(250, 60, 75, 23))
        self.btn_FtoC.setObjectName(_fromUtf8("btn_FtoC"))
        self.editCel = QtGui.QLineEdit(self.centralwidget)
        self.editCel.setGeometry(QtCore.QRect(119, 88, 133, 20))
        self.editCel.setObjectName(_fromUtf8("editCel"))
        self.spinFahr = QtGui.QSpinBox(self.centralwidget)
        self.spinFahr.setGeometry(QtCore.QRect(360, 90, 33, 20))
        self.spinFahr.setObjectName(_fromUtf8("spinFahr"))
        self.verticalSlider = QtGui.QSlider(self.centralwidget)
        self.verticalSlider.setGeometry(QtCore.QRect(170, 210, 22, 160))
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName(_fromUtf8("verticalSlider"))
        self.dial = QtGui.QDial(self.centralwidget)
        self.dial.setGeometry(QtCore.QRect(280, 260, 50, 64))
        self.dial.setObjectName(_fromUtf8("dial"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(392, 60, 41, 291))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(10, 10, 118, 23))
        self.progressBar.setProperty("value", 99)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.checkBox = QtGui.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(290, 220, 70, 17))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.calendarWidget = QtGui.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(430, 10, 264, 155))
        self.calendarWidget.setObjectName(_fromUtf8("calendarWidget"))
        self.timeEdit = QtGui.QTimeEdit(self.centralwidget)
        self.timeEdit.setGeometry(QtCore.QRect(430, 170, 118, 22))
        self.timeEdit.setObjectName(_fromUtf8("timeEdit"))
        self.lcdNumber = QtGui.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(440, 260, 201, 71))
        self.lcdNumber.setProperty("value", 1234.0)
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.fontComboBox = QtGui.QFontComboBox(self.centralwidget)
        self.fontComboBox.setGeometry(QtCore.QRect(70, 150, 112, 20))
        self.fontComboBox.setObjectName(_fromUtf8("fontComboBox"))
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(70, 180, 69, 20))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 718, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_2.setText(_translate("MainWindow", "F", None))
        self.label.setText(_translate("MainWindow", "C", None))
        self.btn_CtoF.setText(_translate("MainWindow", "De C a F >>", None))
        self.btn_FtoC.setText(_translate("MainWindow", "<< De F a C", None))
        self.checkBox.setText(_translate("MainWindow", "CheckBox", None))

