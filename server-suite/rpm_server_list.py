from PyQt4 import QtCore
from PyQt4 import QtGui as qt
import os,sys,platform
class rpm_server_list(qt.QWidget):
    def __init__(self,parent=None):
        self.work()
    def work(self):
        qt.QWidget.__init__(self,parent=None)
#        self=qt.QWidget()
        f=open(".os_name.txt","r")
        temp=f.read()
        if temp.lower()=="centos":
            label=qt.QLabel("< img src='images/centos-back.jpg' height='500' width='500'>",self)
        elif temp.lower()=="fedora":
            label=qt.QLabel("< img src='images/fedora-back.jpg' height='500' width='500'>",self)
        elif temp.lower()=="redhat":
            label=qt.QLabel("< img src='images/redhat.jpg' height='500' width='500'>",self)
        else:
            label=qt.QLabel("< img src='images/default.jpg' height='500' width='500'>",self)
        dns_btn=qt.QPushButton("DNS Server",self)
        dns_btn.setFixedWidth(210)
        #dns_btn.setStyleSheet("background-color:white")
        dhcp_btn=qt.QPushButton("DHCP Server",self)
        dhcp_btn.setFixedWidth(210)
        storage_btn=qt.QPushButton("Storage Server",self)
        storage_btn.setFixedWidth(210)
        vertual_btn=qt.QPushButton("Virtualization",self)
        vertual_btn.setFixedWidth(210)
        directory_btn=qt.QPushButton("Directory Server",self)
        directory_btn.setFixedWidth(210)
        web_btn=qt.QPushButton("WEB Server",self)
        web_btn.setFixedWidth(210)
        ftp_btn=qt.QPushButton("FTP Server",self)
        ftp_btn.setFixedWidth(210)
        #label.move()
        dns_btn.clicked.connect(lambda:self.msg())
        dhcp_btn.clicked.connect(lambda:self.msg())
        storage_btn.clicked.connect(lambda:self.msg())
        vertual_btn.clicked.connect(lambda:self.msg())
        directory_btn.clicked.connect(lambda:self.msg())
        web_btn.clicked.connect(lambda:self.msg())
        ftp_btn.clicked.connect(lambda:self.msg())
        dns_btn.move(145,10)
        dhcp_btn.move(145,60)
        storage_btn.move(145,110)
        vertual_btn.move(145,160)
        directory_btn.move(145,210)
        web_btn.move(145,260)
        ftp_btn.move(145,310)
        self.setFixedSize(500,500)
        self.setWindowTitle("RPM Packaging system")
        self.setWindowIcon(qt.QIcon("images/logo128x128.png"))
        screen = qt.QDesktopWidget().screenGeometry()
        ht=(screen.height()-500)/2
        wd=(screen.width()-500)/2
        self.setGeometry(wd,ht,500,500)
    def msg(self):
        qt.QMessageBox.information(self,"Sorry!", "This feature will be available in next update")