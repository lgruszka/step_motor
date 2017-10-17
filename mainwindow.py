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
        self.resetCounterBtn = QtGui.QPushButton(self.centralwidget)
        self.resetCounterBtn.setGeometry(QtCore.QRect(240, 10, 221, 131))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.resetCounterBtn.setFont(font)
        self.resetCounterBtn.setStyleSheet(_fromUtf8("background: orange"))
        self.resetCounterBtn.setObjectName(_fromUtf8("resetCounterBtn"))
        self.lcdCounter = QtGui.QLCDNumber(self.centralwidget)
        self.lcdCounter.setGeometry(QtCore.QRect(20, 40, 161, 81))
        self.lcdCounter.setObjectName(_fromUtf8("lcdCounter"))
        self.startBtn = QtGui.QPushButton(self.centralwidget)
        self.startBtn.setGeometry(QtCore.QRect(20, 130, 161, 121))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.startBtn.setFont(font)
        self.startBtn.setStyleSheet(_fromUtf8("background: green;\n"
"color: white"))
        self.startBtn.setCheckable(True)
        self.startBtn.setObjectName(_fromUtf8("startBtn"))
        self.exitBtn = QtGui.QPushButton(self.centralwidget)
        self.exitBtn.setGeometry(QtCore.QRect(380, 180, 81, 71))
        self.exitBtn.setStyleSheet(_fromUtf8("background: red;\n"
"color: white;\n"
""))
        self.exitBtn.setObjectName(_fromUtf8("exitBtn"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 280, 161, 91))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.paramBtn = QtGui.QPushButton(self.centralwidget)
        self.paramBtn.setGeometry(QtCore.QRect(200, 180, 161, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.paramBtn.setFont(font)
        self.paramBtn.setStyleSheet(_fromUtf8(""))
        self.paramBtn.setCheckable(True)
        self.paramBtn.setObjectName(_fromUtf8("paramBtn"))
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
        self.label_2.setText(_translate("MainWindow", "ilość cykli", None))
        self.paramBtn.setText(_translate("MainWindow", "parametry", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

