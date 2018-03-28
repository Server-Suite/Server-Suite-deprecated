from PyQt4 import QtCore
from PyQt4 import QtGui as qt
import os,sys,platform,debian_dhcpd,deb_ftp_menu
class deb_server_list(qt.QWidget):
    def __init__(self,parent=None):
        self.work()
    def work(self):
        qt.QWidget.__init__(self,parent=None)
#        self=qt.QWidget()
        #temp=platform.linux_distribution()
        f=open(".os_name.txt","r")
        temp=f.read()
        if temp.lower()=="kali":
            label=qt.QLabel("< img src='images/kali-linux.jpg' height='500' width='500'>",self)
        elif temp.lower()=="ubuntu":
            label=qt.QLabel("< img src='images/ubuntu-back-2.jpg' height='500' width='500'>",self)
        elif temp.lower()=="debian":
            label=qt.QLabel("< img src='images/debian-back.jpg' height='500' width='500'>",self)
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
        dhcp_btn.clicked.connect(lambda:self.start_prg("debian_dhcpd"))
        storage_btn.clicked.connect(lambda:self.msg())
        vertual_btn.clicked.connect(lambda:self.msg())
        directory_btn.clicked.connect(lambda:self.msg())
        web_btn.clicked.connect(lambda:self.msg())
        ftp_btn.clicked.connect(lambda:self.start_prg("ftp"))
        dns_btn.move(145,10)
        dhcp_btn.move(145,60)
        storage_btn.move(145,110)
        vertual_btn.move(145,160)
        directory_btn.move(145,210)
        web_btn.move(145,260)
        ftp_btn.move(145,310)
        self.setFixedSize(500,500)
        self.setWindowTitle("DEB Packaging system")
        self.setWindowIcon(qt.QIcon("images/logo128x128.png"))
        screen = qt.QDesktopWidget().screenGeometry()
        ht=(screen.height()-500)/2
        wd=(screen.width()-500)/2
        self.setGeometry(wd,ht,500,500)
    def msg(self):
        qt.QMessageBox.information(self,"Sorry!", "This feature will be available in next update")
    def start_prg(self,name):
        #deb_server_list.close()
        #os.system("python "+name+".py")
        if name=="debian_dhcpd":
            self.o=debian_dhcpd.dhcp()
            self.o.show()
        elif name=="ftp":
            self.o=deb_ftp_menu.deb_ftp_menu()
            self.o.show()