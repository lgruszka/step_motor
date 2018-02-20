#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import os

import config
form w_new_program import Ui_LoadProgramWindow 

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s


class CLoadProgramWindow(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_LoadProgramWindow()
        self.ui.setupUi(self)
        self.ui.programCmbBox.clicked.connect(self.programCmbBox_Clicked)
