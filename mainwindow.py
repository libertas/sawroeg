# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Mon Feb  3 18:25:04 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(494, 347)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(494, 347))
        self.lineEdit = QtGui.QLineEdit(MainWindow)
        self.lineEdit.setGeometry(QtCore.QRect(80, 10, 151, 41))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.textBrowser = QtGui.QTextBrowser(MainWindow)
        self.textBrowser.setGeometry(QtCore.QRect(10, 50, 471, 281))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.pushButton = QtGui.QPushButton(MainWindow)
        self.pushButton.setGeometry(QtCore.QRect(260, 10, 51, 41))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(MainWindow)
        self.pushButton_2.setGeometry(QtCore.QRect(380, 20, 31, 28))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(MainWindow)
        self.pushButton_3.setGeometry(QtCore.QRect(420, 10, 51, 41))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(MainWindow)
        self.pushButton_4.setGeometry(QtCore.QRect(320, 10, 51, 41))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.comboBox = QtGui.QComboBox(MainWindow)
        self.comboBox.setGeometry(QtCore.QRect(10, 10, 61, 41))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.levenshtein = QtGui.QCheckBox(MainWindow)
        self.levenshtein.setGeometry(QtCore.QRect(230, 30, 21, 16))
        self.levenshtein.setObjectName(_fromUtf8("levenshtein"))
        self.label = QtGui.QLabel(MainWindow)
        self.label.setGeometry(QtCore.QRect(230, 10, 21, 16))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.lineEdit, QtCore.SIGNAL(_fromUtf8("returnPressed()")), MainWindow.newSearch)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.close)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.about)
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.clearText)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.newSearch)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Saw Roeg", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "&Ra", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("MainWindow", "?", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("MainWindow", "N&daep", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setText(QtGui.QApplication.translate("MainWindow", "&Baet", None, QtGui.QApplication.UnicodeUTF8))
        self.levenshtein.setText(QtGui.QApplication.translate("MainWindow", "Cinj", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Cinj", None, QtGui.QApplication.UnicodeUTF8))

