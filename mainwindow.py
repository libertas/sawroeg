# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(494, 347)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(494, 347))
        self.lineEdit = QtWidgets.QLineEdit(MainWindow)
        self.lineEdit.setGeometry(QtCore.QRect(80, 10, 171, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.textBrowser = QtWidgets.QTextBrowser(MainWindow)
        self.textBrowser.setGeometry(QtCore.QRect(10, 70, 471, 271))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(MainWindow)
        self.pushButton.setGeometry(QtCore.QRect(260, 10, 51, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(MainWindow)
        self.pushButton_2.setGeometry(QtCore.QRect(380, 17, 31, 21))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(MainWindow)
        self.pushButton_3.setGeometry(QtCore.QRect(420, 10, 71, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(MainWindow)
        self.pushButton_4.setGeometry(QtCore.QRect(310, 10, 61, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.comboBox = QtWidgets.QComboBox(MainWindow)
        self.comboBox.setGeometry(QtCore.QRect(10, 10, 61, 41))
        self.comboBox.setObjectName("comboBox")

        self.retranslateUi(MainWindow)
        self.lineEdit.returnPressed.connect(MainWindow.newSearch)
        self.pushButton_3.clicked.connect(MainWindow.close)
        self.pushButton_2.clicked.connect(MainWindow.about)
        self.pushButton_4.clicked.connect(MainWindow.clearText)
        self.pushButton.clicked.connect(MainWindow.newSearch)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Saw Roeg"))
        self.pushButton.setText(_translate("MainWindow", "&Ra"))
        self.pushButton_2.setText(_translate("MainWindow", "?"))
        self.pushButton_3.setText(_translate("MainWindow", "N&daep"))
        self.pushButton_4.setText(_translate("MainWindow", "&Baet"))

