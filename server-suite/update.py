import sys ,time,os,thread
from PyQt4.QtCore import *
from PyQt4 import QtCore
from PyQt4.QtGui import *
from PyQt4 import QtGui as qt
import filecmp,time
class update(QWidget):
    def __init__(self, parent=None):
        self.loading()
    def work(self):
        time.sleep(3)
        status=None
        while status==None:
            status=filecmp.cmp("update.file","updated.file")
        if status==False:
            self.movie_screen.deleteLater()
            self.check.setText('update available')
            self.check.move(100,100)
        else:
			self.check.setText("Already at Latest version")
			self.check.move(200,0)
			self.movie_screen.deleteLater()
#---------------------------------------------------------------------------
    def loading(self):
	QWidget.__init__(self, parent=None)
        self.setGeometry(200, 200, 400, 400)
        self.setWindowTitle("Updates. . .")
        self.setWindowIcon(qt.QIcon("images/logo128x128.png"))
        #self.lab=QLabel("<img src='images/cloud.jpg' height='500px' width='500px'>",self)
        frame=qt.QWidget()
        self.movie_screen = QLabel()
        self.movie_screen.setSizePolicy(QSizePolicy.Expanding,
            QSizePolicy.Expanding)
        self.movie_screen.setAlignment(Qt.AlignCenter)
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.movie_screen)
        self.setLayout(main_layout)
        self.movie = QMovie("images/loading.gif", QByteArray(), self)
        self.movie.setCacheMode(QMovie.CacheAll)
        self.movie.setSpeed(200)
        self.movie_screen.setMovie(self.movie)
        self.movie.start()
        self.check= QLabel("\t\tChecking for updates.......")
        self.check.move(200,0)
        thread.start_new_thread(self.work,())
        main_layout.addWidget(self.check)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        screen = qt.QDesktopWidget().screenGeometry()
        ht=(screen.height()-500)/2
        wd=(screen.width()-500)/2
        self.setGeometry(wd,ht,500,500)