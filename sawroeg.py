#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import re
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
import mainwindow
import aboutDialog
import info
from enviroment import *
from new_search import newSearch

from platform import python_version
if python_version().startswith('2'):
    str = unicode
    FileNotFoundError = IOError

try:
    FileNotFoundError
except NameError:
    FileNotFoundError = IOError


class myAboutDialog(QtWidgets.QDialog,  aboutDialog.Ui_Dialog):
    def __init__(self,  parent = None):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.title.setText("Sawreog " + info.version)
        
        text_about = "%s\n\n%s"
        text_about_default = """Sawroeg: Sawloih Cuengh-Gun duh Daegroeg"""\
                             """Email: horizonvei@gmail.com\n"""\
                             """This software is under GPLv3\n"""

        try:
            text_about = text_about % (
                open("README", "r", encoding="utf-8").read(),
                open("COPYING", "r", encoding="utf-8").read()
                )  # In Python3
        except TypeError:
            try:
                text_about = text_about % (
                    open("README", "r").read().decode('utf-8'),
                    open("COPYING", "r").read().decode('utf-8')
                    )  # In Python2
            except FileNotFoundError:
                text_about = text_about_default
        except FileNotFoundError:
            text_about = text_about_default
        self.content.setText(text_about)


class MainWindow(QtWidgets.QMainWindow, mainwindow.Ui_MainWindow):
    def __init__(self, parent=None):
        # get main window
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

        # set window title
        self.setWindowTitle("Sawroeg %s" % info.version)

        # setup icon
        self.setWindowIcon(QtGui.QIcon("icons/sawroeg.png"))

        # move the window to center
        self.move_to_center()

        # setup sawloih
        self.searchingCuengh = False

        # setup comboBox
        for item_name in groupList:
            self.comboBox.addItem(item_name)

        self.clearText()

    def move_to_center(self):
        screen = QtWidgets.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move(
            (screen.width()-size.width()) / 2,
            (screen.height()-size.height()) / 2
        )

    def clearText(self):
        self.lineEdit.setText("")
        self.textBrowser.setText("")

    def newSearch(self):
        key = self.lineEdit.text()
        group = self.comboBox.currentText()
        result_yield = newSearch(key, group, dbpath=groupDB[group])
        result = ""
        n = 1
        for i in result_yield:
            result += "%d.%s\n" % (n, i)
            n += 1
        self.textBrowser.setText(result)

    def about(self):
        myAboutDialog(parent = self).exec_()


if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
