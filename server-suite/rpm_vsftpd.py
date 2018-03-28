#!/usr/bin/python
#------Coded by Saurabh Londhe------------#
#------https://github.com/saurabhlondhe---#
import os,sys,thread
from PyQt4 import QtGui as qt
class test:
	global flag_anonymous
	global flag_allow_ascii_mode
	global flag_enable_chroot
	global flag_listen_ipv4
	global flag_listen_ipv6
	def ftp_service_start(self):
		#os.system("systemctl start vsftpd")
		return
	def ftp_service_enable(self):
		#os.system("systemctl enable vsftpd")
		return
	def ftp_service_restart(self):
		#os.system("systemctl restart vsftpd")
		return
	def ftp_service_stop(self):
		#os.system("systemctl stop vsftpd")
		return
	def firewall(self):
		#os.system("firewall-cmd --add-service=ftp --permanent")
		#os.system("firewall-cmd --reload")
		return
		
	def __init__(self):
		#---------------------------------------------------------------------------------------------------------
		flag_anonymous=False
		flag_allow_ascii_mode=False
		flag_enable_chroot=False
		flag_listen_ipv4=False
		flag_listen_ipv6=False
		#---------------------------------------------------------------------------------------------------------
		w=qt.QApplication(sys.argv)
		frame=qt.QWidget()
		frame.setWindowTitle("Server-Suite FTP")
		#frame.setWindowIcon(qt.QIcon("images/logo.svg"))
		ftp_label=qt.QLabel("<img src='images/ftp.png' height='70' width='60'>",frame)
		service_label=qt.QLabel("<font color='red'>vsftpd services</font>",frame)
		#--------------------------------------------------------------------------------------------------------
		cbox_ftp_anonymous=qt.QCheckBox("Anonymous user",frame)
		cbox_ftp_anonymous.stateChanged.connect(lambda:self.ftp_anonymous(cbox_ftp_anonymous,flag_anonymous))
		cbox_ftp_listen_ipv4=qt.QCheckBox("Enable IPv4",frame)
		cbox_ftp_listen_ipv4.stateChanged.connect(lambda:self.ftp_listen_ipv4(cbox_ftp_listen_ipv4,flag_listen_ipv4))
		cbox_ftp_listen_ipv6=qt.QCheckBox("Enable IPv6",frame)
		cbox_ftp_listen_ipv6.stateChanged.connect(lambda:self.ftp_listen_ipv6(cbox_ftp_listen_ipv6,flag_listen_ipv6))
		
		#----------------------------------------------------------------------------------------------------------
		btn_start_service=qt.QPushButton("strat",frame)
		btn_restart_service=qt.QPushButton("restart",frame)
		btn_enable_service=qt.QPushButton("enable",frame)
		btn_stop_service=qt.QPushButton("stop",frame)
		btn_ok=qt.QPushButton("Ok",frame)
		#----------------------------------------------------------------------------------------------------------
		btn_start_service.clicked.connect(lambda:self.start_ftp_service_start())
		btn_ok.clicked.connect(lambda:self.make_conf_file(flag_anonymous,flag_listen_ipv4,flag_listen_ipv6))
		service_label.move(20,370)
		btn_start_service.move(50,400)
		btn_restart_service.move(150,400)
		btn_enable_service.move(250,400)
		btn_stop_service.move(350,400)
		btn_ok.move(400,450)
		frame.setGeometry(100,100,500,500)
		frame.show()
		cbox_ftp_anonymous.move(50,150)
		cbox_ftp_listen_ipv4.move(50,170)
		cbox_ftp_listen_ipv6.move(50,190)
		#cbox.setFixedSize(400,300)
		#self.top(frame,l)
		w.exec_()
	def set_commands(self):
		os.system("sudo dnf -y install vsftpd")
		os.system("cp /etc/vsftpd/vsftpd.conf /etc/vsftpd/vsftpd-conf.bak")
	def ftp_anonymous(self,cbox_ftp_anonymous,flag_anonymous):
		if cbox_ftp_anonymous.isChecked()==True:
			self.flag_anonymous=True
			return self.flag_anonymous
		else:
			self.flag_anonymous=False
			return self.flag_anonymous
	def uncomment(self):
		print 'uncomment'
		#uncomment lines
	def ftp_listen_ipv4(self,cbox_ftp_listen_ipv4,flag_listen_ipv4):
		if cbox_ftp_listen_ipv4.isChecked()==True:
			self.flag_listen_ipv4=True
		else:
			self.flag_listen_ipv4=False
	def ftp_listen_ipv6(self,cbox_ftp_listen_ipv6,flag_listen_ipv6):
		if cbox_ftp_listen_ipv6.isChecked()==True:
			self.flag_listen_ipv6=True
		else:
			self.flag_listen_ipv6=False
	def add_at_end(self):
		print 'line'
		#add lines
		#local_root=public_html
		#use_localtime=YES
		#seccomp_sandbox=NO
	def make_conf_file(self,flag_anonymous,flag_listen_ipv4,flag_listen_ipv6):
		f=open("vsftpd.conf")	#("/etc/vsftpd/vsftpd.conf")
		s=f.read()
		print str(self.flag_anonymous)
		print str(self.flag_listen_ipv6)
		print str(self.flag_listen_ipv4)
		if self.flag_anonymous:
			s=s.split("ascii_upload_enable=YES")
			s=s[0]+"\nascii_upload_enable=YES"+s[1]
			f.write(s)
		



obj=test()
#===========================================================================================
"""
[root@www ~]# vi /etc/vsftpd/vsftpd.conf

# line 12: no anonymous
anonymous_enable=NO

# line 82,83: uncomment ( allow ascii mode )
ascii_upload_enable=YES
ascii_download_enable=YES

# line 100,101: uncomment ( enable chroot )
chroot_local_user=YES
chroot_list_enable=YES

# line 103: uncomment ( chroot list file )
chroot_list_file=/etc/vsftpd/chroot_list

# line 109: uncomment
ls_recurse_enable=YES

# line 114: change (if listening IPv4 only)
# if listning IPv4 and IPv6 both, specify "NO"
listen=YES

# line 123: change (if listening IPv6 only)
# if listning IPv4 and IPv6 both, specify "YES"
listen_ipv6=NO

# add to the end
# specify root directory (if don't specify, users' home directory become FTP home directory)
local_root=public_html

# use local time
use_localtime=YES

# turn off for seccomp filter (if you cannot login, add this line)
seccomp_sandbox=NO
#------------------------------------------------------------------------------------
[root@www ~]# vi /etc/vsftpd/chroot_list

# add users you allow to move over their home directory
fedora
[root@www ~]# systemctl start vsftpd 
[root@www ~]# systemctl enable vsftpd 
#-------------------------------------------------------------------------------------
[root@www ~]# vi /etc/vsftpd/vsftpd.conf

# add to the end: disable PASV mode
pasv_enable=NO

[root@www ~]# systemctl restart vsftpd

[root@www ~]# firewall-cmd --add-service=ftp --permanent 
success

[root@www ~]# firewall-cmd --reload 
success
#----------------------------------------------------------------------------------------
setsebool -P ftpd_full_access on """