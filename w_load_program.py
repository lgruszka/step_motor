# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'w_load_program.ui'
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

class Ui_LoadProgramWindow(object):
    def setupUi(self, LoadProgramWindow):
        LoadProgramWindow.setObjectName(_fromUtf8("LoadProgramWindow"))
        LoadProgramWindow.resize(480, 320)
        self.pushButton_confirm = QtGui.QPushButton(LoadProgramWindow)
        self.pushButton_confirm.setGeometry(QtCore.QRect(110, 90, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_confirm.setFont(font)
        self.pushButton_confirm.setObjectName(_fromUtf8("pushButton_confirm"))
        self.pushButton_reject = QtGui.QPushButton(LoadProgramWindow)
        self.pushButton_reject.setGeometry(QtCore.QRect(230, 90, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_reject.setFont(font)
        self.pushButton_reject.setObjectName(_fromUtf8("pushButton_reject"))
        self.programCmbBox = QtGui.QComboBox(LoadProgramWindow)
        self.programCmbBox.setGeometry(QtCore.QRect(110, 30, 241, 51))
        self.programCmbBox.setObjectName(_fromUtf8("programCmbBox"))

        self.retranslateUi(LoadProgramWindow)
        QtCore.QMetaObject.connectSlotsByName(LoadProgramWindow)

    def retranslateUi(self, LoadProgramWindow):
        LoadProgramWindow.setWindowTitle(_translate("LoadProgramWindow", "Dialog", None))
        self.pushButton_confirm.setText(_translate("LoadProgramWindow", "potwierdz", None))
        self.pushButton_reject.setText(_translate("LoadProgramWindow", "odrzuc", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    LoadProgramWindow = QtGui.QDialog()
    ui = Ui_LoadProgramWindow()
    ui.setupUi(LoadProgramWindow)
    LoadProgramWindow.show()
    sys.exit(app.exec_())

