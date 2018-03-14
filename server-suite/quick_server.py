from PyQt4 import QtCore
from PyQt4 import QtGui as qt
import sys,os,quick_ftp,quick_http
class quick_server(qt.QWidget):
	def start_ftp(self):
		self.o=quick_ftp.quick_ftp()
		self.o.show()
	def start_http(self):
		self.o=quick_http.quick_http()
		self.o.show()
	def work(self):
		qt.QWidget.__init__(self,parent=None)
		self.setWindowIcon(qt.QIcon("images/logo128x128.png"))
		self.setWindowTitle("quick_server")
		back=qt.QLabel("<img src='images/space.jpg' height='400' width='500'>",self)
		logo=qt.QLabel("<img src='images/logo128x128.png' height='120' width='120'>",self)
		logo.move(190,30)
		ftp=qt.QPushButton("FTP",self)
		ftp.clicked.connect(lambda:self.start_ftp())
		http=qt.QPushButton("HTTP",self)
		http.clicked.connect(lambda:self.start_http())
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		close=qt.QPushButton(self)
		close.setIcon(qt.QIcon(qt.QPixmap("images/close.png")))
		close.move(470,0)
		close.clicked.connect(lambda:self.close())
		ftp.move(50,200)
		http.move(370,200)
		screen = qt.QDesktopWidget().screenGeometry()
		ht=(screen.height()-300)/2
		wd=(screen.width()-500)/2
		self.setGeometry(wd,ht,500,300)
		self.setFixedSize(500,400)
	def __init__(self,parent=None):
		self.work()
"""
app = qt.QApplication(sys.argv)
main_window = quick_server()
main_window.show()
sys.exit(app.exec_())"""