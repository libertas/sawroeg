# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Thu Jun  6 20:02:06 2013
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
        self.lineEdit.setGeometry(QtCore.QRect(160, 10, 221, 41))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton = QtGui.QPushButton(MainWindow)
        self.pushButton.setGeometry(QtCore.QRect(390, 10, 91, 41))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.lineEdit_2 = QtGui.QLineEdit(MainWindow)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 60, 221, 41))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.pushButton_2 = QtGui.QPushButton(MainWindow)
        self.pushButton_2.setGeometry(QtCore.QRect(390, 60, 91, 31))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label = QtGui.QLabel(MainWindow)
        self.label.setGeometry(QtCore.QRect(10, 10, 141, 41))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(MainWindow)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 141, 41))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.textBrowser = QtGui.QTextBrowser(MainWindow)
        self.textBrowser.setGeometry(QtCore.QRect(10, 110, 371, 221))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.pushButton_3 = QtGui.QPushButton(MainWindow)
        self.pushButton_3.setGeometry(QtCore.QRect(420, 290, 61, 41))
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(MainWindow)
        self.pushButton_4.setGeometry(QtCore.QRect(390, 100, 91, 31))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit.clear)
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit_2.clear)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "Ra &Cuengh", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("MainWindow", "&Ra", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "1.Ra Sawcuengh", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "2.Cuengh rox Gun", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("MainWindow", "&Ndaep", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setText(QtGui.QApplication.translate("MainWindow", "&Baet", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QWidget()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

