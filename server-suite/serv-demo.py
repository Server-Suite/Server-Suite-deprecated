#!/usr/bin/python
#----------------------------------------------------------------
import os
import deb_server_list,rpm_server_list,help,update,about,cpu_status,quick_server#,splash
import PyQt4
from PyQt4 import QtGui as qt
from PyQt4 import QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys,platform,time,thread
class server(qt.QWidget):
	def keyPressEvent(self, event):
		print "helo"
		if event.key() == QtCore.Qt.Key_Escape:
			self.close()
	def go_for_server(self):
		rpm_list={"fedora","centos","redhat"}
		deb_list={"kali","ubuntu","debian"}
		self.detected_os=platform.linux_distribution()[0]
		f=open(".os_name.txt","w")
		f.write(self.detected_os)
		f.close()
		if self.detected_os.lower() in rpm_list:
			self.rpm=rpm_server_list.rpm_server_list()
			self.rpm.show()
		elif self.detected_os.lower() in deb_list:
			self.deb=deb_server_list.deb_server_list()
			self.deb.show()
		#os.system("python get_distro.py "+detected_os)
	def get_os(self):
		self.selected_os=self.combobox.currentText()
		selected_os=str(self.selected_os)
		f=open(".os_name.txt","w")
		f.write(selected_os.lower())
		f.close()
		rpm_list={"fedora","centos","redhat"}
		deb_list={"kali","ubuntu","debian"}
		if self.selected_os.lower() in rpm_list:
			self.rpm=rpm_server_list.rpm_server_list()
			self.rpm.show()
		else:# selected_os.lower() in deb_list:
			self.deb=deb_server_list.deb_server_list()
			self.deb.show()
	def show_about(self):
		self.o=about.about()
		self.o.show()
	def show_update(self):
		self.u=update.update()
		self.u.show()
		return
	def detectos(self):
		temp=platform.linux_distribution()
		ver=temp[0]+" "+temp[1]
		return ver
	def show_help(self):
		self.h=help.help()
		self.h.show()
	def show_cpu_status(self):
		o=cpu_status.cpu()
	def quick_start_server(self):
		self.ftp_ob=quick_server.quick_server()
		self.ftp_ob.show()
	def show_splash(self,frame):
		self.sp=splash.splash()
		self.sp.show()
		time.sleep(2)
		#self.sp.close()
		frame.show()
	def __init__(self,parent=None):
		qt.QWidget.__init__(self,parent=None)
		label=qt.QLabel("< img src='images/back-6.jpg' height='500' width='500'>",self)
		pic = qt.QLabel("<img src='images/logo128x128.png' height='50' width='50' >",self)
		label1=qt.QLabel("<font color='black'>Detected OS: <font>",self)
		detected_os=self.detectos()
		label2=qt.QLabel("<font color='green'>"+detected_os+"</font>",self)
		label3=qt.QLabel("Choose OS :",self)
		label3.setHidden(True)
		check_update=qt.QPushButton("Check for update..",self)
		about=qt.QPushButton("About",self)
		help_btn=qt.QPushButton("Help",self)
		cbox=qt.QCheckBox("If detected OS is not correct . .",self)
		combobox=qt.QComboBox(self)
		combobox.addItem("Fedora")
		combobox.addItem("Ubuntu")
		combobox.addItem("CentOS")
		combobox.addItem("Kali")
		combobox.addItem("Debian")
		combobox.addItem("Redhat")
		combobox.setHidden(True)
		btn1=qt.QPushButton("OK",self)
		btn2=qt.QPushButton("OK",self)
		btn1.setHidden(True)
		btn1.clicked.connect(lambda:self.get_os())
		btn2.clicked.connect(lambda:self.go_for_server())
		cbox.stateChanged.connect(lambda:self.cboxchecked(self.cbox))
		about.clicked.connect(lambda:self.show_about())
		#about.returnPressed.connect(lambda:self.show_about())
		check_update.clicked.connect(lambda:self.show_update())
		help_btn.clicked.connect(lambda:self.show_help())
		#cpu_btn.clicked.connect(lambda:self.show_cpu_status())
		quick_server=qt.QPushButton(self)
		quick_server.setIcon(qt.QIcon(qt.QPixmap("images/5-sec.png")))
		quick_server.setToolTip('Server in just <b>5 seconds!</b>')
		quick_server.clicked.connect(lambda:self.quick_start_server())
		pic.move(235,30)
		label1.move(170,100)
		label2.move(270,100)
		cbox.move(150,150)
		label3.move(170,205)
		combobox.move(250,200)
		btn1.move(220,250)
		btn2.move(220,250)
		help_btn.move(40,450)
		about.move(215,450)
		check_update.move(350,450)
		quick_server.move(320,250)
		self.setWindowIcon(qt.QIcon("images/logo.svg"))
		self.setWindowTitle("Server-Suite")
		self.setFixedSize(500,500)
		screen = qt.QDesktopWidget().screenGeometry()
		ht=(screen.height()-500)/2
		wd=(screen.width()-500)/2
		self.setGeometry(wd,ht,500,500)
		#thread.start_new_thread(self.show_splash,(self,))
		#self.show()
		#sys.exit(self.window.exec_())
	def cboxchecked(self,cbox):
			if self.cbox.isChecked() == True:
				#print "box is selected"
				self.label3.setHidden(False)
				self.combobox.setHidden(False)
				self.btn1.setHidden(False)
				self.btn2.setHidden(True)
			else:
				#print "box is deselected"
				self.label3.setHidden(True)
				self.combobox.setHidden(True)
				self.btn1.setHidden(True)
				self.btn2.setHidden(False)

app = qt.QApplication(sys.argv)
main_window = server()
main_window.show()
sys.exit(app.exec_())
