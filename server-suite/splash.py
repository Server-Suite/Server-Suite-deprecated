from PyQt4 import QtCore
from PyQt4 import QtGui as qt
import sys,os,time,thread
class splash(qt.QWidget):
	def __init__(self,parent=None):
		app = qt.QApplication(sys.argv)
		qt.QWidget.__init__(self,parent=None)
		self.setWindowIcon(qt.QIcon("images/logo128x128.png"))
		self.setWindowTitle("Server-Suite")
		back=qt.QLabel("<img src='images/space.jpg' height='300' width='500'>",self)
		logo=qt.QLabel("<img src='images/logo128x128.png' height='120' width='120'>",self)
		slogn=qt.QLabel("<font color='black' size='4'><b>We configure world with Server-Suite</font>",self)
		name=qt.QLabel("<font color='black' size='1'>Designed by Saurabh Londhe</font>",self)
		slogn.move(110,200)
		logo.move(190,65)
		name.move(200,285)
		screen = qt.QDesktopWidget().screenGeometry()
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		ht=(screen.height()-300)/2
		wd=(screen.width()-500)/2
		self.setGeometry(wd,ht,500,300)
		self.setFixedSize(500,300)
		thread.start_new_thread(self.close_window,())
		self.show()
		sys.exit(app.exec_())
		self.serv=serv.server()
		self.show()
	def close_window(self):
		time.sleep(4)
		self.close()
		os.system("python serv.py")
"""
app = qt.QApplication(sys.argv)
main_window = splash()
main_window.show()
#sys.exit(app.exec_())"""
s=splash()