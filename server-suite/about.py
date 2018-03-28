from PyQt4 import QtCore
from PyQt4 import QtGui as qt
import sys,os
class about(qt.QWidget):
	def work(self):
		qt.QWidget.__init__(self,parent=None)
		label_title=qt.QLabel("<img src='logo128x128.png' height='100' width='100'>",self)
		about_data="<center>Copyright "+u"\N{COPYRIGHT SIGN}"+" 2018 Saurabh Londhe</center><br><center>Version 1.0"
		label=qt.QLabel("<font color='black' size='5' >Server-Suite</font>",self)
		label1=qt.QLabel(about_data,self)
		self.setWindowIcon(qt.QIcon("images/logo128x128.png"))
		self.setWindowTitle("Server-Suite About")
		label1.move(40,170)
		label_title.move(100,20)
		label.move(100,130)
		x=300
		y=250
		screen = qt.QDesktopWidget().screenGeometry()
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.Popup)
		#self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
		ht=(screen.height()-y)/2
		wd=(screen.width()-x)/2
		self.setGeometry(wd,ht,x,y)
		self.setFixedSize(x,y)
	def __init__(self,parent=None):
		self.work()

