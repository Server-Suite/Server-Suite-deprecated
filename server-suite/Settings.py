from PyQt4 import QtCore
from PyQt4 import QtGui as qt
import sys,os
class settings_class(qt.QWidget):
	def work(self):
		qt.QWidget.__init__(self,parent=None)
		self.setWindowIcon(qt.QIcon("images/logo128x128.png"))
		self.setWindowTitle("Server-Suite About")
		#self.setWindowOpacity(0.75)
		self.remove_lock=qt.QLabel("<img src='images/lock.png' height='40' width='40'>",self)
		self.remove_lock.move(30,30)
		self.remove_lock_btn=qt.QPushButton(self)
		self.remove_lock_btn.setStyleSheet("background-color:transparent;border:0;")
		self.remove_lock_btn.setGeometry(30,30,40,40)
		self.remove_lock_btn.clicked.connect(lambda:os.system("rm alwayson.lock"))
		self.remove_lock_btn.setToolTip('<font color="white">remove alwayson.lock</font>')

		self.http_host=qt.QLabel("<img src='images/share.png' height='40' width='40'>",self)
		self.http_host.move(30,80)
		self.http_host_btn=qt.QPushButton(self)
		self.http_host_btn.setStyleSheet("background-color:transparent;border:0;")
		self.http_host_btn.setGeometry(30,80,40,40)
		self.http_host_btn.clicked.connect(lambda:os.system("echo 'start'"))#("xterm -e 'python online_cpu_status.py'"))
		self.http_host_btn.setToolTip('<font color="white">share server status</font>')
		self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
		x=100
		y=250
		screen = qt.QDesktopWidget().screenGeometry()
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.Popup)
		ht=(screen.height()/2)-250
		wd=(screen.width()/2)+250
		self.setGeometry(wd,ht,x,y)
		self.setFixedSize(x,y)
	def __init__(self,parent=None):
		self.work()
"""
app = qt.QApplication(sys.argv)
main_window = settings_class()
main_window.show()
sys.exit(app.exec_())"""