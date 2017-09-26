#!/usr/bin/env python
# -*- coding: utf-8 -*-
# simple.py
from __builtin__ import True

import sys
import os
import time

from mainwindow import Ui_MainWindow

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

pathname = os.path.dirname(sys.argv[0])

class CMain(QtGui.QMainWindow):
        def __init__(self):
                QtGui.QMainWindow.__init__(self)
                self.ui = Ui_MainWindow()
                self.ui.setupUi(self)
                
                self.ui.startBtn.clicked.connect(self.startBtn_Clicked)
                self.ui.resetCounterBtn.clicked.connect(self.resetCounterBtn_Clicked)
                self.ui.upBtn.clicked.connect(self.upBtn_Clicked)
                self.ui.downBtn.clicked.connect(self.downBtn_Clicked)
                
                #timer input czy jest rozkaz od maszyny
                self.check_input = QtCore.QTimer()
                self.check_input.timeout.connect(self.checkInput)
                
                #timer input czy doliczyc cykl maszyny
                self.check_cycle = QtCore.QTimer()
                self.check_cycle.timeout.connect(self.checkCycle)
                
                self.counter = 0
                self.counter2 = 0
                self.cycles = 0
                self.steps_one_cycle = 1.5
                self.przyrost = 0.1
                self.ui.lcdSteps.display(self.steps_one_cycle)
                
                self.pixmapUp = QtGui.QPixmap(_fromUtf8(pathname+"/images/up.png"))
                self.mapaUp = self.pixmapUp.createMaskFromColor(QtGui.QColor(255,255,255),0)
                self.pixmapUp.setMask(self.mapaUp)
                self.ui.upBtn.setIcon(QtGui.QIcon(self.pixmapUp))
                
                self.pixmapDown = QtGui.QPixmap(_fromUtf8(pathname+"/images/down.png"))
                self.mapaDown = self.pixmapDown.createMaskFromColor(QtGui.QColor(255,255,255),0)
                self.pixmapDown.setMask(self.mapaDown)
                self.ui.downBtn.setIcon(QtGui.QIcon(self.pixmapDown))
                
        #przelic obroty silnika na pojedyncze kroki 
        def rot_to_steps(self, turns):
                steps = 200.*turns
                return steps
                
        #zakrec silnik
        def move_motor(self, steps):
                print "obracam motor o {}".format(steps)
                time.sleep(2)
                print "koniec obrotu"
        
        def checkInput(self):
                self.counter = self.counter + 1 
                #if rozkaz_podaj_barwnik == 1:
                if self.counter == 1000:
                        self.move_motor(self.rot_to_steps(float(self.ui.lcdSteps.value()))) 
                        self.counter = 0
                        
        def checkCycle(self):
                self.counter2 = self.counter2 + 1
                if self.counter2 == 1000:
                        print "counter2 {}".format(self.counter2)
                        self.cycles = self.cycles + 1
                        self.ui.lcdCounter.display(self.cycles)
                        self.counter2 = 0
                
        def resetCounterBtn_Clicked(self):
                self.cycles = 0
                self.ui.lcdCounter.display(self.cycles)
                
        def startBtn_Clicked(self):
                if self.ui.startBtn.isChecked() == True:
                        print "wcisnalem"
                        self.check_cycle.start(1)
                        self.check_input.start(1)
                        self.ui.startBtn.setStyleSheet(_fromUtf8("background: red; color: white"))
                        self.ui.startBtn.setText("stop")
                        self.ui.upBtn.setEnabled(False)
                        self.ui.downBtn.setEnabled(False)
                else:
                        print "odcisnalem"
                        self.check_cycle.stop()
                        self.check_input.stop()
                        self.ui.startBtn.setStyleSheet(_fromUtf8("background: green; color: white"))
                        self.ui.startBtn.setText("start")
                        self.ui.upBtn.setEnabled(True)
                        self.ui.downBtn.setEnabled(True)
                        
        def upBtn_Clicked(self):
                self.steps_one_cycle = self.steps_one_cycle + self.przyrost
                self.ui.lcdSteps.display(self.steps_one_cycle)
                
                
        def downBtn_Clicked(self):
                self.steps_one_cycle = self.steps_one_cycle - self.przyrost
                self.ui.lcdSteps.display(self.steps_one_cycle)
        
                        
                
                
                
if __name__=='__main__':

        app = QtGui.QApplication(sys.argv)
        window = CMain()
        
        window.show()
        print "1"
        sys.exit(app.exec_())
        print "2"
