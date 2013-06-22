#! /usr/bin/env python3

from PyQt4 import QtGui
import sys

from dictionary import *
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
		
		from sawguq import sawguq
		for i in sawguq:
			self.bro_text+=sawguq[i]
		self.clearText()
	
	def move_to_center(self):
		screen = QtGui.QDesktopWidget().screenGeometry()
		size = self.geometry()
		self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)
	
	def clearText(self):
		self.textBrowser.setText(add_index_number(self.bro_text))
		self.lineEdit.setText("")
	
	def newSearch(self):
		key=self.lineEdit.text()
		self.textBrowser.setText(newSearch(key))
	
	def about(self):
		try:
			text_about="Sawroeg:Sawloih Cuengh-Gun duh Daegroeg\n"
		except:
			pass
		
		try:
			text_about+="\n"
			text_about+="\n"
			text_about+=open("README.md").read()
		except:
			pass
		
		try:
			text_about+="\n"
			text_about+="\n"
			text_about+=open("COPYING").read()
			self.textBrowser.setText(text_about)
		except:
			pass
		
	
if __name__=="__main__":
	app=QtGui.QApplication(sys.argv)
	window=MainWindow()
	window.show()
	sys.exit(app.exec_())
