# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'not_root.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = not_root_user()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

