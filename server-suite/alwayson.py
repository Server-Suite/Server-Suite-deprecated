COMPLETED_STYLE = """
QProgressBar{
    border: 1px solid grey;
    border-radius: 9px;
    text-align: center
}

QProgressBar::chunk {
    background-color: aqua;
    width: 5px;
    margin: 1px;
}
"""
from PyQt4 import QtCore
from PyQt4 import QtGui as qt
import sys,os,psutil,thread
class on(qt.QWidget):
	def show_status(self):
		try:
			self.o_s=server_status()
			self.o_s.show()
		except:
			pass
		#self.obj=cpu_status()
		#self.obj.show()
	def close_window(self):
		self.close()
		try:
			self.o_s.flag=False
		except:
			pass
		os.system("rm alwayson.lock")
	def work(self):
		qt.QWidget.__init__(self,parent=None)
		glow=qt.QLabel("<img src='images/glow.png' height='150' width='150'>",self)
		label_title=qt.QLabel("<img src='logo128x128.png' height='50' width='50'>",self)
		self.setWindowIcon(qt.QIcon("images/logo128x128.png"))
		self.setWindowTitle("Server-Suite")
		self.btn = qt.QPushButton(self)
		self.btn.setIcon(qt.QIcon(qt.QPixmap("images/black_cross.png")))
		self.btn.move(100,20)
		self.btn.setFixedSize(50,50)
		self.btn.setStyleSheet("background-color:transparent;border:0;")
		self.btn.clicked.connect(lambda:self.close_window())
		self.status=qt.QPushButton(self)
		print "touch lock"
		#self.status.setIcon(qt.QIcon(qt.QPixmap("images/black_cross.png")))
		self.status.move(50,50)
		self.status.setFixedSize(50,50)
		self.status.setStyleSheet("background-color:transparent;border:0;")
		self.status.clicked.connect(lambda:self.show_status())
		label_title.move(50,50)
		x=160
		y=150
		screen = qt.QDesktopWidget().screenGeometry()
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
		self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint)
		ht=(screen.height()-100)
		wd=(screen.width()-100)
		self.setGeometry(wd,ht,x,y)
		self.setFixedSize(x,y)
	def __init__(self,parent=None):
		if os.path.isfile("alwayson.lock")==False:
			os.system("touch alwayson.lock")
			self.work()
		else:
			print "alwaays on is locked"
class server_status(qt.QWidget):
	def cpu_cycle(self):
		while self.flag:
			value=self.o.get_cpu_percent()
			self.cpu_per_lbl.setText("<font color='black'>CPU:</font><font color='red'>"+value+" %</font>")
			print value
	def __init__(self,parent=None):
		qt.QWidget.__init__(self,parent=None)
		self.flag=True
		self.msg_back=qt.QLabel("<img src='images/msg.png' height='300' width='300'>",self)
		self.setWindowIcon(qt.QIcon("images/logo128x128.png"))
		self.setWindowTitle("Server-Suite About")
		self.o=cpu()
		self.cpu_per_lbl=qt.QLabel("<font color='black'>CPU:</font><font color='red'>"+str(psutil.cpu_percent())+" %</font>",self)
		self.mem_per_lbl=qt.QLabel(self)
		self.temp_per_lbl=qt.QLabel(self)
		self.battery_lbl=qt.QLabel(self)
		mem=self.o.get_ram()
		temp=psutil.sensors_temperatures()
		temp=str(temp["coretemp"]).split("=")[2].split(",")[0]
		batry=self.o.get_battery()
		self.mem_per_lbl.setText("<font color='black'>Memory:</font><font color='red'>"+str(mem)+" %</font>")
		self.temp_per_lbl.setText("<font color='black'>CPU Temperature:</font><font color='red'>"+str(temp)+"\xb0</font>")
		self.battery_lbl.setText("<font color='black'>Battery:</font><font color='red'>"+batry+" %</font>")
		self.cpu_per_lbl.move(50,30)
		self.cpu_per_lbl.setFixedSize(100,20)
		self.mem_per_lbl.move(50,50)
		self.mem_per_lbl.setFixedSize(100,20)
		self.temp_per_lbl.move(50,70)
		self.temp_per_lbl.setFixedSize(200,20)
		self.battery_lbl.move(50,90)
		self.battery_lbl.setFixedSize(200,20)
		thread.start_new_thread(self.cpu_cycle,())
		screen = qt.QDesktopWidget().screenGeometry()
		self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
		self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint | QtCore.Qt.Popup)
		x=300
		y=300
		"""try:
			self.obj=cpu_status()
			self.obj.show()
		except:
			pass"""
		ht=(screen.height()-350)
		wd=(screen.width()-400)
		self.setGeometry(wd,ht,x,y)
		self.setFixedSize(x,y)
class cpu_status(qt.QWidget):
	def core_progress(self):
		self.ob=cpu()
		print str(self.ob.get_cpu_core())
		try:
			while True:
				core=self.ob.get_cpu_core()
				print core
				self.progress.setValue(core[0]*1)
				self.progress1.setValue(core[1]*1)
				self.progress2.setValue(core[2]*1)
				self.progress3.setValue(core[3]*1)
		except:
			pass	
	def __init__(self,parent=None):
		qt.QWidget.__init__(self,parent=None)
		self.setWindowIcon(qt.QIcon("images/logo128x128.png"))
		self.setWindowTitle("Server-Suite About")
		self.msg_back=qt.QLabel("<img src='images/cpu.png' height='400' width='400'>",self)
		screen = qt.QDesktopWidget().screenGeometry()
		self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
		self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint | QtCore.Qt.Popup)
		self.progress = qt.QProgressBar(self)
		self.progress.setGeometry(110, 120, 180, 20)
		self.progress.setMaximum(0)
		self.progress.setMaximum(100)
		self.progress.setStyleSheet(COMPLETED_STYLE)
		self.progress1 = qt.QProgressBar(self)
		self.progress1.setGeometry(110, 150, 180, 20)
		self.progress1.setMaximum(0)
		self.progress1.setMaximum(100)
		self.progress1.setStyleSheet(COMPLETED_STYLE)
		self.progress2 = qt.QProgressBar(self)
		self.progress2.setGeometry(110, 180, 180, 20)
		self.progress2.setMaximum(0)
		self.progress2.setMaximum(100)
		self.progress2.setStyleSheet(COMPLETED_STYLE)
		self.progress3 = qt.QProgressBar(self)
		self.progress3.setGeometry(110, 210, 180, 20)
		self.progress3.setMaximum(0)
		self.progress3.setMaximum(100)
		self.progress3.setStyleSheet(COMPLETED_STYLE)
		thread.start_new_thread(self.core_progress,())
		#self.progress.setOrientation(QtCore.Qt.Vertical)
		x=400
		y=400
		ht=(screen.height()-650)
		wd=(screen.width()-900)
		self.setGeometry(wd,ht,x,y)
		self.setFixedSize(x,y)
class cpu():
	def get_cpu_percent(self):
		value=str(psutil.cpu_percent(interval=2))
		return value
	def get_ram(self):
		mem =str(psutil.virtual_memory()).split("=")[3].split(",")[0]
		return mem
	def get_cpu_core(self):
		try:
			s=psutil.cpu_percent(interval=2,percpu=True)
			return s
		except:
			pass
	def get_battery(self):
		status=os.popen("cat /sys/class/power_supply/BAT0/uevent").read().split("POWER_SUPPLY_CAPACITY=")[1].split("\n")[0]
		if int(status)>=100:
			return "100"
		else:
			return status
"""
app = qt.QApplication(sys.argv)
main_window = cpu_status()
main_window.show()
sys.exit(app.exec_())"""