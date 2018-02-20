#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import os

import config
from w_parameters import Ui_ParamWindow

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class CParamWindow(QtGui.QDialog): 
        def __init__(self):
                QtGui.QDialog.__init__(self)
                self.ui = Ui_ParamWindow()
                self.ui.setupUi(self)
                self.ui.upBtn.clicked.connect(self.upBtn_Clicked)
                self.ui.downBtn.clicked.connect(self.downBtn_Clicked)
                self.ui.upBtn.setAutoRepeat(True)
                self.ui.downBtn.setAutoRepeat(True)
                self.ui.upBtn.setAutoRepeatInterval(200)
                self.ui.downBtn.setAutoRepeatInterval(200)
                self.ui.returnBtn.clicked.connect(self.returnBtn_Clicked)
                self.ui.rotateNrBtn.clicked.connect(self.rotateNrBtn_Clicked)
                self.ui.velBtn.clicked.connect(self.velBtn_Clicked)
                self.ui.cycleNrBtn.clicked.connect(self.cycleNrBtn_Clicked)
                
                self.ui.loadPrgBtn.clicked.connect(self.loadPrgBtn_Clicked)
                self.ui.savePrgBtn.clicked.connect(self.savePrgBtn_Clicked)
                
                #ustawianie poczatkowych wartosci parametrow
                self.plik = open(config.pathname+"/parametry.txt").readlines()
                print self.plik
                config.rotates_per_cycle = float(self.plik[1])
                config.velocity = float(self.plik[3])
                config.cycles_to_reset = float(self.plik[5])
                self.ui.lcdSteps.display(config.rotates_per_cycle)
                self.ui.lcdVel.display(config.velocity)
                self.ui.lcdCycles.display(config.cycles_to_reset)
                
                self.pixmapUp = QtGui.QPixmap(_fromUtf8(config.pathname+"/images/up.png"))
                self.mapaUp = self.pixmapUp.createMaskFromColor(QtGui.QColor(255,255,255),0)
                self.pixmapUp.setMask(self.mapaUp)
                self.ui.upBtn.setIcon(QtGui.QIcon(self.pixmapUp))
                
                self.pixmapDown = QtGui.QPixmap(_fromUtf8(config.pathname+"/images/down.png"))
                self.mapaDown = self.pixmapDown.createMaskFromColor(QtGui.QColor(255,255,255),0)
                self.pixmapDown.setMask(self.mapaDown)
                self.ui.downBtn.setIcon(QtGui.QIcon(self.pixmapDown))
                
        def upBtn_Clicked(self):
                if self.ui.rotateNrBtn.isChecked() is True:
                        config.rotates_per_cycle = config.rotates_per_cycle + config.przyrost_rotates_per_cycle
                elif self.ui.velBtn.isChecked() is True:
                        config.velocity = config.velocity + config.przyrost_velocity
                elif self.ui.cycleNrBtn.isChecked() is True:
                        config.cycles_to_reset = config.cycles_to_reset + config.przyrost_cycles_to_reset
                self.ui.lcdSteps.display(config.rotates_per_cycle)
                self.ui.lcdVel.display(config.velocity)
                self.ui.lcdCycles.display(config.cycles_to_reset)
                
        def downBtn_Clicked(self):
                if self.ui.rotateNrBtn.isChecked() is True:
                        config.rotates_per_cycle = config.rotates_per_cycle - config.przyrost_rotates_per_cycle
                elif self.ui.velBtn.isChecked() is True:
                        config.velocity = config.velocity - config.przyrost_velocity
                elif self.ui.cycleNrBtn.isChecked() is True:
                        config.cycles_to_reset = config.cycles_to_reset - config.przyrost_cycles_to_reset
                self.ui.lcdSteps.display(config.rotates_per_cycle)
                self.ui.lcdVel.display(config.velocity)
                self.ui.lcdCycles.display(config.cycles_to_reset)
                
        def rotateNrBtn_Clicked(self):
                self.ui.upBtn.setAutoRepeatInterval(200)
                self.ui.downBtn.setAutoRepeatInterval(200)
                if self.ui.rotateNrBtn.isChecked == False:
                        self.ui.rotateNrBtn.setChecked(True)
                else:
                        self.ui.velBtn.setChecked(False)
                        self.ui.cycleNrBtn.setChecked(False)
                
        def velBtn_Clicked(self):
                self.ui.upBtn.setAutoRepeatInterval(200)
                self.ui.downBtn.setAutoRepeatInterval(200)
                if self.ui.velBtn.isChecked == False:
                        self.ui.velBtn.setChecked(True)
                else:
                        self.ui.rotateNrBtn.setChecked(False)
                        self.ui.cycleNrBtn.setChecked(False)
                
        def cycleNrBtn_Clicked(self):
                self.ui.upBtn.setAutoRepeatInterval(20)
                self.ui.downBtn.setAutoRepeatInterval(20)
                if self.ui.cycleNrBtn.isChecked == False:
                        self.ui.cycleNrBtn.setChecked(True)
                else:
                        self.ui.rotateNrBtn.setChecked(False)
                        self.ui.velBtn.setChecked(False)

        def loadPrgBtn_Clicked(self):
            config.load_program_window.showFullScreen()
            config.load_program_window.programCmbBox_Clicked()
            
        def savePrgBtn_Clicked(self):
            config.new_program_window.showFullScreen()

        def returnBtn_Clicked(self):
                config.rotates_per_cycle = self.ui.lcdSteps.value()
                config.velocity = self.ui.lcdVel.value()
                config.cycles_to_reset = self.ui.lcdCycles.value()
                self.plik = ['rotates_per_cycle\n', str(config.rotates_per_cycle)+'\n', 'velocity\n', str(config.velocity)+'\n', 'cycles_to_reset\n', str(config.cycles_to_reset)+'\n']
                open(config.pathname+"/parametry.txt", 'w').writelines((self.plik))
                self.setVisible(False)
                
