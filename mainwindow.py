# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './mainwindow.ui'
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
        MainWindow.resize(480, 320)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.upBtn = QtGui.QPushButton(self.centralwidget)
        self.upBtn.setGeometry(QtCore.QRect(200, 10, 81, 81))
        self.upBtn.setText(_fromUtf8(""))
        self.upBtn.setIconSize(QtCore.QSize(81, 81))
        self.upBtn.setObjectName(_fromUtf8("upBtn"))
        self.downBtn = QtGui.QPushButton(self.centralwidget)
        self.downBtn.setGeometry(QtCore.QRect(200, 100, 81, 81))
        self.downBtn.setText(_fromUtf8(""))
        self.downBtn.setIconSize(QtCore.QSize(81, 81))
        self.downBtn.setObjectName(_fromUtf8("downBtn"))
        self.resetCounterBtn = QtGui.QPushButton(self.centralwidget)
        self.resetCounterBtn.setGeometry(QtCore.QRect(300, 130, 161, 111))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.resetCounterBtn.setFont(font)
        self.resetCounterBtn.setStyleSheet(_fromUtf8("background: orange"))
        self.resetCounterBtn.setObjectName(_fromUtf8("resetCounterBtn"))
        self.lcdSteps = QtGui.QLCDNumber(self.centralwidget)
        self.lcdSteps.setGeometry(QtCore.QRect(20, 30, 161, 81))
        self.lcdSteps.setSmallDecimalPoint(False)
        self.lcdSteps.setProperty("value", 6.0)
        self.lcdSteps.setProperty("intValue", 6)
        self.lcdSteps.setObjectName(_fromUtf8("lcdSteps"))
        self.lcdCounter = QtGui.QLCDNumber(self.centralwidget)
        self.lcdCounter.setGeometry(QtCore.QRect(300, 30, 161, 81))
        self.lcdCounter.setObjectName(_fromUtf8("lcdCounter"))
        self.startBtn = QtGui.QPushButton(self.centralwidget)
        self.startBtn.setGeometry(QtCore.QRect(20, 130, 161, 111))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.startBtn.setFont(font)
        self.startBtn.setStyleSheet(_fromUtf8("background: green;\n"
"color: white"))
        self.startBtn.setCheckable(True)
        self.startBtn.setObjectName(_fromUtf8("startBtn"))
        self.exitBtn = QtGui.QPushButton(self.centralwidget)
        self.exitBtn.setGeometry(QtCore.QRect(380, 250, 81, 41))
        self.exitBtn.setStyleSheet(_fromUtf8("background: red;\n"
"color: white;\n"
""))
        self.exitBtn.setObjectName(_fromUtf8("exitBtn"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 250, 241, 31))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 19))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.resetCounterBtn.setText(_translate("MainWindow", "reset", None))
        self.startBtn.setText(_translate("MainWindow", "start", None))
        self.exitBtn.setText(_translate("MainWindow", "Zamknij", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

