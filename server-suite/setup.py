#!/usr/bin/python
import sys ,time,os,thread
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtGui as qt
import time
class MoviePlayer(QWidget):
    def __init__(self, parent=None):
		self.loading()


    def work(self):
        #os.system("mkdir -p /usr/bin/server-suite/")
        time.sleep(3)
        self.check.setText('coping files')
        time.sleep(3)
        #os.system("cp -rf content /usr/bin/server-suite/")
        self.check.setText('making Desktop Icon')
        #os.system("cp Server-Suite /usr/share/applications")
        #self.movie_screen.deleteLater()


#---------------------------------------------------------------------------


    def loading(self):
	QWidget.__init__(self, parent=None)
        self.setGeometry(200, 200, 400, 400)
        self.setWindowTitle("Setup. . .")
        self.setWindowIcon(qt.QIcon("images/logo128x128.png"))
        frame=qt.QWidget()
        self.movie_screen = QLabel()
        self.movie_screen.setSizePolicy(QSizePolicy.Expanding,
            QSizePolicy.Expanding)
        self.movie_screen.setAlignment(Qt.AlignCenter)
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.movie_screen)
        self.setLayout(main_layout)
        self.movie = QMovie("images/install.gif", QByteArray(), self)
        self.movie.setCacheMode(QMovie.CacheAll)
        self.movie.setSpeed(100)
        self.movie_screen.setMovie(self.movie)
        self.movie.start()
        self.check= QLabel("\t\tStarting installation.......")
        self.check.move(200,0)
        thread.start_new_thread(self.work,())
        main_layout.addWidget(self.check)
        #self.movie.stop()
app = QApplication(sys.argv)
player = MoviePlayer()
player.movie.start()
player.show()
sys.exit(app.exec_())
