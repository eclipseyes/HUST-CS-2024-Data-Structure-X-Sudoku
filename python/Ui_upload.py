# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Qiu\Desktop\mess\sudoku_project\python\upload.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1126, 775)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(0, -20, 1101, 811))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.listView.setFont(font)
        self.listView.setObjectName("listView")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(390, 20, 401, 91))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(48)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.file_choose = QtWidgets.QPushButton(self.centralwidget)
        self.file_choose.setGeometry(QtCore.QRect(400, 150, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.file_choose.setFont(font)
        self.file_choose.setObjectName("file_choose")
        self.saved_path_label = QtWidgets.QLabel(self.centralwidget)
        self.saved_path_label.setGeometry(QtCore.QRect(90, 300, 331, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.saved_path_label.setFont(font)
        self.saved_path_label.setObjectName("saved_path_label")
        self.judge_label = QtWidgets.QLabel(self.centralwidget)
        self.judge_label.setGeometry(QtCore.QRect(170, 650, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.judge_label.setFont(font)
        self.judge_label.setObjectName("judge_label")
        self.judge = QtWidgets.QLabel(self.centralwidget)
        self.judge.setGeometry(QtCore.QRect(370, 640, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.judge.setFont(font)
        self.judge.setObjectName("judge")
        self.dpll_address_label = QtWidgets.QLabel(self.centralwidget)
        self.dpll_address_label.setGeometry(QtCore.QRect(70, 470, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.dpll_address_label.setFont(font)
        self.dpll_address_label.setObjectName("dpll_address_label")
        self.cdcl_time_label = QtWidgets.QLabel(self.centralwidget)
        self.cdcl_time_label.setGeometry(QtCore.QRect(70, 530, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.cdcl_time_label.setFont(font)
        self.cdcl_time_label.setObjectName("cdcl_time_label")
        self.cdcl_time = QtWidgets.QLabel(self.centralwidget)
        self.cdcl_time.setGeometry(QtCore.QRect(290, 540, 131, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.cdcl_time.setFont(font)
        self.cdcl_time.setObjectName("cdcl_time")
        self.cdcl_address_label = QtWidgets.QLabel(self.centralwidget)
        self.cdcl_address_label.setGeometry(QtCore.QRect(70, 570, 181, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.cdcl_address_label.setFont(font)
        self.cdcl_address_label.setObjectName("cdcl_address_label")
        self.rate_label = QtWidgets.QLabel(self.centralwidget)
        self.rate_label.setGeometry(QtCore.QRect(610, 640, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.rate_label.setFont(font)
        self.rate_label.setObjectName("rate_label")
        self.optimization_rate = QtWidgets.QLabel(self.centralwidget)
        self.optimization_rate.setGeometry(QtCore.QRect(790, 650, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.optimization_rate.setFont(font)
        self.optimization_rate.setObjectName("optimization_rate")
        self.upload_back = QtWidgets.QPushButton(self.centralwidget)
        self.upload_back.setGeometry(QtCore.QRect(90, 30, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.upload_back.setFont(font)
        self.upload_back.setObjectName("upload_back")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(90, 150, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.cnf_path = QtWidgets.QLineEdit(self.centralwidget)
        self.cnf_path.setGeometry(QtCore.QRect(90, 230, 921, 31))
        self.cnf_path.setFrame(True)
        self.cnf_path.setObjectName("cnf_path")
        self.save_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_button.setGeometry(QtCore.QRect(730, 290, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.save_button.setFont(font)
        self.save_button.setObjectName("save_button")
        self.saved_path = QtWidgets.QLineEdit(self.centralwidget)
        self.saved_path.setGeometry(QtCore.QRect(80, 360, 931, 31))
        self.saved_path.setObjectName("saved_path")
        self.source_button = QtWidgets.QPushButton(self.centralwidget)
        self.source_button.setGeometry(QtCore.QRect(470, 290, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.source_button.setFont(font)
        self.source_button.setObjectName("source_button")
        self.solve_button = QtWidgets.QPushButton(self.centralwidget)
        self.solve_button.setGeometry(QtCore.QRect(560, 140, 151, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.solve_button.setFont(font)
        self.solve_button.setObjectName("solve_button")
        self.dpll_address = QtWidgets.QLineEdit(self.centralwidget)
        self.dpll_address.setGeometry(QtCore.QRect(250, 470, 771, 31))
        self.dpll_address.setObjectName("dpll_address")
        self.cdcl_address = QtWidgets.QLineEdit(self.centralwidget)
        self.cdcl_address.setGeometry(QtCore.QRect(260, 590, 771, 31))
        self.cdcl_address.setObjectName("cdcl_address")
        self.dpll_button = QtWidgets.QPushButton(self.centralwidget)
        self.dpll_button.setGeometry(QtCore.QRect(560, 420, 331, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.dpll_button.setFont(font)
        self.dpll_button.setObjectName("dpll_button")
        self.cdcl_button = QtWidgets.QPushButton(self.centralwidget)
        self.cdcl_button.setGeometry(QtCore.QRect(560, 540, 331, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.cdcl_button.setFont(font)
        self.cdcl_button.setObjectName("cdcl_button")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(70, 410, 351, 51))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.dpll_time_label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.dpll_time_label.setFont(font)
        self.dpll_time_label.setObjectName("dpll_time_label")
        self.horizontalLayout.addWidget(self.dpll_time_label)
        self.dpll_time = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.dpll_time.setFont(font)
        self.dpll_time.setObjectName("dpll_time")
        self.horizontalLayout.addWidget(self.dpll_time)
        self.better_solve_button_1 = QtWidgets.QPushButton(self.centralwidget)
        self.better_solve_button_1.setGeometry(QtCore.QRect(720, 130, 111, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.better_solve_button_1.setFont(font)
        self.better_solve_button_1.setObjectName("better_solve_button_1")
        self.better_solve_button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.better_solve_button_2.setGeometry(QtCore.QRect(840, 130, 111, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.better_solve_button_2.setFont(font)
        self.better_solve_button_2.setObjectName("better_solve_button_2")
        self.better_solve_button_3 = QtWidgets.QPushButton(self.centralwidget)
        self.better_solve_button_3.setGeometry(QtCore.QRect(960, 130, 111, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.better_solve_button_3.setFont(font)
        self.better_solve_button_3.setObjectName("better_solve_button_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1126, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.file_choose.clicked.connect(self.cnf_path.show) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "问题求解"))
        self.file_choose.setText(_translate("MainWindow", "选择文件"))
        self.saved_path_label.setText(_translate("MainWindow", "解析成txt文件路径（供验证）："))
        self.judge_label.setText(_translate("MainWindow", "结果判定为："))
        self.judge.setText(_translate("MainWindow", "未求解"))
        self.dpll_address_label.setText(_translate("MainWindow", "求解cnf文件地址："))
        self.cdcl_time_label.setText(_translate("MainWindow", "优化算法实现时间："))
        self.cdcl_time.setText(_translate("MainWindow", "（未实现）"))
        self.cdcl_address_label.setText(_translate("MainWindow", "求解cnf文件地址："))
        self.rate_label.setText(_translate("MainWindow", "优化率："))
        self.optimization_rate.setText(_translate("MainWindow", "未完全求解"))
        self.upload_back.setText(_translate("MainWindow", "返回"))
        self.label_4.setText(_translate("MainWindow", "请输入文件路径（cnf格式）："))
        self.save_button.setText(_translate("MainWindow", "打开解析文件"))
        self.source_button.setText(_translate("MainWindow", "打开原文件"))
        self.solve_button.setText(_translate("MainWindow", "基础求解"))
        self.dpll_button.setText(_translate("MainWindow", "打开基础算法求解文件"))
        self.cdcl_button.setText(_translate("MainWindow", "打开优化算法求解文件"))
        self.dpll_time_label.setText(_translate("MainWindow", "基础算法实现时间："))
        self.dpll_time.setText(_translate("MainWindow", "（未实现）"))
        self.better_solve_button_1.setText(_translate("MainWindow", "优化1"))
        self.better_solve_button_2.setText(_translate("MainWindow", "优化2"))
        self.better_solve_button_3.setText(_translate("MainWindow", "优化3"))