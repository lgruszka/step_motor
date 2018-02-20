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
#12 jako wejscie na sygnal z maszyny czy cykl wykonano
#16 jako wejscie na sygnal reset z przycisku
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

#ustaw 20 jako wejscie i sciagnij napiecie w gore
GPIO.setup(20,GPIO.IN, pull_up_down=GPIO.PUD_UP)
#ustaw 12 jako wejscie i sciagnij napiecie w gore
GPIO.setup(12,GPIO.IN, pull_up_down=GPIO.PUD_UP)
#ustaw 16 jako wejscie i sciagnij napiecie w gore
# GPIO.setup(16,GPIO.IN, pull_up_down=GPIO.PUD_UP)

from mainwindow import Ui_MainWindow
from Cparameter_window import CParamWindow
from Cnew_program_window import CNewProgramWindow
from Cload_program_window import CLoadProgramWindow

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

config.pathname = os.path.dirname(sys.argv[0])
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
                self.ui.blockScreenBtn.clicked.connect(self.blockScreenBtn_Clicked)
                self.ui.exitBtn.clicked.connect(self.exitBtn_Clicked)
                self.ui.paramBtn.clicked.connect(self.paramBtn_Clicked)
                
                self.ui.lcdClock.display(time.strftime("%H"+":"+"%M"+":"+"%S"))
                # timer input czy jest rozkaz od maszyny
                # self.check_input = QtCore.QTimer()
                # self.check_input.timeout.connect(self.checkInput)
                
                # timer input czy doliczyc cykl maszyny
                self.check_cycle = QtCore.QTimer()
                self.check_cycle.timeout.connect(self.checkCycle)
                
                self.check_cycle.stop()
                # self.check_input.stop()


                
        # przelicz obroty silnika na pojedyncze kroki 
        def rot_to_steps(self, turns):
                steps = 200.*config.microstep*turns
                return steps

        def vel_to_pause(self, vel):
                pause = 1.0/(200.*config.microstep*vel)/2.0
                return pause

        def cycle_done(self, channel): 
                        count = 0
                        while(count<10):
                                if GPIO.input(12) == 0:
                                        count=count+1
                                        time.sleep(0.01)
                                        print "cycle done {}".format(count)
                                else:
                                        print "fake cycle sygnal"
                                        return            
                        config.cycles = config.cycles + 1
                        if config.cycles >= config.cycles_to_reset:
                               GPIO.output(19,GPIO.LOW)
                        time.sleep(1.5)
                        self.ui.lcdClock.display(time.strftime("%H"+":"+"%M"+":"+"%S"))

        def reset_ext_btn(self, channel): 
                    count = 0
                    while(count<5):
                                if GPIO.input(16) == 0:
                                        count=count+1
                                        time.sleep(0.01)
                                        print "button pressed {}".format(count)
                                else:
                                        print "fake button sygnal"
                                        return            
                    self.resetCounterBtn_Clicked()

                
        #zakrec silnik
        def move_motor(self, channel):
                count = 0
                while (count < 6):
                        if GPIO.input(20) == 0:
                                count=count+1
                                time.sleep(0.03)
                                print "move motor {}".format(count)
                        else:
                                print "fake motor sygnal"
                                return                
                if config.enable is True:
                        #GPIO.setup(20,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
                        #time.sleep(0.5)                        
                        pause = self.vel_to_pause(float(config.velocity))
                        steps = self.rot_to_steps(float(config.rotates_per_cycle))
                        move_time = 2*pause*steps
                        print move_time

                        print "obracam motor o {}".format(steps)
                        print datetime.datetime.now()
                        for i in range(int(steps)):
                            GPIO.output(21,GPIO.HIGH)
                            time.sleep(pause)
                            GPIO.output(21,GPIO.LOW)
                            time.sleep(pause)
                        print "koniec obrotu"
                        if move_time <2.2:
	                        time.sleep(2.2-move_time)
                        else:
	                        pass 
                else:
                        print "probowalem w trybie zabronionym"
                        
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
                        GPIO.add_event_detect(20, GPIO.FALLING, callback = self.move_motor)
                        GPIO.add_event_detect(12, GPIO.FALLING, callback = self.cycle_done)
                        # GPIO.add_event_detect(16, GPIO.FALLING, callback = self.reset_ext_btn)
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
                        # GPIO.remove_event_detect(16)
                        GPIO.remove_event_detect(20)
                        self.ui.startBtn.setStyleSheet(_fromUtf8("background: green; color: white"))
                        self.ui.startBtn.setText("start")
        
        def paramBtn_Clicked(self):
                config.param_window.showFullScreen()
        
        def blockScreenBtn_Clicked(self):
                QtGui.QMessageBox.information(self,'Info',"Blokada ekranu",QtGui.QMessageBox.Cancel)
        
        def exitBtn_Clicked(self):
                self.close()
                self.check_cycle.stop()
                #self.check_input.stop()
                GPIO.cleanup()
                
                '''try:
                        os.system("sudo shutdown -h now")
                except:
                        os.system("shutdown now -h")'''                       
               
               

                
if __name__=='__main__':

        app = QtGui.QApplication(sys.argv)
        main_window = CMain()
        config.param_window = CParamWindow()
        config.new_program_window = CNewProgramWindow()
        config.load_program_window = CLoadProgramWindow()

        main_window.showFullScreen()
        print "1"
        sys.exit(app.exec_())
        GPIO.cleanup()
        print "2"
