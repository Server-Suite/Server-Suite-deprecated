import os,sys,_thread
from subprocess import Popen, PIPE
from debian import Ui_MainWindow
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5 import QtCore, QtGui, QtWidgets
class installThread(QThread):
    signal = pyqtSignal('PyQt_PyObject')

    def __init__(self):
        QThread.__init__(self)
    def run(self,command="systemctl is-active apache2"):#apt-get install -y apache2
        process = Popen(command, stdout=PIPE, shell=True)
        while True:
            line = process.stdout.readline().rstrip()
            if not line:
                break
            #yield line
            self.signal.emit(str(line)[1:])

class debian_script(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(debian_script, self).__init__(parent)
        self.setupUi(self)
        self.object_thread = installThread()
        self.pushButton_5.clicked.connect(lambda:self.object_thread.start())
        self.object_thread.signal.connect(self.install)
    def set_green(self,data):
        return ("<font color='#20C20E' >"+data+"</font>")
    def install(self,result):
        #self.textBrowser.setText("pinging")
        self.textBrowser.append(self.set_green(str(result)))
    
app = QtWidgets.QApplication(["Server-Suite"])
form = debian_script()
form.show()
app.exec_()