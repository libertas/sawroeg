#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from  __future__ import unicode_literals

from platform import python_version
if python_version().startswith('2'):
    str=unicode
    FileNotFoundError=IOError

import re
import sys

from PyQt4 import QtGui

from dictionary import *
import mainwindow
import info


try:
    FileNotFoundError
except NameError:
    FileNotFoundError = IOError


def newSearch(key, group):
    if not key:
        return ""

    if group == "Saw":
        result = searchWord(key, False)
    elif group == "Laeh":
        result = searchExamples(key)
    value = ""
    n = 0
    if group != "Laeh":
        for i in result:
            for j in i[1]:
                n += 1
                value += "%d.%s\n" % (n, j)
    else:
        for i in result:
            n += 1
            if not i in value:
                value += "%d.%s\n" % (n, i)
    return value


class MainWindow(QtGui.QWidget, mainwindow.Ui_MainWindow):
    def __init__(self, parent=None):
        # get main window
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        
        # set window title
        self.setWindowTitle("Saw Roeg %s" % info.version)

        # setup icon
        self.setWindowIcon(QtGui.QIcon("icons/sawroeg.png"))

        # move the window to center
        self.move_to_center()

        # setup sawloih
        self.searchingCuengh = False

        # setup comboBox
        self.comboBox.addItem("Saw")  # Word
        self.comboBox.addItem("Laeh")  # Examples

        from sawguq import sawguq
        self.clearText()

    def move_to_center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move(
            (screen.width()-size.width())/2,
            (screen.height()-size.height())/2
        )

    def clearText(self):
        self.lineEdit.setText("")
        self.textBrowser.setText("")

    def newSearch(self):
        key = self.lineEdit.text()
        levenshtein = self.levenshtein.isChecked()
        result = newSearch(key, self.comboBox.currentText())
        if levenshtein:
            import accurate_search
            result = accurate_search.byLevenshtein(key, result)
        self.textBrowser.setText(result)

    def about(self):
        text_about = "%s\n\n%s"
        text_about_default = """Sawroeg: Sawloih Cuengh-Gun duh Daegroeg"""\
                             """Email: horizonvei@gmail.com\n"""\
                             """This software is under GPLv3\n"""

        try:
            text_about = text_about % (
                open("README", "r", encoding="utf-8").read(),
                open("COPYING", "r", encoding="utf-8").read()
                )#In Python3
        except TypeError:
            try:
                text_about = text_about % (
                    open("README", "r").read().decode('utf-8'),
                    open("COPYING", "r").read().decode('utf-8')
                    )#In Python2
            except FileNotFoundError:
                text_about = text_about_default
        except FileNotFoundError:
            text_about = text_about_default

        self.textBrowser.setText(text_about)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
