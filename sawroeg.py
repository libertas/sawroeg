#!/usr/bin/env python3

import re
import sys

from PyQt4 import QtGui

from dictionary import *
import mainwindow


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
        self.textBrowser.setText(newSearch(key, self.comboBox.currentText()))

    def about(self):
        text_about=str()
        try:
            text_about += open("README", "r", encoding="utf-8").read()
        except FileNotFoundError:
            text_about += "Sawroeg: Sawloih Cuengh-Gun duh Daegroeg\n"
            text_about += "Email: horizonvei@gmail.com"

        try:
            text_about += "\n\n"
            text_about += open("COPYING", "r",encoding="utf-8").read()
        except FileNotFoundError:
            text_about += "This software is under GPLv3\n"

        self.textBrowser.setText(text_about)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
