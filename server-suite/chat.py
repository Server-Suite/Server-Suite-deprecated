from PyQt4 import QtCore
from PyQt4 import QtGui as qt
import sys,os,socket,thread
class about():
	cnt=0
	def quit_prg(self):
		self.s.send("quit")
	def set(self,data):
		self.cnt+=1
		self.data1=data+"\n"
		self.frame.l.insertPlainText(self.data1)
		#self.s.send(data)
		self.frame.textbox.setText("")
		self.frame.l.verticalScrollBar().setSliderPosition(self.cnt)
	def recv_data(self,s):
		while True:
			data=self.s.recv(2048)
			if data=="quit":
				break
			else:
				self.set(data)

	def work(self):
		self.data1=""
		#qt.QWidget.__init__(self,parent=None)
		w=qt.QApplication(sys.argv)
		self.frame=qt.QWidget()
		self.frame.setWindowIcon(qt.QIcon("images/logo128x128.png"))
		self.frame.setWindowTitle("chat-app")
		self.frame.textbox = qt.QLineEdit(self.frame)
		self.frame.l=qt.QPlainTextEdit(self.frame)
		self.frame.l.setReadOnly(True)
		self.frame.l.move(20,20)
		self.frame.l.setFixedSize(450,400)
		self.frame.btn=qt.QPushButton("Quit",self.frame)
		self.frame.btn.clicked.connect(lambda:self.quit_prg())
		self.frame.textbox.returnPressed.connect(lambda:self.set(self.frame.textbox.text()))
		self.frame.l.verticalScrollBar().setValue(0)
		self.frame.textbox.move(20, 450)
		self.frame.textbox.setFixedSize(450,20)
		screen = qt.QDesktopWidget().screenGeometry()
		ht=(screen.height()-500)/2
		wd=(screen.width()-500)/2
		self.frame.setGeometry(wd,ht,500,500)
		self.frame.setFixedSize(500,500)
		self.frame.show()
		w.exec_()
	def __init__(self):
		#thread.start_new_thread(self.work,())
		#self.s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		#self.s.connect(("172.16.8.6",1234))
		#if self.s:
			#thread.start_new_thread(self.recv_data,(self.s,))
		self.work()	
	def __del__(self):
		self.s.close()
		print "destructor called"

o=about()