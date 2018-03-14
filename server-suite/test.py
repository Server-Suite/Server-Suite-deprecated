from PyQt4 import QtCore
from PyQt4 import QtGui as qt
import sys,os,socket,thread
class about():
    def work(self):
        self.data1=""
        cnt=0
        #qt.QWidget.__init__(self,parent=None)
        w=qt.QApplication(sys.argv)
        self.frame=qt.QWidget()
        self.frame.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
        self.frame.setWindowIcon(qt.QIcon("images/logo128x128.png"))
        self.frame.setWindowTitle("chat-app")
        self.frame.l=qt.QPlainTextEdit(self.frame)
        self.frame.l.setReadOnly(True)
        self.frame.l.move(0,0)
        self.frame.l.setFixedSize(500,500)
        self.frame.btn=qt.QPushButton("Quit",self.frame)
        self.frame.btn.clicked.connect(lambda:self.frame.close())
        f=open("/root/home/itl_lab/self/index.html")
        data=""
        for line in f:
            cnt+=1
            data=data+line.strip()
        self.frame.l.appendHtml(data)#"<font color ='red'> Sample Text</font>")
        self.frame.l.verticalScrollBar().setSliderPosition(1)
        screen = qt.QDesktopWidget().screenGeometry()
        self.frame.btn.move(420,470)
        ht=(screen.height()-500)/2
        wd=(screen.width()-500)/2
        self.frame.setGeometry(wd,ht,500,500)
        self.frame.setFixedSize(500,500)
        self.frame.show()
        w.exec_()
    def __init__(self):
        self.work() 

o=about()