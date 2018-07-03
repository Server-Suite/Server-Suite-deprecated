from init import Ui_MainWindow
import os,sys,random,_thread,psutil,time
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal
from subprocess import Popen, PIPE, STDOUT
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar

class PingThread(QThread):
    signal = pyqtSignal('PyQt_PyObject')

    def __init__(self):
        QThread.__init__(self)
        self.ip="127.0.0.1"
    def run(self,command="ping -c 1 "):#apt-get install -y apache2
        process = Popen(command+self.ip, stdout=PIPE, shell=True)
        while True:
            line = process.stdout.readline().rstrip()
            if not line:
                break
            #yield line
            self.signal.emit(str(line)[1:])


class server_suite(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(server_suite, self).__init__(parent)
        self.setupUi(self)
        self.demons_state()
        conn = sqlite3.connect('.view_data.db')
        data=conn.execute("select * from dock")
        self.name=[]
        self.value=[]
        self.flag=True
        self.new=0
        self.load_docks(data)
        self.pushButton.setText(self.get_os())
        self.pushButton.clicked.connect(lambda:self.go_for_server())
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.canvas1=self.canvas
        #f, axarr = plt.subplots(2, sharex=True)
        self.s1=[]
        for j in range(58):
	        self.s1.append(0)
        #animation.FuncAnimation(f,self.plot, interval = 500)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.verticalLayout_5.addWidget(self.canvas)
        self.process  = QtCore.QProcess(self)
        _thread.start_new_thread(self.plot,())
        self.lineEdit.setHidden(True)
        self.lineEdit.returnPressed.connect(lambda:self.advance_line_enter())
        self.comboBox.setHidden(True)
        self.comboBox.currentIndexChanged.connect(lambda:self.change_os())
        self.pushButton_2.setHidden(True)
        self.comboBox_2.setHidden(True)
        self.textBrowser_2.setHidden(True)
        self.checkBox.stateChanged.connect(lambda:self.choose_os())
        self.checkBox_2.stateChanged.connect(lambda:self.show_advance())
        self.textBrowser_3.setTextColor(QtGui.QColor("green"))
        self.df_Th()
        _thread.start_new_thread(self.get_net_speed,())
        #self.dockWidget_4.setHidden(True)
        #-------------------menubar-------------------------------------------------------
        self.actionServer_list.triggered.connect(lambda:self.server_list_checkbox())
        self.actionCPU_Usage.triggered.connect(lambda:self.cpu_usage_checkbox())
        self.actionMounted_Volumes.triggered.connect(lambda:self.dockWidget_2.show())
        self.actionCPU_Usage_2.triggered.connect(lambda:self.dockWidget_3.show())
        self.actionServer_list_2.triggered.connect(lambda:self.dockWidget.show())
        self.actionAbout_Server_Suite.triggered.connect(lambda:self.show_about())
        self.actionHide_Menu_Bar.triggered.connect(lambda:self.hide_menubar())
        #---------------------------------------------------------------------------------------------------------------
    def go_for_server(self):
        if "debian" in self.pushButton.text():
            _thread.start_new_thread(os.system,("sudo python3 debian_script.py",))
    def show_dialog(self):
        import dialog
        Dialog = QtWidgets.QDialog()
        o=dialog.Ui_Dialog()
        o.show()
    def hide_menubar(self):
        if self.flag:
            self.menuBar.setHidden(True)
            self.flag=False
        else:
            self.menuBar.setHidden(False)
            self.flag=True
    def show_about(self):
        import about
        form=about.Ui_MainWindow()
        form.show()
    def get_net_speed(self):
        initial_down = psutil.net_io_counters().bytes_recv
        initial_up = psutil.net_io_counters().bytes_sent
        while True:
            now_down = psutil.net_io_counters().bytes_recv
            now_up = psutil.net_io_counters().bytes_sent
            download_speed = (now_down - initial_down)/1000
            upload_speed = (now_up - initial_up)/1000
            self.lcdNumber_3.display(self.new)
            self.lcdNumber_4.display(str(psutil.virtual_memory().percent))
            self.lcdNumber.display(upload_speed)
            self.lcdNumber_2.display(download_speed)
            initial_down = now_down
            initial_up = now_up
            time.sleep(1)
    def df_Th(self):
        self.textBrowser_3.setText("")
        status=os.popen("df -Th",mode='r').read()
        for line in status.split("\n"):
            self.textBrowser_3.append(line)
    def server_list_checkbox(self):
        if self.actionServer_list.isChecked():
            self.dockWidget.show()
        else:
            self.dockWidget.close()
    def cpu_usage_checkbox(self):
        if self.actionCPU_Usage.isChecked():
            self.dockWidget_3.show()
        else:
            self.dockWidget_3.close()
    def load_docks(self,data):
        for ui_data in data:
            self.name.append(ui_data[0])
            self.value.append(ui_data[1])
        if self.value[0]==0:
            self.dockWidget.setHidden(True)
            self.actionServer_list.setChecked(False)
        else:
            self.dockWidget.setHidden(False)
            self.actionServer_list.setChecked(True)
        if self.value[1]==0:
            self.dockWidget_3.setHidden(True)
            self.actionCPU_Usage.setChecked(False)
        else:
            self.dockWidget_3.setHidden(False)
            self.actionCPU_Usage.setChecked(True)
        if self.value[2]==0:
            self.dockWidget.setHidden(True)
        else:
            self.dockWidget.setHidden(False)
    def change_os(self):
        self.pushButton.setText((self.comboBox.currentText()).lower())
    def advance_line_enter(self):
        if self.comboBox_2.currentText() == "ping":
            self.textBrowser_2.setText("")
            status=os.popen("ping "+self.lineEdit.text()+" -c 1").read()
            for line in status.split("\n"):
                self.textBrowser_2.append(self.set_green(line))
        elif self.comboBox_2.currentIndex() == 2:
            self.textBrowser_2.setText("")
            status=os.popen("sudo nmap -sS -O "+self.lineEdit.text(),mode='r').read()
            for line in status.split("\n"):
                self.textBrowser_2.append(self.set_green(line))
    def demons_state(self):
        self.textBrowser.append(self.set_green("ftp"))
        self.textBrowser.append(self.set_green("http"))
        self.textBrowser.append(self.set_green("nfs"))
        self.textBrowser.append(self.set_green("samba"))
        self.textBrowser.append(self.set_green("iscsi"))
    def get_os(self):
        import platform
        temp=platform.linux_distribution()
        ver=temp[0]+" "+temp[1]
        return (ver)

    def choose_os(self):
        if self.checkBox.isChecked():
            self.comboBox.setHidden(False)
        else:
            self.comboBox.setHidden(True)
            self.pushButton.setText(self.get_os())
    def show_advance(self):
        if self.checkBox_2.isChecked():
            self.comboBox_2.setHidden(False)
            self.textBrowser_2.setHidden(False)
            self.lineEdit.setHidden(False)
        else:
            self.comboBox_2.setHidden(True)
            self.textBrowser_2.setHidden(True)
            self.lineEdit.setHidden(True)
    def plot(self):
        
        try:
            win = self.canvas.manager.window
        except AttributeError:
            win = self.canvas.window()
        toolbar = win.findChild(QtWidgets.QToolBar)
        toolbar.setVisible(False)
        ax = self.figure.add_subplot(111)
        while True:
            self.new=psutil.cpu_percent(interval=0.2)
            #print(self.new)
            self.s1.append(self.new)
            ax.clear()
            ax.plot(self.s1,'.-')
            if len(self.s1)==60:
                self.s1.pop(0)
            #print (self.s1)
            self.canvas.draw()
            time.sleep(0.1)
        #self.canvas.draw()
    def set_green(self,data):
        return ("<font color='#20C20E' >"+data+"</font>")
#-------------------------------------------------------------------------------------------------------
class not_root_user(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(400, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl=QtWidgets.QLabel(self.centralwidget)
        self.lbl.setText("<img src='tensed.png' >")
        self.lbl.setFixedSize(400,400)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(290, 370, 90, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda:MainWindow.close())
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Server-Suite"))
        self.pushButton.setText(_translate("MainWindow", "OK"))

def main():
    app = QtWidgets.QApplication(["Server-Suite"])
    form = server_suite()
    form.showMaximized()
    app.exec_()

def main_2():
    app = QtWidgets.QApplication(["Server-Suite"])
    MainWindow = QtWidgets.QMainWindow()
    ui = not_root_user()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    if os.geteuid() != 0:
        main_2()
    else:
        main()