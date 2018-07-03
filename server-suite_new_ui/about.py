# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(QtWidgets.QMainWindow):
	def __init__(self, parent=None):
		super(Ui_MainWindow, self).__init__()#parent=parent)
		self.setupUi(self)
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(632, 310)
		x=632
		y=310
		screen = QtWidgets.QDesktopWidget().screenGeometry()
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.Popup)
		#self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
		ht=(screen.height()-y)/2
		wd=(screen.width()-x)/2
		self.setGeometry(wd,ht,x,y)
		self.setFixedSize(x,y)
		self.m=MainWindow
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.label = QtWidgets.QLabel(self.centralwidget)
		self.label.setGeometry(QtCore.QRect(60, 50, 150, 150))
		self.label.setObjectName("label")
		self.widget = QtWidgets.QWidget(self.centralwidget)
		self.widget.setGeometry(QtCore.QRect(30, 260, 591, 46))
		self.widget.setObjectName("widget")
		self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
		self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
		self.horizontalLayout_2.setObjectName("horizontalLayout_2")
		self.pushButton = QtWidgets.QPushButton(self.widget)
		self.pushButton.setObjectName("pushButton")
		self.pushButton.clicked.connect(lambda:self.authors_list())
		self.horizontalLayout_2.addWidget(self.pushButton)
		self.pushButton_2 = QtWidgets.QPushButton(self.widget)
		self.pushButton_2.setObjectName("pushButton_2")
		self.pushButton_2.clicked.connect(lambda:self.license_text())
		self.horizontalLayout_2.addWidget(self.pushButton_2)
		self.pushButton_3 = QtWidgets.QPushButton(self.widget)
		self.pushButton_3.setObjectName("pushButton_3")
		self.horizontalLayout_2.addWidget(self.pushButton_3)
		self.line = QtWidgets.QFrame(self.centralwidget)
		self.line.setGeometry(QtCore.QRect(273, 0, 20, 251))
		self.line.setFrameShape(QtWidgets.QFrame.VLine)
		self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line.setObjectName("line")
		self.label_2 = QtWidgets.QLabel(self.centralwidget)
		self.label_2.setGeometry(QtCore.QRect(310, 10, 301, 41))
		self.label_2.setStyleSheet("font: 75 22pt \"Cantarell\";")
		self.label_2.setObjectName("label_2")
		self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
		self.textBrowser.setGeometry(QtCore.QRect(300, 50, 321, 201))
		self.textBrowser.setAutoFillBackground(True)
		self.textBrowser.setObjectName("textBrowser")
		MainWindow.setCentralWidget(self.centralwidget)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)
	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "About Server-Suite"))
		self.label.setText(_translate("MainWindow", "<img src='logo128x128.png' width='150' height='150'>"))
		self.pushButton.setText(_translate("MainWindow", "Authors"))
		self.pushButton_2.setText(_translate("MainWindow", "License"))
		self.pushButton_3.setText(_translate("MainWindow", "Credits"))
		self.label_2.setText(_translate("MainWindow", "Server-Suite"))
	def authors_list(self):
		list="""<center><br><br><br><br>
<b>Saurabh Londhe</b><br><br>
Sonalkumar Kadelwar<br>
Ashish Chikalikar<br>
Sourabh Deshmukh</center>"""
		self.textBrowser.setText(list)
	def license_text(self):
		data="""
MIT License

Copyright (c) 2018 Server-Suite

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""
		self.textBrowser.setText(data)