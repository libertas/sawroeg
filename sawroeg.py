#! /usr/bin/env python3

from PyQt4 import QtGui

try:
	import sys
except:
	pass

try:
	import re
except:
	pass

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
		
		#setup comboBox
		self.comboBox.addItem("Gyaeuj")#Head
		self.comboBox.addItem("Gyang")#Mid
		self.comboBox.addItem("Laeh")#Examples
		
		from sawguq import sawguq
		for i in sawguq:
			self.bro_text+=str(sawguq[i])
		self.clearText()
	
	def move_to_center(self):
		screen = QtGui.QDesktopWidget().screenGeometry()
		size = self.geometry()
		self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)
	
	def clearText(self):
		self.textBrowser.setText(self.bro_text)
		self.lineEdit.setText("")
	
	def newSearch(self):
		key=self.lineEdit.text()
		self.textBrowser.setText(newSearch(key,self.comboBox.currentText()))
	
	def about(self):
		text_about="Sawroeg:Sawloih Cuengh-Gun duh Daegroeg\n"
		text_about+="Email: horizonvei@gmail.com"
		
		try:
			text_about+="\n"
			text_about+="\n"
			text_about+=open("README").read()
		except:
			pass
		
		try:
			text_about+="\n"
			text_about+="\n"
			text_about+=open("COPYING").read()
		except:
			pass
		
		self.textBrowser.setText(text_about)
		
	
if __name__=="__main__":
	app=QtGui.QApplication(sys.argv)
	window=MainWindow()
	window.show()
	sys.exit(app.exec_())
