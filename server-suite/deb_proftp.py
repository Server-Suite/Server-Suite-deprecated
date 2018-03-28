from PyQt4 import QtCore
from PyQt4 import QtGui as qt
import sys,os,saunet
class deb_proftp(qt.QWidget):
	def save_n_apply(self):
		print "saved changes"
		print str(self.flag_ipv6)+"\n"+self.get_domain.text()+"\n"+self.get_rootD.text()+"\n"+self.get_user.text()
		self.start_proftpd.setHidden(False)
		self.status_proftpd.setHidden(False)
		self.restart_proftpd.setHidden(False)
		self.enabel_proftpd.setHidden(False)
		#self.apply_change.setHidden(True)
		#self.ok_key.setHidden(False)
	def msg(self,frame):
		status=str(saunet.status("proftpd"))
		if status=="active":
			qt.QMessageBox.information(frame, "status",status)
		elif status=="inactive":
			qt.QMessageBox.critical(frame, "status",status)
	def proftp_service(self,service):
		if service=="start":
			print "started service"
			#os.system("systemctl start isc-dhcp-server")
		elif service=="restart":
			print "restarted service"
			#os.system("systemctl restart isc-dhcp-server")
		elif service=="enabel":
			print "enabeled service"
			#os.system("systemctl enabel isc-dhcp-server")
	def ipv6(self):
		if self.cbox_ipv6.isChecked()==True:
			self.flag_ipv6=True
			print self.flag_ipv6
		elif self.cbox_ipv6.isChecked()==False:
			self.flag_ipv6=False
			print self.flag_ipv6
	def check_proftp(self):
		status=str(os.popen("apt list proftpd-*").read())
		os.system("clear")
		if "installed" in status:
			return True
		else:
			return False
	def install(self):
		status=os.system("apt-get -y install proftpd")
		status=0
		if status==0:
			self.proftpd_status.setText("<b><font color='green'>Succesfully installed</font>")
			self.install_proftpd.setHidden(True)
			return True
		else:
			False
	def __init__(self,parent=None):
		qt.QWidget.__init__(self,parent=None)
		self.setWindowIcon(qt.QIcon("images/logo128x128.png"))
		self.setWindowTitle("Proftp")
		self.flag_ipv6=False
		back=qt.QLabel("<img src='images/ftp-back.jpg' height='500' width='500'>",self)
		#------------------------------------------------------------------------------
		if self.check_proftp():
			self.proftpd_status=qt.QLabel("<b><font color='green'>PROftp is installed</font>",self)
			self.proftpd_status.move(200,50)
		else:
			self.proftpd_status=qt.QLabel("<b><font color='red'>PROftp is not installed</font>",self)
			self.proftpd_status.move(200,50)
			self.install_proftpd=qt.QPushButton("Install",self)
			self.install_proftpd.clicked.connect(lambda:self.install())
			self.install_proftpd.move(370,45)
		self.cbox_ipv6=qt.QCheckBox("IPV6",self)
		self.cbox_ipv6.stateChanged.connect(lambda:self.ipv6())
		self.cbox_ipv6.move(50,100)
		self.get_domain_lbl=qt.QLabel("<b><font color='black'>Enter domain name:",self)
		self.get_domain=qt.QLineEdit(self)
		self.get_domain.setText("www."+saunet.hostname()[1])
		self.get_domain_lbl.move(50,130)
		self.get_domain.move(200,125)
		self.get_domain.setFixedSize(200,25)
		self.get_rootD_lbl=qt.QLabel("<b><font color='black'>Enter root Directory:",self)
		self.get_rootD=qt.QLineEdit(self)
		self.get_rootD.setText("/root/")
		self.get_rootD_lbl.move(50,160)
		self.get_rootD.move(200,155)
		self.get_rootD.setFixedSize(200,25)
		self.get_user_lbl=qt.QLabel("<b><font color='black'>Enter user name:",self)
		self.get_user=qt.QLineEdit(self)
		self.get_user.setText("root")
		self.get_user_lbl.move(50,190)
		self.get_user.move(200,185)
		self.get_user.setFixedSize(200,25)

		self.start_proftpd=qt.QPushButton("Start",self)
		self.start_proftpd.clicked.connect(lambda:self.proftp_service("start"))
		self.start_proftpd.setHidden(True)

		self.status_proftpd=qt.QPushButton("status",self)
		self.status_proftpd.clicked.connect(lambda:self.msg(self))
		self.status_proftpd.setHidden(True)

		self.restart_proftpd=qt.QPushButton("Restart",self)
		self.restart_proftpd.clicked.connect(lambda:self.proftp_service("restart"))
		self.restart_proftpd.setHidden(True)

		self.enabel_proftpd=qt.QPushButton("Enabel",self)
		self.enabel_proftpd.clicked.connect(lambda:self.proftp_service("enabel"))
		self.enabel_proftpd.setHidden(True)

		self.apply_change=qt.QPushButton("apply",self)
		self.apply_change.clicked.connect(lambda:self.save_n_apply())

		#self.ok_key=qt.QPushButton("OK",self)
		#self.ok_key.clicked.connect(lambda:self.close())
		#self.ok_key.setHidden(True)

		self.cancle=qt.QPushButton("Cancel",self)
		self.cancle.clicked.connect(lambda:self.close())

		self.restart_proftpd.move(150,400)

		self.start_proftpd.move(50,400)

		self.enabel_proftpd.move(250,400)

		self.status_proftpd.move(350,400)

		self.apply_change.move(400,450)
		#self.ok_key.move(400,450)
		self.cancle.move(300,450)
		screen = qt.QDesktopWidget().screenGeometry()
		ht=(screen.height()-500)/2
		wd=(screen.width()-500)/2
		self.setGeometry(wd,ht,500,500)
		self.setFixedSize(500,500)
"""app = qt.QApplication(sys.argv)
main_window = deb_proftp()
main_window.show()
sys.exit(app.exec_())"""