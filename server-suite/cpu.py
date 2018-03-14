import os,sys,psutil,time,thread
from PyQt4 import QtGui as qt
class cpu:
	def get_net_speed(self,frame,net_speed,cpu_use,cpu_cicle):
	    initial_down = psutil.net_io_counters().bytes_recv
	    initial_up = psutil.net_io_counters().bytes_sent
	    while True:
	        now_down = psutil.net_io_counters().bytes_recv
	        now_up = psutil.net_io_counters().bytes_sent
	        download_speed = (now_down - initial_down)/1000
	        upload_speed = (now_up - initial_up)/1000
	        s=(str(download_speed)+"KB/s\t\t-\t "+str(upload_speed)+"KB/s")
	        net_speed.setText(s)
	        initial_down = now_down
	        initial_up = now_up
	        time.sleep(1)
	        cpu_all_detail=os.popen("mpstat").read()
	        cpu_cicle.setText(str(cpu_all_detail))
	        cpu=psutil.cpu_percent()
	        cpu="CPU Usage in % : ("+str(cpu)+") %"
	        cpu_use.setText(cpu)
	def __init__(self):
		w=qt.QApplication(sys.argv)
		frame=qt.QWidget()
		label1=qt.QLabel("< img src='images/back-8.jpg' height='442' width='590'>",frame)
		div_1=qt.QLabel("=================================================================================",frame)
		net_speed=qt.QLabel("NET",frame)
		div_2=qt.QLabel("=================================================================================",frame)
		cpu_use=qt.QLabel("CPU",frame)
		div_3=qt.QLabel("=================================================================================",frame)
		cpu_cicle=qt.QLabel("CPU cicles",frame)
		div_4=qt.QLabel("=================================================================================",frame)
		thread.start_new_thread(self.get_net_speed,(frame,net_speed,cpu_use,cpu_cicle))
		#thread.start_new_thread(self.cpu_usage_perc,(frame,cpu_use))
		net_speed.move(20,20)
		div_2.move(0,30)
		cpu_cicle.move(0,55)
		div_3.move(0,75)
		cpu_use.move(200,100)
		cpu_use.setFixedSize(200,100)
		cpu_cicle.setFixedSize(600,100)
		frame.setGeometry(100,100,500,500)
		frame.setFixedSize(590,442)
		frame.show()
		w.exec_()
c=cpu()
