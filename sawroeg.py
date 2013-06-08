#! /usr/bin/env python3

from PyQt4 import QtGui
import sys

from dictionary import *
from sawguq import sawguq
import mainwindow


class MainWindow(QtGui.QWidget,mainwindow.Ui_MainWindow):
	def __init__(self,parent=None):
		QtGui.QWidget.__init__(self)
		self.setupUi(self)
		
		self.searchingCuengh=False
		self.bro_text=""
		
		for i in sawguq:
			self.bro_text+=sawguq[i]
		self.textBrowser.setText(self.bro_text)
	
	def clearText(self):
		self.textBrowser.setText(self.bro_text)
		self.lineEdit.setText("")
		self.lineEdit_2.setText("")
	
	def searchCuengh(self):
		self.textBrowser.setText(searchCuengh(self.lineEdit.text()))
		self.searchingCuengh=True
	
	def search(self):
		if self.searchingCuengh==True:
			self.textBrowser.setText(self.bro_text)
		self.textBrowser.find(self.lineEdit_2.text())
		self.searchingCuengh=False
		
	
if __name__=="__main__":
	app=QtGui.QApplication(sys.argv)
	window=MainWindow()
	window.show()
	sys.exit(app.exec_())
