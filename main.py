#!/usr/bin/env python
# -*- coding: utf-8 -*-
# simple.py
from __builtin__ import True

import sys
import os
import RPi.GPIO as GPIO
import time
import datetime
#import threading

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#21 to wyjscie do sterownika silnika
#26 wystawiam na zawsze wysoki jako symulator sygnalu z maszyny
#20 ustawiam jako wejscie do odczytu sygnalu z maszyny


#   ] [
#   ] [
#  26 20
#  G  21

#set 21 as output
GPIO.setup(21,GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(26,GPIO.OUT, initial=GPIO.HIGH)
#set 20 as input and pull voltage down
GPIO.setup(20,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

from mainwindow import Ui_MainWindow

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

pathname = os.path.dirname(sys.argv[0])
#run_motor_thread_lock = threading.Lock()

class CMain(QtGui.QMainWindow):
        def __init__(self):
                QtGui.QMainWindow.__init__(self)
                self.ui = Ui_MainWindow()
                self.ui.setupUi(self)
                
                self.ui.startBtn.clicked.connect(self.startBtn_Clicked)
                self.ui.resetCounterBtn.clicked.connect(self.resetCounterBtn_Clicked)
                self.ui.exitBtn.clicked.connect(self.exitBtn_Clicked)
                
                self.ui.upBtn.clicked.connect(self.upBtn_Clicked)
                self.ui.downBtn.clicked.connect(self.downBtn_Clicked)
                
                #timer input czy jest rozkaz od maszyny
                self.check_input = QtCore.QTimer()
                self.check_input.timeout.connect(self.checkInput)
                
                #timer input czy doliczyc cykl maszyny
                self.check_cycle = QtCore.QTimer()
                self.check_cycle.timeout.connect(self.checkCycle)
                self.enable = False
                
                self.counter = 0
                self.counter2 = 0
                self.cycles = 0
                self.steps_one_cycle = 1.5
                self.microstep = 4
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
                steps = 200.*self.microstep*turns
                return steps
                
        #zakrec silnik
        def move_motor(self, steps):
                print "obracam motor o {}".format(steps)
                print datetime.datetime.now()
                for i in range(int(steps)):
                    GPIO.output(21,GPIO.HIGH)
                    time.sleep(0.001)
                    GPIO.output(21,GPIO.LOW)
                    time.sleep(0.001)
                print "koniec obrotu"
                #do usuniecia - zastapic przez sygnal maszyny
                self.cycles = self.cycles + 1
        
        def checkInput(self):
                if GPIO.input(20):
                        if self.enable is True:
                                #self.enable = False
                                #run_motor_thread_lock.acquire()
                                self.move_motor(self.rot_to_steps(float(self.ui.lcdSteps.value()))) 
                                time.sleep(0.2)
                                #self.enable = True
                                #run_motor_thread_lock.release()
                        else:
                                print "probowalem w trybie zabronionym"
                        
        def checkCycle(self):
                        self.ui.lcdCounter.display(self.cycles)
                
        def resetCounterBtn_Clicked(self):
                self.cycles = 0
                self.ui.lcdCounter.display(self.cycles)
                
        def startBtn_Clicked(self):
                if self.ui.startBtn.isChecked() == True:
                        print "wcisnalem"
                        self.enable = True
                        self.check_cycle.start(10)
                        self.check_input.start(1)
                        self.ui.startBtn.setStyleSheet(_fromUtf8("background: red; color: white"))
                        self.ui.startBtn.setText("stop")
                        self.ui.upBtn.setEnabled(False)
                        self.ui.downBtn.setEnabled(False)
                else:
                        print "odcisnalem"
                        self.enable = False
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
        
        def exitBtn_Clicked(self):
                self.close()
                #os.system("shutdown now -h")                       
                
                
                
if __name__=='__main__':

        app = QtGui.QApplication(sys.argv)
        window = CMain()

        window.ui.lineEdit.setVisible(False)
        window.show()
        print "1"
        sys.exit(app.exec_())
        GPIO.cleanup()
        print "2"
