"""import sys
from PyQt4.QtCore import QTimeLine
from PyQt4.QtGui import *

class FaderWidget(QWidget):

    def __init__(self, old_widget, new_widget):
    
        QWidget.__init__(self, new_widget)
        
        self.old_pixmap = QPixmap(new_widget.size())
        old_widget.render(self.old_pixmap)
        self.pixmap_opacity = 1.0
        
        self.timeline = QTimeLine()
        self.timeline.valueChanged.connect(self.animate)
        self.timeline.finished.connect(self.close)
        self.timeline.setDuration(333)
        self.timeline.start()
        
        self.resize(new_widget.size())
        self.show()
    
    def paintEvent(self, event):
    
        painter = QPainter()
        painter.begin(self)
        painter.setOpacity(self.pixmap_opacity)
        painter.drawPixmap(0, 0, self.old_pixmap)
        painter.end()
    
    def animate(self, value):
    
        self.pixmap_opacity = 1.0 - value
        self.repaint()

class StackedWidget(QStackedWidget):

    def __init__(self, parent = None):
        QStackedWidget.__init__(self, parent)
    
    def setCurrentIndex(self, index):
        self.fader_widget = FaderWidget(self.currentWidget(), self.widget(index))
        QStackedWidget.setCurrentIndex(self, index)
    
    def setPage1(self):
        self.setCurrentIndex(0)
    
    def setPage2(self):
        self.setCurrentIndex(1)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    
    window = QWidget()
    
    stack = StackedWidget()
    stack.addWidget(QCalendarWidget())
    editor = QTextEdit()
    editor.setPlainText("Hello world! "*100)
    stack.addWidget(editor)
    
    page1Button = QPushButton("Page 1")
    page2Button = QPushButton("Page 2")
    page1Button.clicked.connect(stack.setPage1)
    page2Button.clicked.connect(stack.setPage2)
    
    layout = QGridLayout(window)
    layout.addWidget(stack, 0, 0, 1, 2)
    layout.addWidget(page1Button, 1, 0)
    layout.addWidget(page2Button, 1, 1)
    
    window.show()
    
    sys.exit(app.exec_())



from PyQt4 import QtCore, QtGui

class AnimatedDialog(QtGui.QDialog):

    def __init__(self, parent=None):
        super(AnimatedDialog, self).__init__(parent)

        self.text = QtGui.QLineEdit(self)
        self.text.move(20,20)


    def showEvent(self, event):
        size = self.size()
        start_size = QtCore.QSize(size.width(), 0)
        self.resize(start_size)

        anim = QtCore.QPropertyAnimation(self, 'size', self)
        anim.setStartValue(start_size)
        anim.setEndValue(size)
        anim.setDuration(700)

        self.show()
        anim.start()

        event.accept()


if __name__ == "__main__":
    app = QtGui.QApplication([])
    win = AnimatedDialog()
    win.resize(300,100)
    win.show()
    win.raise_()
    app.exec_()



from PyQt4 import QtCore, QtGui

class AnimatedDialog(QtGui.QDialog):

    def __init__(self, parent=None):
        super(AnimatedDialog, self).__init__(parent)

        self.text = QtGui.QLineEdit(self)
        self.text.move(20,20)
        
        self._shaker = QtCore.QPropertyAnimation(self, 'pos', self)
        self._shaker.setDuration(300)

        self.text.returnPressed.connect(self.shakey)


    def showEvent(self, event):
        size = self.size()
        start_size = QtCore.QSize(size.width(), 0)
        self.resize(start_size)

        anim = QtCore.QPropertyAnimation(self, 'size', self)
        anim.setStartValue(start_size)
        anim.setEndValue(size)
        anim.setDuration(100)

        self.show()
        anim.start()

        event.accept()

    def shakey(self):
        pos = self.pos()
        shaker = self._shaker

        shaker.setStartValue(pos)
        shaker.setEndValue(pos)

        pos.setX(pos.x()+20)
        shaker.setKeyValueAt(.2, pos)
        shaker.setKeyValueAt(.6, pos)

        pos.setX(pos.x()-40)
        shaker.setKeyValueAt(.4, pos)
        shaker.setKeyValueAt(.8, pos)

        shaker.start()


if __name__ == "__main__":
    app = QtGui.QApplication([])
    win = AnimatedDialog()
    win.resize(300,100)
    win.show()
    win.raise_()
    app.exec_()


import matplotlib.pyplot as plt
import psutil
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Used', 'free'
mem=int(float(str(psutil.virtual_memory()).split("=")[3].split(",")[0]))
sizes = [mem, 100-mem,]
explode = (0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()"""
#!/usr/bin/env python
"""
http://matplotlib.sf.net/matplotlib.pylab.html#-pie for the docstring.
"""
"""
from pylab import *

# create figure
figwidth = 10.0    # inches
figheight = 3.5   # inches
figure(1, figsize=(figwidth, figheight))
rcParams['font.size'] = 12.0
rcParams['axes.titlesize'] = 16.0
rcParams['xtick.labelsize'] = 12.0
rcParams['legend.fontsize'] = 12.0
explode=(0.05, 0.0)
colors=('b','g')
Ncols = 3
plotheight = figwidth/Ncols
H = plotheight/figheight
W = 1.0 / Ncols
margin = 0.1
left = [W*margin, W*(1+margin), W*(2+margin)]
bottom = H*margin
width = W*(1-2*margin)
height = H*(1-2*margin)

# cpu utilization
explode=(0.05, 0.0)
colors=('b','g')
utilized = 10.0
free = 100.0 - utilized
fracs = [utilized, free]
axes([left[0], bottom, width, height])
#axes([20, 10, 10, 10])
patches = pie(fracs, colors=colors, explode=explode, autopct='%1.f%%', shadow=True)
title('CPU Throughput')
legend((patches[0], patches[2]), ('Processing', 'Idle'), loc=(0,-.05))

# ROM utilization
utilized = 30.0
free = 100.0 - utilized
fracs = [utilized, free]
axes([left[1], bottom, width, height])
patches = pie(fracs, colors=colors, explode=explode, autopct='%1.f%%', shadow=True)
title('ROM Memory Usage')
legend((patches[0], patches[2]), ('Used', 'Unused'), loc=(0,-.05))

# RAM utilization
utilized = 15.0
free = 100.0 - utilized
fracs = [utilized, free]
axes([left[2], bottom, width, height])
patches = pie(fracs, colors=colors, explode=explode, autopct='%1.f%%', shadow=True)
title('RAM Memory Usage')
legend((patches[0], patches[2]), ('Used', 'Unused'), loc=(0,-.05))

savefig('utilization')
show()"""
#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
ZetCode Advanced PyQt5 tutorial 

This program animates the size of a
widget with QPropertyAnimation.

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
'''

from PyQt5.QtWidgets import QWidget, QApplication, QFrame, QPushButton
from PyQt5.QtCore import QRect, QPropertyAnimation
import sys
             
             
class Example(QWidget):

    def __init__(self):
        super().__init__()
        
        
        self.initUI()
        
    def initUI(self):
        
        self.button = QPushButton("Start", self)
        self.button.clicked.connect(self.doAnim)
        self.button.move(30, 30)
        
        self.frame = QFrame(self)
        self.frame.setFrameStyle(QFrame.Panel | QFrame.Raised)
        self.frame.setGeometry(150, 30, 100, 100)
        
        self.setGeometry(300, 300, 380, 300)
        self.setWindowTitle('Animation')
        self.show()        
        

    def doAnim(self):

        self.anim = QPropertyAnimation(self.frame, b"geometry")
        self.anim.setDuration(10000)
        self.anim.setStartValue(QRect(150, 30, 100, 100))
        self.anim.setEndValue(QRect(150, 30, 200, 200))
        self.anim.start()

if __name__ == "__main__":
    
    app = QApplication([])
    ex = Example()
    ex.show()
    app.exec_()