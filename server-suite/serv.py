#!/usr/bin/python
#----------------------------------------------------------------
import os
import deb_server_list,rpm_server_list,help,update,about,cpu_status,quick_server,alwayson,Settings
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
	def go_for_server(self,detected_os):
		rpm_list={"fedora","centos","redhat"}
		deb_list={"kali","ubuntu","debian"}
		detected_os=platform.linux_distribution()[0]
		f=open(".os_name.txt","w")
		f.write(detected_os)
		f.close()
		if detected_os.lower() in rpm_list:
			self.rpm=rpm_server_list.rpm_server_list()
			self.rpm.show()
		elif detected_os.lower() in deb_list:
			self.deb=deb_server_list.deb_server_list()
			self.deb.show()
		#os.system("python get_distro.py "+detected_os)
	def get_os(self,frame,combobox):
		self.selected_os=combobox.currentText()
		selected_os=str(self.selected_os)
		f=open(".os_name.txt","w")
		f.write(selected_os.lower())
		f.close()
		rpm_list={"fedora","centos","redhat"}
		deb_list={"kali","ubuntu","debian"}
		if selected_os.lower() in rpm_list:
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
	def show_splash(self):
		try:
			self.sp=alwayson.on()
			self.sp.show()
		except:
			pass
	def show_settings(self):
		self.o=Settings.settings_class()
		self.o.show()
	def __init__(self):
		self.window=qt.QApplication(sys.argv)
		flag=True
		frame=qt.QWidget()
		label=qt.QLabel("< img src='images/back-6.1.jpg' height='500' width='500'>",frame)
		pic = qt.QLabel("<img src='images/logo128x128.png' height='50' width='50' >",frame)
		settings = qt.QLabel("<img src='images/settings1.png' height='20' width='20' >",frame)
		label1=qt.QLabel("<font color='black'>Detected OS: <font>",frame)
		detected_os=self.detectos()
		label2=qt.QLabel("<font color='green'>"+detected_os+"</font>",frame)
		label3=qt.QLabel("Choose OS :",frame)
		label3.setHidden(True)
		check_update=qt.QPushButton("Check for update..",frame)
		about=qt.QPushButton("About",frame)
		help_btn=qt.QPushButton("Help",frame)
		cbox=qt.QCheckBox("If detected OS is not correct . .",frame)
		#cpu_btn=qt.QPushButton("Start Http CUP",frame)
		combobox=qt.QComboBox(frame)
		combobox.addItem("Fedora")
		combobox.addItem("Ubuntu")
		combobox.addItem("CentOS")
		combobox.addItem("Kali")
		combobox.addItem("Debian")
		combobox.addItem("Redhat")
		combobox.setHidden(True)
		btn1=qt.QPushButton("OK",frame)
		btn2=qt.QPushButton("OK",frame)
		settings_btn=qt.QPushButton(frame)
		btn1.setHidden(True)
		btn1.clicked.connect(lambda:self.get_os(frame,combobox))
		btn2.clicked.connect(lambda:self.go_for_server(detected_os))
		cbox.stateChanged.connect(lambda:self.cboxchecked(label3,combobox,cbox,btn1,btn2))
		about.clicked.connect(lambda:self.show_about())
		#about.returnPressed.connect(lambda:self.show_about())
		check_update.clicked.connect(lambda:self.show_update())
		help_btn.clicked.connect(lambda:self.show_help())
		settings_btn.clicked.connect(lambda:self.show_settings())
		quick_server_lbl=qt.QLabel("<img src='images/5-sec.svg' height='25' width='25'>",frame)
		quick_server_lbl.move(320,250)
		quick_server=qt.QPushButton(frame)
		quick_server.setGeometry(320,250,40,40)
		quick_server.setStyleSheet("background-color:transparent;border:2;")
		#quick_server.setIcon(qt.QIcon(qt.QPixmap("images/5-sec.png")))
		quick_server.setToolTip('Server in just <b>5 seconds!</b>')
		quick_server.clicked.connect(lambda:self.quick_start_server())
		pic.move(235,30)
		settings.move(475,5)
		settings_btn.setStyleSheet("background-color:transparent;border:0;")
		settings_btn.move(470,5)
		settings_btn.setFixedSize(30,30)
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
		frame.setWindowIcon(qt.QIcon("images/logo.svg"))
		frame.setWindowTitle("Server-Suite")
		frame.setFixedSize(500,500)
		screen = qt.QDesktopWidget().screenGeometry()
		ht=(screen.height()-500)/2
		wd=(screen.width()-500)/2
		frame.setGeometry(wd,ht,500,500)
		#thread.start_new_thread(self.show_splash,())
		self.show_splash()
		frame.show()
		sys.exit(self.window.exec_())
		
	def closeEvent(self,event,frame):
		result = qt.QMessageBox.question(frame,
                      "Confirm Exit...",
                      "Are you sure you want to exit ?",
                      qt.QMessageBox.Yes| qt.QMessageBox.No)
	def closeEvent(self, event): 
		print "Closing" 
		self.destory()
	def cboxchecked(self,label3,combobox,cbox,btn1,btn2):
			if cbox.isChecked() == True:
				#print "box is selected"
				label3.setHidden(False)
				combobox.setHidden(False)
				btn1.setHidden(False)
				btn2.setHidden(True)
			else:
				#print "box is deselected"
				label3.setHidden(True)
				combobox.setHidden(True)
				btn1.setHidden(True)
				btn2.setHidden(False)


obj=server()

