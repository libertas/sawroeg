#! /usr/bin/env python3

import os
from os import system
import sys

if os.name=="posix":
    python_name="python3" #change it if it's not "python3"
    
    system("cp -r ./ /opt/sawroeg/")
    system("ln /opt/sawroeg/sawroeg.desktop /usr/share/applications/sawroeg.desktop")
    system('echo "cd /opt/sawroeg/\n'+python_name+' /opt/sawroeg/sawroeg.py" > /usr/local/bin/sawroeg')
    system("chmod +rx /opt/sawroeg")
    system("chmod +x /usr/local/bin/sawroeg")

elif os.name=="nt":
    if len(sys.argv)==1:
        system("setup.py build")
    else:
        from cx_Freeze import setup, Executable  
        base = None  
        base = "Win32GUI"  
        setup(  
            name = "sawroeg",  
            version = "0.1",  
            description = "Aen Sawloih Cuengh-Gun ndeu",  
            executables = [Executable("sawroeg.py", base = base)]) 
