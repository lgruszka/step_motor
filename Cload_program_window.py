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
        #self.ui.programCmbBox.clicked.connect(self.programCmbBox_Clicked)
        

    def programCmbBox_Clicked(self):
            self.ui.programCmbBox.clear()
            prg_list = [prg.split('.txt')[0] for prg in os.listdir(config.pathname+"/programy") if '.txt' in prg]
            prg_list.sort()
            for i in prg_list:
                self.ui.programCmbBox.addItem(_fromUtf8(i))
            self.ui.programCmbBox.setCurrentIndex(-1)
