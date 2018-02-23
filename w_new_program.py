# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'w_new_program.ui'
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

class Ui_NewProgramWindow(object):
    def setupUi(self, NewProgramWindow):
        NewProgramWindow.setObjectName(_fromUtf8("NewProgramWindow"))
        NewProgramWindow.resize(480, 320)
        self.lineEdit_prgName = QtGui.QLineEdit(NewProgramWindow)
        self.lineEdit_prgName.setGeometry(QtCore.QRect(140, 30, 201, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_prgName.setFont(font)
        self.lineEdit_prgName.setObjectName(_fromUtf8("lineEdit_prgName"))
        self.pushButton_confirm = QtGui.QPushButton(NewProgramWindow)
        self.pushButton_confirm.setGeometry(QtCore.QRect(20, 20, 111, 91))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_confirm.setFont(font)
        self.pushButton_confirm.setStyleSheet(_fromUtf8("background: green;\n"
"color: white"))
        self.pushButton_confirm.setObjectName(_fromUtf8("pushButton_confirm"))
        self.pushButton_return = QtGui.QPushButton(NewProgramWindow)
        self.pushButton_return.setGeometry(QtCore.QRect(350, 20, 111, 91))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_return.setFont(font)
        self.pushButton_return.setStyleSheet(_fromUtf8("background: red;\n"
"color: white"))
        self.pushButton_return.setObjectName(_fromUtf8("pushButton_return"))

        self.retranslateUi(NewProgramWindow)
        QtCore.QMetaObject.connectSlotsByName(NewProgramWindow)

    def retranslateUi(self, NewProgramWindow):
        NewProgramWindow.setWindowTitle(_translate("NewProgramWindow", "Dialog", None))
        self.pushButton_confirm.setText(_translate("NewProgramWindow", "Potwierdź", None))
        self.pushButton_return.setText(_translate("NewProgramWindow", "Powrót", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    NewProgramWindow = QtGui.QDialog()
    ui = Ui_NewProgramWindow()
    ui.setupUi(NewProgramWindow)
    NewProgramWindow.show()
    sys.exit(app.exec_())

