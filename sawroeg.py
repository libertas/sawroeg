#! /usr/bin/env python3

from PyQt4 import QtGui
import sys

from dictionary import *
from sawguq import sawguq
import mainwindow


class MainWindow(QtGui.QWidget,mainwindow.Ui_MainWindow):
	def __init__(self,parent=None):
		#get main window
		QtGui.QWidget.__init__(self)
		self.setupUi(self)
		
		self.move_to_center()
		
		#setup sawloih
		self.searchingCuengh=False
		self.bro_text=""
		
		for i in sawguq:
			self.bro_text+=sawguq[i]
		self.textBrowser.setText(self.bro_text)
	
	def move_to_center(self):
		screen = QtGui.QDesktopWidget().screenGeometry()
		size = self.geometry()
		self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)
	
	def clearText(self):
		self.textBrowser.setText(self.bro_text)
		self.lineEdit.setText("")
		self.lineEdit_2.setText("")
	
	def searchCuengh(self):
		key=self.lineEdit.text()
		self.textBrowser.setText(searchCuengh(key,sawguq[key[0].upper()]))
	
	def search(self):
		self.textBrowser.setText(search(self.lineEdit_2.text()))
		
	
if __name__=="__main__":
	app=QtGui.QApplication(sys.argv)
	window=MainWindow()
	window.show()
	sys.exit(app.exec_())