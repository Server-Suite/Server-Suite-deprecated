# -*- coding: utf-8 -*-
from PyQt4 import QtCore
from PyQt4 import QtGui as qt
import sys,os
class about(qt.QWidget):
	def stop_ftp(self,show_path):
		try:
			show_path.setText("PATH:\t"+"<font color='red'>"+self.file+"</font>")
		except:
			file=os.getcwd()
			show_path.setText("PATH:\t"+"<font color='red'>"+os.getcwd()+"</font>")
	def open_folder(self,show_path):
		self.file = str(qt.QFileDialog.getExistingDirectory(self, "Select Directory"))
		show_path.setText("PATH:\t"+"<font color='red'>"+self.file+"</font>")
	def strat_ftp(self):
		try:
			cmd="xterm -e 'python ftp_server.py "+self.file+"'"
		except:
			cmd="xterm -e 'python ftp_server.py "+str(os.getcwd())+"'"
		os.system(cmd)
	def work(self):
		qt.QWidget.__init__(self,parent=None)
		self.setWindowIcon(qt.QIcon("images/logo128x128.png"))
		self.setWindowTitle("FTP(quick)")
		back=qt.QLabel("<img src='images/tree.jpg' height='300' width='500'>",self)
		ftp_logo=qt.QLabel("<img src='images/ftp-server.png' height='100' width='100'>",self)
		ftp_logo.move(200,120)
		warn=qt.QLabel("<font color='green'><b>For hosting You need to choose folder:</font>",self)
		warn.move(50,20)
		show_path=qt.QLabel("<font color='black'>PATH:<font>\t"+"<font color='red'>"+os.getcwd()+"</font>",self)
		show_path.move(50,75)
		choose=qt.QPushButton("choose",self)
		choose.clicked.connect(lambda:self.open_folder(show_path))
		choose.move(400,15)
		q_ftp=qt.QPushButton("start",self)
		q_ftp.setAutoDefault(True)
		q_ftp.clicked.connect(lambda:self.strat_ftp())
		q_ftp.move(210,215)
		refresh=qt.QPushButton("refresh",self)
		refresh.clicked.connect(lambda:self.stop_ftp(show_path))
		refresh.move(400,70)
		Help=qt.QPushButton(self)
		Help.setIcon(qt.QIcon(qt.QPixmap("images/help.png")))
		Help.clicked.connect(lambda:self.msg())
		Help.move(20,250)
		screen = qt.QDesktopWidget().screenGeometry()
		ht=(screen.height()-500)/2
		wd=(screen.width()-500)/2
		self.setGeometry(wd,ht,500,500)
		self.setFixedSize(500,300)
	def msg(self):
		qt.QMessageBox.information(self,"Help!", "This program runs in 'xterm' terminal so it must be installed. If Xterm isn't installed then you can install by using <font color='red'><b>'sudo apt-get install xterm'</font> or <font color='red'><b>'sudo dnf install xterm'</font> For closeing FTP server use <font color='red'><b> ctrl+c</font> or <font color='red'><b>close </font>the terminal")
	def __init__(self,parent=None):
		self.work()
"""
app = qt.QApplication(sys.argv)
main_window = about()
main_window.show()
sys.exit(app.exec_())"""