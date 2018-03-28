from PyQt4 import QtGui as qt
import os,sys
class help(qt.QWidget):
    def __init__(self,parent=None):
        qt.QWidget.__init__(self,parent=None)
        self.setWindowTitle("Server-Suite Help")
        self.setWindowIcon(qt.QIcon("images/logo128x128.png"))
        label=qt.QLabel("< img src='images/title-2.png' height='100' width='500''>",self)
        label1=qt.QLabel("< img src='images/logo128x128.png' height='75' width='80'>",self)
        text=qt.QLabel("<font color='black' size=4 face='arial'>Server-Suite</font>",self)
        text.move(212,70)
        label1.move(215,00)
        self.setFixedSize(500,500)
        screen = qt.QDesktopWidget().screenGeometry()
        ht=(screen.height()-500)/2
        wd=(screen.width()-500)/2
        self.setGeometry(wd,ht,500,500)
