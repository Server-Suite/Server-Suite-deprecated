# -*- coding: utf-8 -*-
from PyQt4 import QtCore
from PyQt4 import QtGui as qt
import sys,os
class quick_http(qt.QWidget):
	def stop_http(self,show_path):
		try:
			show_path.setText("<font color='black'>PATH:</font>\t"+"<font color='black'><b>"+self.file+"</font>")
		except:
			file=os.getcwd()
			show_path.setText("<font color='black'>PATH:</font>\t"+"<font color='black'><b>"+os.getcwd()+"</font>")
	def open_folder(self,show_path):
		self.file = str(qt.QFileDialog.getExistingDirectory(self, "Select Directory"))
		show_path.setText("<font color='black'>PATH:</font>\t"+"<font color='black'><b>"+self.file+"</font>")
	def start_http(self):
		try:
			cmd="xterm -e 'cd "+self.file+" && python -m SimpleHTTPServer 8888'"
		except:
			cmd="xterm -e 'python -m SimpleHTTPServer 8888'"			
		os.system(cmd)
	def work(self):
		qt.QWidget.__init__(self,parent=None)
		self.setWindowIcon(qt.QIcon("images/logo128x128.png"))
		self.setWindowTitle("HTTP(quick)")
		back=qt.QLabel("<img src='images/http.jpg' height='400' width='500'>",self)
		ftp_logo=qt.QLabel("<img src='images/logo480x480.png' height='100' width='100'>",self)
		ftp_logo.move(200,120)
		warn=qt.QLabel("<font color='black'><b>For hosting choose folder with index.html file:</font>",self)
		warn.move(50,20)
		show_path=qt.QLabel("<font color='black'>PATH:</font>\t"+"<font color='black'><b>"+os.getcwd()+"</font>",self)
		show_path.move(50,75)
		choose=qt.QPushButton("choose",self)
		choose.clicked.connect(lambda:self.open_folder(show_path))
		choose.move(400,15)
		q_ftp=qt.QPushButton("start",self)
		q_ftp.setAutoDefault(True)
		q_ftp.clicked.connect(lambda:self.start_http())
		q_ftp.move(210,215)
		refresh=qt.QPushButton("refresh",self)
		refresh.clicked.connect(lambda:self.stop_http(show_path))
		refresh.move(400,70)
		Help=qt.QPushButton(self)
		Help.setIcon(qt.QIcon(qt.QPixmap("images/help.png")))
		Help.setToolTip('<b>HELP!</b>')
		Help.clicked.connect(lambda:self.msg())
		Help.move(20,250)
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		close=qt.QPushButton(self)
		close.setIcon(qt.QIcon(qt.QPixmap("images/close.png")))
		close.move(470,0)
		close.clicked.connect(lambda:self.close())
		screen = qt.QDesktopWidget().screenGeometry()
		ht=(screen.height()-300)/2
		wd=(screen.width()-500)/2
		self.setGeometry(wd,ht,500,300)
		self.setFixedSize(500,400)
	def msg(self):
		qt.QMessageBox.information(self,"Help!", "This program runs in 'xterm' terminal so it must be installed. If Xterm isn't installed then you can install by using <font color='red'><b>'sudo apt-get install xterm'</font> or <font color='red'><b>'sudo dnf install xterm'</font> For closeing HTTP server use <font color='red'><b> ctrl+c</font> or <font color='red'><b>close </font>the terminal")
	def __init__(self,parent=None):
		self.work()
"""
app = qt.QApplication(sys.argv)
main_window = quick_http()
main_window.show()
sys.exit(app.exec_())"""