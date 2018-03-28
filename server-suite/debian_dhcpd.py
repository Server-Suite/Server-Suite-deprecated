from PyQt4 import QtCore
from PyQt4 import QtGui as qt
import sys,os,saunet
class dhcp(qt.QWidget):
    def save_n_apply(self,start_dhcp,restart_dhcp,status_dhcp,enabel_dhcp,ok_key,apply_change):
        print "saved changes"
        start_dhcp.setHidden(False)
        status_dhcp.setHidden(False)
        restart_dhcp.setHidden(False)
        enabel_dhcp.setHidden(False)
        apply_change.setHidden(True)
        ok_key.setHidden(False)
    def msg(self,frame):
        status=str(saunet.status("isc-dhcp-server"))
        if status=="active":
            qt.QMessageBox.information(frame, "status",status)
        elif status=="inactive":
            qt.QMessageBox.critical(frame, "status",status)
    def dhcp_service(self,service):
        if service=="start":
            print "started service"
            #os.system("systemctl start isc-dhcp-server")
        elif service=="restart":
            print "restarted service"
            #os.system("systemctl restart isc-dhcp-server")
        elif service=="enabel":
            print "enabeled service"
            #os.system("systemctl enabel isc-dhcp-server")
    def install(self,dhcp_status,install_dhcp):
        status=os.system("apt-get -y install isc-dhcp-server")
        if status==0:
            dhcp_status.setText("<b><font color='green'>Succesfully installed</font>")
            install_dhcp.setHidden(True)
            return True
        else:
            False
    def check_dhcp(self):
        status=str(os.popen("apt list isc-dhcp-server").read())
        os.system("clear")
        if "installed" in status:
            return True
        else:
            return False
    def __init__(self,parent=None):
        qt.QWidget.__init__(self,parent=None)
        #w=qt.QApplication(sys.argv)
        #frame=qt.QWidget()
        self.setWindowTitle("DHCP")
        self.setWindowIcon(qt.QIcon("images/logo.svg"))
        back=qt.QLabel("<img src='images/dhcp.jpg' height='500' width='500'>",self)
        #------------------------------------------------------------------------------
        if True:#self.check_dhcp():
            dhcp_status=qt.QLabel("<b><font color='green'>DHCP is installed</font>",self)
        else:
            dhcp_status=qt.QLabel("<b><font color='red'>DHCP is not installed</font>",self)
            install_dhcp=qt.QPushButton("Install",self)
            install_dhcp.clicked.connect(lambda:self.install(dhcp_status,install_dhcp))
            install_dhcp.move(370,45)        
        get_domain_lbl=qt.QLabel("<b><font color='black'>Enter domain name:",self)
        get_domain=qt.QLineEdit(self)
        get_domain.setText(saunet.hostname()[1])
        value=saunet.ip()
        get_ip_lbl=qt.QLabel("<b><font color='black'>Enter ip address:</font></b>",self)
        get_ip=qt.QLineEdit(self)
        get_ip.setText(value[0])

        get_subnet_lbl=qt.QLabel("<b><font color='black'>Enter subnet:",self)
        get_subnet=qt.QLineEdit(self)
        #get_ip.setText(server_name)

        get_netmask_lbl=qt.QLabel("<b><font color='black'>Enter netmask:",self)
        get_netmask=qt.QLineEdit(self)
        get_netmask.setText(value[1])

        get_gateway_lbl=qt.QLabel("<b><font color='black'>Enter getway:",self)
        get_gateway=qt.QLineEdit(self)
        get_gateway.setText(saunet.gateway())

        get_ip_range_lbl=qt.QLabel("<b><font color='black'>Enter IP range from:",self)
        get_ip_range=qt.QLineEdit(self)
        get_range_to_lbl=qt.QLabel("<b><font color='black'>to",self)
        get_range_to=qt.QLineEdit(self)

        start_dhcp=qt.QPushButton("Start",self)
        start_dhcp.clicked.connect(lambda:self.dhcp_service("start"))
        start_dhcp.setHidden(True)

        status_dhcp=qt.QPushButton("status",self)
        status_dhcp.clicked.connect(lambda:self.msg(self))
        status_dhcp.setHidden(True)

        restart_dhcp=qt.QPushButton("Restart",self)
        restart_dhcp.clicked.connect(lambda:self.dhcp_service("restart"))
        restart_dhcp.setHidden(True)

        enabel_dhcp=qt.QPushButton("Enabel",self)
        enabel_dhcp.clicked.connect(lambda:self.dhcp_service("enabel"))
        enabel_dhcp.setHidden(True)

        apply_change=qt.QPushButton("apply",self)
        apply_change.clicked.connect(lambda:self.save_n_apply(start_dhcp,restart_dhcp,status_dhcp,enabel_dhcp,ok_key,apply_change))

        ok_key=qt.QPushButton("OK",self)
        ok_key.clicked.connect(lambda:self.close())
        ok_key.setHidden(True)

        cancle=qt.QPushButton("Cancel",self)
        cancle.clicked.connect(lambda:self.close())
        #------------------------------------------------------------------------------
        dhcp_status.move(200,50)
        dhcp_status.setFixedSize(150,30)

        get_domain_lbl.move(50,100)
        get_domain.move(200,95)
        get_domain.setFixedSize(200,25)

        get_ip_lbl.move(50,150)
        get_ip.move(200,145)
        get_ip.setFixedSize(200,25)

        get_subnet_lbl.move(50,200)
        get_subnet.move(200,195)
        get_subnet.setFixedSize(200,25)

        get_netmask_lbl.move(50,250)
        get_netmask.move(200,245)
        get_netmask.setFixedSize(200,25)

        get_gateway_lbl.move(50,300)
        get_gateway.move(200,295)
        get_gateway.setFixedSize(200,25)

        get_ip_range_lbl.move(20,350)
        get_ip_range.move(160,345)
        get_range_to_lbl.move(300,350)
        get_range_to.move(325,345)

        restart_dhcp.move(150,400)

        start_dhcp.move(50,400)

        enabel_dhcp.move(250,400)

        status_dhcp.move(350,400)

        apply_change.move(400,450)
        ok_key.move(400,450)
        cancle.move(300,450)
        screen = qt.QDesktopWidget().screenGeometry()
        ht=(screen.height()-500)/2
        wd=(screen.width()-500)/2
        self.setGeometry(wd,ht,500,500)
        self.setFixedSize(500,500)
        #self.show()
        #w.exec_()
"""
root@dlp:~# aptitude -y install isc-dhcp-server
root@dlp:~# vi /etc/dhcp/dhcpd.conf
# line 13: specify domain name
option domain-name "srv.world";
# line 14: specify nameserver's hostname or IP address
option domain-name-servers dlp.srv.world;
# line 21: uncomment
authoritative;
# add follows to the end
# specify network address and subnet-mask
subnet 10.0.0.0 netmask 255.255.255.0 {
     # specify default gateway
     option routers 10.0.0.1;
     # specify subnet-mask
     option subnet-mask 255.255.255.0;
     # specify the range of leased IP address
     range dynamic-bootp 10.0.0.200 10.0.0.254;
}
root@dlp:~# systemctl restart isc-dhcp-server 
"""