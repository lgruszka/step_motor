#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import os

import config
from w_load_program import Ui_LoadProgramWindow 

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s


class CLoadProgramWindow(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_LoadProgramWindow()
        self.ui.setupUi(self)
        # self.ui.programCmbBox.activated[str].connect(self.refresh_params)
        self.ui.pushButton_confirm.clicked.connect(self.pushButton_confirm_Clicked)
        self.ui.pushButton_return.clicked.connect(self.pushButton_return_Clicked)
        

    def refreshProgramCmbBox(self):
            self.ui.programCmbBox.clear()
            prg_list = [prg.split('.txt')[0] for prg in os.listdir(config.pathname+"/programy") if '.txt' in prg]
            prg_list.sort()
            for i in prg_list:
                self.ui.programCmbBox.addItem(_fromUtf8(i))
            self.ui.programCmbBox.setCurrentIndex(-1)
            
    def getName(self):
        return self.ui.programCmbBox.currentText()
    
    def refresh_params(self, source_path):
        #ustawianie wczytanych wartosci parametrow
        print source_path
        self.plik = open(source_path).readlines()
        config.current_program_name = self.plik[0][:-1]
        config.rotates_per_cycle = float(self.plik[2])
        config.velocity = float(self.plik[4])
        config.cycles_to_reset = float(self.plik[6])
        config.param_window.ui.lcdSteps.display(config.rotates_per_cycle)
        config.param_window.ui.lcdVel.display(config.velocity)
        config.param_window.ui.lcdCycles.display(config.cycles_to_reset)
        
    def pushButton_confirm_Clicked(self):
        if len(self.getName()) is 0:
            QtGui.QMessageBox.information(self,'Info',"wybierz program",QtGui.QMessageBox.Ok)
        else:
            try:
                source_path_ = config.pathname +"/programy/" + self.ui.programCmbBox.currentText()+'.txt'
                self.refresh_params(source_path_)
                self.hide()
            except:
                QtGui.QMessageBox.information(self,'Info',"wczytanie programu niemozliwe",QtGui.QMessageBox.Ok)
                source_path_ = config.pathname+"/parametry.txt"
                self.refresh_params(source_path_)
                
    def pushButton_return_Clicked(self):
        self.hide()

