# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'init.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(778, 624)
        MainWindow.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../home/server-suite/logo128x128.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setMinimumSize(QtCore.QSize(211, 0))
        self.pushButton.setObjectName("pushButton")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.pushButton)
        self.checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox.setObjectName("checkBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.checkBox)
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.comboBox)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setObjectName("pushButton_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.pushButton_2)
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_2.setObjectName("checkBox_2")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.checkBox_2)
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.comboBox_2)
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.groupBox)
        self.textBrowser_2.setMinimumSize(QtCore.QSize(0, 300))
        self.textBrowser_2.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.SpanningRole, self.textBrowser_2)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.SpanningRole, self.lineEdit)
        self.verticalLayout.addWidget(self.groupBox, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.dockWidget = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.dockWidgetContents)
        self.textBrowser.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 11pt \"Cantarell\";")
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_3.addWidget(self.textBrowser)
        self.pushButton_4 = QtWidgets.QPushButton(self.dockWidgetContents)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_3.addWidget(self.pushButton_4)
        self.pushButton_3 = QtWidgets.QPushButton(self.dockWidgetContents)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_3.addWidget(self.pushButton_3)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget)
        self.dockWidget_3 = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget_3.setMinimumSize(QtCore.QSize(120, 200))
        self.dockWidget_3.setMaximumSize(QtCore.QSize(400, 524287))
        self.dockWidget_3.setObjectName("dockWidget_3")
        self.dockWidgetContents_3 = QtWidgets.QWidget()
        self.dockWidgetContents_3.setObjectName("dockWidgetContents_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.dockWidgetContents_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.dockWidget_3.setWidget(self.dockWidgetContents_3)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget_3)
        self.dockWidget_2 = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget_2.setMinimumSize(QtCore.QSize(95, 200))
        self.dockWidget_2.setMaximumSize(QtCore.QSize(400, 524287))
        self.dockWidget_2.setObjectName("dockWidget_2")
        self.dockWidgetContents_2 = QtWidgets.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.dockWidgetContents_2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.dockWidgetContents_2)
        self.textBrowser_3.setStyleSheet("")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.verticalLayout_6.addWidget(self.textBrowser_3)
        self.verticalLayout_7.addLayout(self.verticalLayout_6)
        self.dockWidget_2.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget_2)
        self.dockWidget_4 = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget_4.setObjectName("dockWidget_4")
        self.dockWidgetContents_4 = QtWidgets.QWidget()
        self.dockWidgetContents_4.setObjectName("dockWidgetContents_4")
        self.formLayout_2 = QtWidgets.QFormLayout(self.dockWidgetContents_4)
        self.formLayout_2.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName("formLayout_2")
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.dockWidgetContents_4)
        self.lcdNumber_3.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lcdNumber_3)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_2 = QtWidgets.QLabel(self.dockWidgetContents_4)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_8.addWidget(self.label_2, 0, QtCore.Qt.AlignLeft)
        self.formLayout_2.setLayout(2, QtWidgets.QFormLayout.LabelRole, self.verticalLayout_8)
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.dockWidgetContents_4)
        self.lcdNumber_2.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lcdNumber_2)
        self.label_3 = QtWidgets.QLabel(self.dockWidgetContents_4)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lcdNumber = QtWidgets.QLCDNumber(self.dockWidgetContents_4)
        self.lcdNumber.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.lcdNumber.setObjectName("lcdNumber")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lcdNumber)
        self.label_4 = QtWidgets.QLabel(self.dockWidgetContents_4)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(self.dockWidgetContents_4)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lcdNumber_4 = QtWidgets.QLCDNumber(self.dockWidgetContents_4)
        self.lcdNumber_4.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.lcdNumber_4.setObjectName("lcdNumber_4")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lcdNumber_4)
        self.dockWidget_4.setWidget(self.dockWidgetContents_4)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget_4)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 778, 28))
        self.menuBar.setObjectName("menuBar")
        self.menuView = QtWidgets.QMenu(self.menuBar)
        self.menuView.setObjectName("menuView")
        self.menuSettings = QtWidgets.QMenu(self.menuBar)
        self.menuSettings.setObjectName("menuSettings")
        self.menu_Preferances = QtWidgets.QMenu(self.menuSettings)
        self.menu_Preferances.setObjectName("menu_Preferances")
        self.menuWindow = QtWidgets.QMenu(self.menuBar)
        self.menuWindow.setObjectName("menuWindow")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuTool = QtWidgets.QMenu(self.menuBar)
        self.menuTool.setObjectName("menuTool")
        MainWindow.setMenuBar(self.menuBar)
        self.actionServer_list = QtWidgets.QAction(MainWindow)
        self.actionServer_list.setCheckable(True)
        self.actionServer_list.setObjectName("actionServer_list")
        self.actionCPU_Usage = QtWidgets.QAction(MainWindow)
        self.actionCPU_Usage.setCheckable(True)
        self.actionCPU_Usage.setObjectName("actionCPU_Usage")
        self.actionAll_Status = QtWidgets.QAction(MainWindow)
        self.actionAll_Status.setCheckable(True)
        self.actionAll_Status.setObjectName("actionAll_Status")
        self.actionMinimize = QtWidgets.QAction(MainWindow)
        self.actionMinimize.setCheckable(True)
        self.actionMinimize.setMenuRole(QtWidgets.QAction.NoRole)
        self.actionMinimize.setObjectName("actionMinimize")
        self.actionServer_Suite_Help = QtWidgets.QAction(MainWindow)
        self.actionServer_Suite_Help.setObjectName("actionServer_Suite_Help")
        self.actionAbout_Server_Suite = QtWidgets.QAction(MainWindow)
        self.actionAbout_Server_Suite.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.actionAbout_Server_Suite.setObjectName("actionAbout_Server_Suite")
        self.actionHide_Menu_Bar = QtWidgets.QAction(MainWindow)
        self.actionHide_Menu_Bar.setCheckable(True)
        self.actionHide_Menu_Bar.setObjectName("actionHide_Menu_Bar")
        self.actionRefresh = QtWidgets.QAction(MainWindow)
        self.actionRefresh.setObjectName("actionRefresh")
        self.actionA = QtWidgets.QAction(MainWindow)
        self.actionA.setObjectName("actionA")
        self.actionServer_list_2 = QtWidgets.QAction(MainWindow)
        self.actionServer_list_2.setObjectName("actionServer_list_2")
        self.actionCPU_Usage_2 = QtWidgets.QAction(MainWindow)
        self.actionCPU_Usage_2.setObjectName("actionCPU_Usage_2")
        self.actionMounted_Volumes = QtWidgets.QAction(MainWindow)
        self.actionMounted_Volumes.setObjectName("actionMounted_Volumes")
        self.menuView.addSeparator()
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionServer_list_2)
        self.menuView.addAction(self.actionCPU_Usage_2)
        self.menuView.addAction(self.actionMounted_Volumes)
        self.menu_Preferances.addAction(self.actionServer_list)
        self.menu_Preferances.addAction(self.actionCPU_Usage)
        self.menu_Preferances.addAction(self.actionAll_Status)
        self.menuSettings.addAction(self.menu_Preferances.menuAction())
        self.menuWindow.addAction(self.actionMinimize)
        self.menuWindow.addAction(self.actionHide_Menu_Bar)
        self.menuHelp.addAction(self.actionServer_Suite_Help)
        self.menuHelp.addSeparator()
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout_Server_Suite)
        self.menuTool.addAction(self.actionRefresh)
        self.menuBar.addAction(self.menuView.menuAction())
        self.menuBar.addAction(self.menuSettings.menuAction())
        self.menuBar.addAction(self.menuTool.menuAction())
        self.menuBar.addAction(self.menuWindow.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Server-Suite"))
        self.groupBox.setTitle(_translate("MainWindow", "Server-Suite"))
        self.label.setText(_translate("MainWindow", "Detected Operating System"))
        self.pushButton.setText(_translate("MainWindow", "Linux"))
        self.checkBox.setText(_translate("MainWindow", "No it\'s different"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Debian"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Fedora"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Ubuntu"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Centos"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Kali Linux"))
        self.comboBox.setItemText(5, _translate("MainWindow", "RHEL"))
        self.pushButton_2.setText(_translate("MainWindow", "Go"))
        self.checkBox_2.setText(_translate("MainWindow", "Advance options"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Configure manualy"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "ping"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "port scan"))
        self.pushButton_4.setText(_translate("MainWindow", "http"))
        self.pushButton_3.setText(_translate("MainWindow", "ftp"))
        self.label_2.setText(_translate("MainWindow", "   Downloading.."))
        self.label_3.setText(_translate("MainWindow", "   uploading..."))
        self.label_4.setText(_translate("MainWindow", "   CPU usage (%)"))
        self.label_5.setText(_translate("MainWindow", "   Memory (%)"))
        self.menuView.setTitle(_translate("MainWindow", "&view"))
        self.menuSettings.setTitle(_translate("MainWindow", "&Settings"))
        self.menu_Preferances.setTitle(_translate("MainWindow", "&Preferances"))
        self.menuWindow.setTitle(_translate("MainWindow", "&Window"))
        self.menuHelp.setTitle(_translate("MainWindow", "&Help"))
        self.menuTool.setTitle(_translate("MainWindow", "&Tool"))
        self.actionServer_list.setText(_translate("MainWindow", "&Server list"))
        self.actionCPU_Usage.setText(_translate("MainWindow", "&CPU Usage"))
        self.actionAll_Status.setText(_translate("MainWindow", "&Mounted Volumes"))
        self.actionMinimize.setText(_translate("MainWindow", "Minimize"))
        self.actionMinimize.setShortcut(_translate("MainWindow", "Ctrl+M"))
        self.actionServer_Suite_Help.setText(_translate("MainWindow", "&Server-Suite Help"))
        self.actionServer_Suite_Help.setShortcut(_translate("MainWindow", "Ctrl+?"))
        self.actionAbout_Server_Suite.setText(_translate("MainWindow", "&About Server-Suite"))
        self.actionHide_Menu_Bar.setText(_translate("MainWindow", "Hide Menu Bar"))
        self.actionHide_Menu_Bar.setShortcut(_translate("MainWindow", "Ctrl+H"))
        self.actionRefresh.setText(_translate("MainWindow", "&Refresh"))
        self.actionRefresh.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.actionA.setText(_translate("MainWindow", "a"))
        self.actionServer_list_2.setText(_translate("MainWindow", "&Server list"))
        self.actionCPU_Usage_2.setText(_translate("MainWindow", "&CPU Usage"))
        self.actionMounted_Volumes.setText(_translate("MainWindow", "&Mounted Volumes"))

