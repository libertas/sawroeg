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

import mainwindow
import info


try:
    FileNotFoundError
except NameError:
    FileNotFoundError = IOError

from new_search import newSearch


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
        if python_version().startswith("2"):
            key = unicode(key.toUtf8(), "utf8", "ignore")
        levenshtein = self.levenshtein.isChecked()
        result_yield = newSearch(key, self.comboBox.currentText(), levenshtein)
        result = ""
        n = 1
        for i in result_yield:
            result += "%d.%s\n" % (n, i)
            n += 1
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
