from PyQt4 import QtCore
from PyQt4 import QtGui as qt
import sys,os
class deb_ftp_menu(qt.QWidget):
	def pureftp(self):
		print "pure"
	def vsftp(self):
		print "vsftp"
	def proftp(self):
		print "proftp"
		import deb_proftp
		self.o=deb_proftp.deb_proftp()
		self.o.show()
	def work(self):
		qt.QWidget.__init__(self,parent=None)
		self.setWindowIcon(qt.QIcon("images/logo128x128.png"))
		self.setWindowTitle("Server-Suite About")
		self.back=qt.QLabel("<img src='images/blur.png' height='250' width='330'>",self)
		self.vsftp_b=qt.QPushButton("vsftp",self)
		self.vsftp_b.clicked.connect(lambda:self.vsftp())
		self.vsftp_b.move(20,100)
		self.proftp_b=qt.QPushButton("proftp",self)
		self.proftp_b.clicked.connect(lambda:self.proftp())
		self.proftp_b.move(120,100)
		self.pureftp_b=qt.QPushButton("pureftp",self)
		self.pureftp_b.clicked.connect(lambda:self.pureftp())
		self.pureftp_b.move(220,100)
		x=330
		y=250
		screen = qt.QDesktopWidget().screenGeometry()
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.Popup)
		self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
		ht=(screen.height()-y)/2
		wd=(screen.width()-x)/2
		self.setGeometry(wd,ht,x,y)
		self.setFixedSize(x,y)
	def __init__(self,parent=None):
		self.work()
"""
app = qt.QApplication(sys.argv)
main_window = deb_ftp_menu()
main_window.show()
sys.exit(app.exec_())"""