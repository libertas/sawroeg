#! /usr/bin/env python3

import os
from os import system

if os.name=="posix":
	python_name="python3" #change it if it's not "python3"
	
	system("cp -r ./ /opt/sawroeg/")
	system('echo "cd /opt/sawroeg/;'+python_name+' /opt/sawroeg/sawroeg.py" > /usr/local/bin/sawroeg')
	system("chmod +x /usr/local/bin/sawroeg")

elif os.name=="nt":
	from cx_Freeze import setup, Executable  
	base = None  
	base = "Win32GUI"  
	setup(  
		name = "sawroeg",  
		version = "0.1",  
		description = "Aen Sawloih Cuengh-Gun ndeu",  
        executables = [Executable("sawroeg.py", base = base)]) 
