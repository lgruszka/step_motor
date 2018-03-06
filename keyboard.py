#!/usr/bin/env python
# -*- coding: utf-8 -*-
# simple.py

import sys
import os
import time
import subprocess
from PyQt4 import QtCore,QtGui,QtDBus


class Open(object):
    def __init__(self):
        u"""
        Otwiera program onboard
        """
        screenH = QtGui.QApplication.desktop().size().height()
        screenW = QtGui.QApplication.desktop().size().width()
        heigh = int(screenH*0.5) #wysokosc 1/2 ekranu
        width = screenW # 3*heigh #szerokosc proporcjonalnie 3x wysokosc
        y = int(screenH*0.5) #wyswietlana na samym dole ekranu
        x = screenW/2 - width/2 #wyswietlana w polowie szerokosci ekranu
        
        self.klawiatura = subprocess.Popen(["onboard","-x "+str(x),"-y "+str(y),"-s "+str(width)+"x"+str(heigh),"-a"])
        Hide()
    def Close(self):
        u"""
        Zamyka program odboard
        """
        self.klawiatura.kill()
        
def Show():
    u"""
    Pokazuje klawiature onboard
    """
    time.sleep(0.1)
    QtDBus.QDBusConnection.sessionBus().send(QtDBus.QDBusMessage.createMethodCall('org.onboard.Onboard', '/org/onboard/Onboard/Keyboard','org.onboard.Onboard.Keyboard','Show'))
    
def Hide():
    u"""
    Ukrywa klawiature onboard
    """
    time.sleep(0.1)
    QtDBus.QDBusConnection.sessionBus().send(QtDBus.QDBusMessage.createMethodCall('org.onboard.Onboard', '/org/onboard/Onboard/Keyboard','org.onboard.Onboard.Keyboard','Hide'))

if __name__ == '__main__':
    Open()
