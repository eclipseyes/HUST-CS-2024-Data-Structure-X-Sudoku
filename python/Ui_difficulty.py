# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Qiu\Desktop\杂\python\difficulty.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1175, 838)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(10, -90, 1151, 841))
        self.listView.setObjectName("listView")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(370, 90, 501, 201))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(60)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.easy = QtWidgets.QPushButton(self.centralwidget)
        self.easy.setGeometry(QtCore.QRect(280, 360, 231, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        self.easy.setFont(font)
        self.easy.setObjectName("easy")
        self.simple = QtWidgets.QPushButton(self.centralwidget)
        self.simple.setGeometry(QtCore.QRect(620, 360, 221, 91))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        self.simple.setFont(font)
        self.simple.setObjectName("simple")
        self.intermediate = QtWidgets.QPushButton(self.centralwidget)
        self.intermediate.setGeometry(QtCore.QRect(280, 510, 231, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        self.intermediate.setFont(font)
        self.intermediate.setObjectName("intermediate")
        self.expert = QtWidgets.QPushButton(self.centralwidget)
        self.expert.setGeometry(QtCore.QRect(620, 500, 221, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        self.expert.setFont(font)
        self.expert.setObjectName("expert")
        self.difficulty_back = QtWidgets.QPushButton(self.centralwidget)
        self.difficulty_back.setGeometry(QtCore.QRect(100, 40, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.difficulty_back.setFont(font)
        self.difficulty_back.setObjectName("difficulty_back")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1175, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "选择难度"))
        self.easy.setText(_translate("MainWindow", "简单"))
        self.simple.setText(_translate("MainWindow", "基础"))
        self.intermediate.setText(_translate("MainWindow", "中级"))
        self.expert.setText(_translate("MainWindow", "专家"))
        self.difficulty_back.setText(_translate("MainWindow", "返回"))
