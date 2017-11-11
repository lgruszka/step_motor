#!/usr/bin/env python
# -*- coding: utf-8 -*-
# simple.py
from __builtin__ import True

import sys
import os
import config
import RPi.GPIO as GPIO
import time
import datetime
#import threading

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#21 to wyjscie do sterownika silnika
#19 wystawiam jako wyjscie na brzeczek
#16 jako wejscie na sygnal z maszyny czy cykl wykonano
#26 wystawiam na zawsze wysoki jako symulator sygnalu z maszyny
#20 ustawiam jako wejscie do odczytu sygnalu z maszyny wywolujacej ruch


#   ] [
#   ] [
#  05 G
#  06 12
#  13 G
#  19 16
#  26 20
#  G  21

#ustaw 21 jako wyjscie na sterownik silnika
GPIO.setup(21,GPIO.OUT, initial=GPIO.LOW)
#ustaw 26 jako wyjscie w stanie zawsze wysokim
GPIO.setup(26,GPIO.OUT, initial=GPIO.HIGH)
#ustaw 19 jako wyjscie na brzeczek
GPIO.setup(19,GPIO.OUT, initial=GPIO.HIGH)

#ustaw 20 jako wejscie i sciagnij napiecie w dol
GPIO.setup(20,GPIO.IN)#, pull_up_down=GPIO.PUD_UP)
#ustaw 16 jako wejscie i sciagnij napiecie w dol
GPIO.setup(12,GPIO.IN)#, pull_up_down=GPIO.PUD_UP)

from mainwindow import Ui_MainWindow
from w_parameters import Ui_ParamWindow

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

pathname = os.path.dirname(sys.argv[0])
#run_motor_thread_lock = threading.Lock()


#TODO zapisz parametry do pliku i odczytaj z pliku
#TODO sprawdzic wyjscie na piszczalke


class CMain(QtGui.QMainWindow):
        def __init__(self):
                QtGui.QMainWindow.__init__(self)
                self.ui = Ui_MainWindow()
                self.ui.setupUi(self)
                
                self.ui.startBtn.clicked.connect(self.startBtn_Clicked)
                self.ui.resetCounterBtn.clicked.connect(self.resetCounterBtn_Clicked)
                self.ui.exitBtn.clicked.connect(self.exitBtn_Clicked)
                self.ui.paramBtn.clicked.connect(self.paramBtn_Clicked)
                
                self.ui.lcdClock.display(time.strftime("%H"+":"+"%M"+":"+"%S"))
                #timer input czy jest rozkaz od maszyny
#                self.check_input = QtCore.QTimer()
#                self.check_input.timeout.connect(self.checkInput)
                
                #timer input czy doliczyc cykl maszyny
                self.check_cycle = QtCore.QTimer()
                self.check_cycle.timeout.connect(self.checkCycle)
                
                self.check_cycle.stop()
                #self.check_input.stop()


                
        #przelic obroty silnika na pojedyncze kroki 
        def rot_to_steps(self, turns):
                steps = 200.*config.microstep*turns
                return steps

        def vel_to_pause(self, vel):
                pause = 1.0/(200.*config.microstep*vel)/2.0
                return pause

	def cycle_done(self, channel):                     
			config.cycles = config.cycles + 1
                        if config.cycles >= config.cycles_to_reset:
                               GPIO.output(19,GPIO.LOW)

                
        #zakrec silnik
        def move_motor(self, channel):
                if config.enable is True:
			#GPIO.setup(20,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
			#time.sleep(0.5)                        
			pause = self.vel_to_pause(float(config.velocity))
                        steps = self.rot_to_steps(float(config.rotates_per_cycle))
                        print "obracam motor o {}".format(steps)
                        print datetime.datetime.now()
                        for i in range(int(steps)):
                            GPIO.output(21,GPIO.HIGH)
                            time.sleep(pause)
                            GPIO.output(21,GPIO.LOW)
                            time.sleep(pause)
                        print "koniec obrotu"
                else:
                        print "probowalem w trybie zabronionym"
        	self.ui.lcdClock.display(time.strftime("%H"+":"+"%M"+":"+"%S"))
#        def checkInput(self):
#                if GPIO.input(20):
#                        if config.enable is True:
#                                self.move_motor(self.rot_to_steps(float(config.rotates_per_cycle)), self.vel_to_pause(float(config.velocity))) 
#                                time.sleep(0.2)
#                        else:
#                                print "probowalem w trybie zabronionym"
                        
        def checkCycle(self):
                        self.ui.lcdClock.display(time.strftime("%H"+":"+"%M"+":"+"%S"))
                        self.ui.lcdCounter.display(config.cycles)

        def resetCounterBtn_Clicked(self):
                config.cycles = 0
                GPIO.output(19,GPIO.HIGH)
                self.ui.lcdCounter.display(config.cycles)
                
        def startBtn_Clicked(self):
                if self.ui.startBtn.isChecked() == True:
                        print "wcisnalem"
                        config.enable = True
                        self.check_cycle.start(10)
                        #self.check_input.start(1)
			GPIO.add_event_detect(20, GPIO.RISING, callback = self.move_motor, bouncetime = 300)
			GPIO.add_event_detect(12, GPIO.FALLING, callback = self.cycle_done, bouncetime = 100)
                        self.ui.startBtn.setStyleSheet(_fromUtf8("background: red; color: white"))
                        self.ui.startBtn.setText("stop")
                        if config.cycles >= config.cycles_to_reset:
                               GPIO.output(19,GPIO.LOW)
                        else:
                               GPIO.output(19,GPIO.HIGH)
                else:
                        print "odcisnalem"
                        enable = False

                        GPIO.output(19,GPIO.HIGH)
                        GPIO.output(21,GPIO.LOW)
                        self.check_cycle.stop()
                        #self.check_input.stop()
			GPIO.remove_event_detect(12)
			GPIO.remove_event_detect(20)
                        self.ui.startBtn.setStyleSheet(_fromUtf8("background: green; color: white"))
                        self.ui.startBtn.setText("start")
        
        def paramBtn_Clicked(self):
                param_window.showFullScreen()
        
        def exitBtn_Clicked(self):
                self.close()
                self.check_cycle.stop()
                #self.check_input.stop()
                GPIO.cleanup()
                #os.system("shutdown now -h")                       
               
               
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
                
                self.ui.lcdSteps.display(config.rotates_per_cycle)
                self.ui.lcdVel.display(config.velocity)
                self.ui.lcdCycles.display(config.cycles_to_reset)
                
                self.pixmapUp = QtGui.QPixmap(_fromUtf8(pathname+"/images/up.png"))
                self.mapaUp = self.pixmapUp.createMaskFromColor(QtGui.QColor(255,255,255),0)
                self.pixmapUp.setMask(self.mapaUp)
                self.ui.upBtn.setIcon(QtGui.QIcon(self.pixmapUp))
                
                self.pixmapDown = QtGui.QPixmap(_fromUtf8(pathname+"/images/down.png"))
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
                
        def returnBtn_Clicked(self):
                config.rotates_per_cycle = self.ui.lcdSteps.value()
                config.velocity = self.ui.lcdVel.value()
                config.cycles_to_reset = self.ui.lcdCycles.value()
                self.setVisible(False)
                
                
if __name__=='__main__':

        app = QtGui.QApplication(sys.argv)
        main_window = CMain()
        param_window = CParamWindow()

        main_window.showFullScreen()
        print "1"
        sys.exit(app.exec_())
        GPIO.cleanup()
        print "2"
