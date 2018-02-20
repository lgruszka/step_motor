# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'w_parameters.ui'
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

class Ui_ParamWindow(object):
    def setupUi(self, ParamWindow):
        ParamWindow.setObjectName(_fromUtf8("ParamWindow"))
        ParamWindow.resize(480, 320)
        self.lcdSteps = QtGui.QLCDNumber(ParamWindow)
        self.lcdSteps.setGeometry(QtCore.QRect(190, 20, 161, 71))
        self.lcdSteps.setSmallDecimalPoint(False)
        self.lcdSteps.setProperty("value", 2.0)
        self.lcdSteps.setProperty("intValue", 2)
        self.lcdSteps.setObjectName(_fromUtf8("lcdSteps"))
        self.downBtn = QtGui.QPushButton(ParamWindow)
        self.downBtn.setGeometry(QtCore.QRect(380, 130, 81, 101))
        self.downBtn.setText(_fromUtf8(""))
        self.downBtn.setIconSize(QtCore.QSize(81, 81))
        self.downBtn.setObjectName(_fromUtf8("downBtn"))
        self.upBtn = QtGui.QPushButton(ParamWindow)
        self.upBtn.setGeometry(QtCore.QRect(380, 20, 81, 101))
        self.upBtn.setText(_fromUtf8(""))
        self.upBtn.setIconSize(QtCore.QSize(81, 81))
        self.upBtn.setObjectName(_fromUtf8("upBtn"))
        self.lcdVel = QtGui.QLCDNumber(ParamWindow)
        self.lcdVel.setGeometry(QtCore.QRect(190, 93, 161, 71))
        self.lcdVel.setProperty("value", 2.0)
        self.lcdVel.setObjectName(_fromUtf8("lcdVel"))
        self.velBtn = QtGui.QPushButton(ParamWindow)
        self.velBtn.setGeometry(QtCore.QRect(25, 98, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.velBtn.setFont(font)
        self.velBtn.setCheckable(True)
        self.velBtn.setObjectName(_fromUtf8("velBtn"))
        self.rotateNrBtn = QtGui.QPushButton(ParamWindow)
        self.rotateNrBtn.setGeometry(QtCore.QRect(25, 25, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.rotateNrBtn.setFont(font)
        self.rotateNrBtn.setCheckable(True)
        self.rotateNrBtn.setChecked(True)
        self.rotateNrBtn.setObjectName(_fromUtf8("rotateNrBtn"))
        self.cycleNrBtn = QtGui.QPushButton(ParamWindow)
        self.cycleNrBtn.setGeometry(QtCore.QRect(25, 170, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cycleNrBtn.setFont(font)
        self.cycleNrBtn.setCheckable(True)
        self.cycleNrBtn.setObjectName(_fromUtf8("cycleNrBtn"))
        self.lcdCycles = QtGui.QLCDNumber(ParamWindow)
        self.lcdCycles.setGeometry(QtCore.QRect(190, 166, 161, 71))
        self.lcdCycles.setSmallDecimalPoint(False)
        self.lcdCycles.setProperty("value", 1000.0)
        self.lcdCycles.setProperty("intValue", 1000)
        self.lcdCycles.setObjectName(_fromUtf8("lcdCycles"))
        self.returnBtn = QtGui.QPushButton(ParamWindow)
        self.returnBtn.setGeometry(QtCore.QRect(380, 250, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.returnBtn.setFont(font)
        self.returnBtn.setIconSize(QtCore.QSize(81, 81))
        self.returnBtn.setObjectName(_fromUtf8("returnBtn"))
        self.savePrgBtn = QtGui.QPushButton(ParamWindow)
        self.savePrgBtn.setGeometry(QtCore.QRect(190, 250, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.savePrgBtn.setFont(font)
        self.savePrgBtn.setObjectName(_fromUtf8("savePrgBtn"))
        self.frame = QtGui.QFrame(ParamWindow)
        self.frame.setGeometry(QtCore.QRect(20, 240, 341, 5))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.loadPrgBtn = QtGui.QPushButton(ParamWindow)
        self.loadPrgBtn.setGeometry(QtCore.QRect(30, 250, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.loadPrgBtn.setFont(font)
        self.loadPrgBtn.setObjectName(_fromUtf8("loadPrgBtn"))

        self.retranslateUi(ParamWindow)
        QtCore.QMetaObject.connectSlotsByName(ParamWindow)

    def retranslateUi(self, ParamWindow):
        ParamWindow.setWindowTitle(_translate("ParamWindow", "Dialog", None))
        self.velBtn.setText(_translate("ParamWindow", "prędkość\n"
" [obr/s]", None))
        self.rotateNrBtn.setText(_translate("ParamWindow", "ilość obrotów\n"
" [obr/cykl]", None))
        self.cycleNrBtn.setText(_translate("ParamWindow", "ilość cykli \n"
"do resetu", None))
        self.returnBtn.setText(_translate("ParamWindow", "Powrót", None))
        self.savePrgBtn.setText(_translate("ParamWindow", "zapisz program", None))
        self.loadPrgBtn.setText(_translate("ParamWindow", "wczytaj program", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ParamWindow = QtGui.QDialog()
    ui = Ui_ParamWindow()
    ui.setupUi(ParamWindow)
    ParamWindow.show()
    sys.exit(app.exec_())

