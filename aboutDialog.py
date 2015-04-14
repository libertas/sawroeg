# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aboutDialog.ui'
#
# Created: Tue Apr 14 21:19:35 2015
#      by: PyQt4 UI code generator 4.11.3
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 300)
        Dialog.setMaximumSize(QtCore.QSize(400, 300))
        self.title = QtGui.QLabel(Dialog)
        self.title.setGeometry(QtCore.QRect(30, 10, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setText(_fromUtf8(""))
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName(_fromUtf8("title"))
        self.content = QtGui.QTextBrowser(Dialog)
        self.content.setGeometry(QtCore.QRect(10, 50, 381, 241))
        self.content.setObjectName(_fromUtf8("content"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Gvendaengz", None))

