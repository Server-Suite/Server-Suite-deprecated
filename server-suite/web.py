import sys ,time,filecmp
from PyQt4.QtCore import *
from PyQt4.QtGui import * 
class MoviePlayer(QWidget): 
    def __init__(self, parent=None): 
        QWidget.__init__(self, parent) 
        self.setGeometry(200, 200, 400, 400)
        self.setWindowTitle("Updates. . .")
        self.movie_screen = QLabel()
        self.movie_screen.setSizePolicy(QSizePolicy.Expanding, 
            QSizePolicy.Expanding)        
        self.movie_screen.setAlignment(Qt.AlignCenter) 
        main_layout = QVBoxLayout() 
        main_layout.addWidget(self.movie_screen)
        self.setLayout(main_layout) 
        self.movie = QMovie("loading1.gif", QByteArray(), self) 
        self.movie.setCacheMode(QMovie.CacheAll) 
        self.movie.setSpeed(100) 
        self.movie_screen.setMovie(self.movie) 
        self.movie.start()
        check= QLabel("\t\tChecking for updates.......")
        main_layout.addWidget(check)
        #self.available()
        flag=filecmp.cmp('update.file','updated.file')
        if flag==False:
			#check.deleteLater()
			check= QLabel("\t\tUpdate Available")
			main_layout.addWidget(check)
			
			
			
			
#		else:
#			print 'no update'

#	def available(self):
		#os.system("wget updated.file")
#		flag=filecmp.cmp('update.file','updated.file')
#		if flag==False:
#			print 'update available'
			#os.system("mv updated.file  update.file")
#		else:
#			print 'no update'

app = QApplication(sys.argv) 
player = MoviePlayer() 
player.show() 
sys.exit(app.exec_())
