# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Wed Jul 24 09:06:20 2013
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(494, 347)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(494, 347))
        self.lineEdit = QtGui.QLineEdit(MainWindow)
        self.lineEdit.setGeometry(QtCore.QRect(90, 10, 161, 41))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.textBrowser = QtGui.QTextBrowser(MainWindow)
        self.textBrowser.setGeometry(QtCore.QRect(10, 60, 471, 281))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.pushButton = QtGui.QPushButton(MainWindow)
        self.pushButton.setGeometry(QtCore.QRect(260, 10, 51, 41))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(MainWindow)
        self.pushButton_2.setGeometry(QtCore.QRect(380, 20, 31, 28))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(MainWindow)
        self.pushButton_3.setGeometry(QtCore.QRect(420, 10, 61, 41))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(MainWindow)
        self.pushButton_4.setGeometry(QtCore.QRect(320, 10, 51, 41))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.comboBox = QtGui.QComboBox(MainWindow)
        self.comboBox.setGeometry(QtCore.QRect(10, 10, 71, 41))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.lineEdit, QtCore.SIGNAL(_fromUtf8("returnPressed()")), MainWindow.newSearch)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.close)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.about)
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.clearText)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.newSearch)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Saw Roeg", None))
        self.pushButton.setText(_translate("MainWindow", "&Ra", None))
        self.pushButton_2.setText(_translate("MainWindow", "?", None))
        self.pushButton_3.setText(_translate("MainWindow", "N&daep", None))
        self.pushButton_4.setText(_translate("MainWindow", "&Baet", None))

