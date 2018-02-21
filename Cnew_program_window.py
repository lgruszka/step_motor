#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import os

import config
from w_new_program import Ui_NewProgramWindow 

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s


class CNewProgramWindow(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_NewProgramWindow()
        self.ui.setupUi(self)
        
        self.ui.pushButton_confirm.clicked.connect(self.pushButton_confirm_Clicked)
        self.ui.pushButton_return.clicked.connect(self.pushButton_return_Clicked)
        
        
    def getName(self):
        return self.ui.lineEdit_prgName.text()
        
    def saveParam(self, dest_path):
        config.rotates_per_cycle = config.param_window.ui.lcdSteps.value()
        config.velocity = config.param_window.ui.lcdVel.value()
        config.cycles_to_reset = config.param_window.ui.lcdCycles.value()
        self.plik = [str(config.current_program_name),'rotates_per_cycle\n', str(config.rotates_per_cycle)+'\n', 'velocity\n', str(config.velocity)+'\n', 'cycles_to_reset\n', str(config.cycles_to_reset)+'\n']
        open(dest_path, 'w').writelines((self.plik))
        
    def saveDefaults(self):
        pass    # TODO
        
    def pushButton_confirm_Clicked(self):
        if len(self.getName()) is 0:
            QtGui.QMessageBox.information(self,'Info',"podaj nazwę programu",QtGui.QMessageBox.Ok)
        else:
            try:
                dest_path_ = config.pathname +"/programy/" + self.ui.lineEdit_prgName.text()+'.txt'
                self.saveParam(dest_path_)
                self.hide()
            except:
                QtGui.QMessageBox.information(self,'Info',"zapisanie programu niemozliwe",QtGui.QMessageBox.Ok)
                
    def pushButton_return_Clicked(self):
        self.hide()
