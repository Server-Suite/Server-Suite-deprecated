from PyQt4 import QtCore
from PyQt4 import QtGui as qt
import sys,os,socket,thread,pass_sau
class login():
	def get(self,user,s):
		self.frame.textbox.setText("")
		if pass_sau.check_enc_pass(user,s):
			#self.frame.hide()
			self.frame.close()
			self.frame.lbl1.setHidden(True)
			os.system("python serv.py")
			#self.frame.show()
		else:
			self.frame.lbl1.setHidden(False)
	def set(self,user,s):
		self.frame.textbox.setText("")
		pass_sau.set_enc_pass(str(user),str(s))
		self.frame.btn2.setHidden(True)
		self.frame.btn.setHidden(False)
		self.frame.textbox.returnPressed.connect(lambda:self.get(self.frame.l.text(),self.frame.textbox.text()))
	def work(self):
		self.data1=""
		#qt.QWidget.__init__(self,parent=None)
		w=qt.QApplication(sys.argv)
		self.frame=qt.QWidget()
		self.frame.setAutoFillBackground(True)
		self.frame.setAttribute(QtCore.Qt.WA_TranslucentBackground, 10)
		flag=(os.path.exists("passwd") and os.path.exists("passwd"))
		#self.frame.lb=qt.QLabel("<img src=images/trans-1.png height='300' width='300'>",self.frame)
		self.frame.lbl=qt.QLabel("<img src=images/logo-white.png height='100' width='100'>",self.frame)
		self.frame.lbl1=qt.QLabel("<font color='red'>Wrong username or password</font>",self.frame)
		self.frame.lbl1.setHidden(True)
		self.frame.lbl.move(100,30)
		self.frame.lbl1.move(60,130)
		self.frame.setWindowIcon(qt.QIcon("images/logo128x128.png"))
		self.frame.setWindowTitle("Login")
		self.frame.l=qt.QLineEdit(self.frame)
		self.frame.textbox = qt.QLineEdit(self.frame)
		self.frame.textbox.setEchoMode(qt.QLineEdit.Password)
		self.frame.l.move(50,150)
		self.frame.l.setFixedSize(200,30)
		self.frame.btn=qt.QPushButton("Login",self.frame)
		self.frame.btn2=qt.QPushButton("Sign up",self.frame)
		if flag:
			self.frame.btn2.setHidden(True)
			self.frame.textbox.returnPressed.connect(lambda:self.get(self.frame.l.text(),self.frame.textbox.text()))
		else:
			self.frame.btn.setHidden(True)
		self.frame.btn.move(100,250)
		self.frame.btn2.move(100,250)
		self.frame.btn.clicked.connect(lambda:self.get(self.frame.l.text(),self.frame.textbox.text()))
		self.frame.btn2.clicked.connect(lambda:self.set(self.frame.l.text(),self.frame.textbox.text()))
		self.frame.textbox.move(50,200)
		self.frame.textbox.setFixedSize(200,30)
		screen = qt.QDesktopWidget().screenGeometry()
		ht=(screen.height()-300)/2
		wd=(screen.width()-300)/2
		self.frame.setGeometry(wd,ht,300,300)
		#self.frame.setFixedSize(300,300)
		self.frame.show()
		w.exec_()
	def __init__(self):
		self.work()
	def __del__(self):
		self.s.close()
		print "destructor called"
o=login()
