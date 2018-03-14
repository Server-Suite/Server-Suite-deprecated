from PyQt4 import QtGui as qt
import time,os,sys,thread
import psutil


def get_net_speed():
    initial_down = psutil.net_io_counters().bytes_recv
    initial_up = psutil.net_io_counters().bytes_sent
    while True:
        now_down = psutil.net_io_counters().bytes_recv
        now_up = psutil.net_io_counters().bytes_sent
        download_speed = (now_down - initial_down)/1000
        upload_speed = (now_up - initial_up)/1000
        s=(str(download_speed)+"KB/s\t\t-\t "+str(upload_speed)+"KB/s")
        l.setText(s)
        initial_down = now_down
        initial_up = now_up
        time.sleep(1)


if __name__ == '__main__':
    w=qt.QApplication(sys.argv)
    frame=qt.QWidget()
    frame.setGeometry(100,100,250,80)
    frame.setWindowTitle("Net_Speed")
    download=qt.QLabel("<font color='green'>download</font>",frame)
    upload_=qt.QLabel("<font color='red'>upload</font>",frame)
    l=qt.QLabel("<font color='red'>speed</font>",frame)
    download.move(20,0)
    upload_.move(170,0)
    l.move(20,0)
    l.setFixedSize(250,100)
    thread.start_new_thread(get_net_speed,())
    frame.show()
    w.exec_()
