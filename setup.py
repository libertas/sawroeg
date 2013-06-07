#! /usr/bin/env python3

python_name="python3" #change it if it's not "python3"

from os import system

system("cp -r ./ /opt/sawroeg/")
system('echo "'+python_name+' /opt/sawroeg/sawroeg.py" > /usr/local/bin/sawroeg')
system("chmod +x /usr/local/bin/sawroeg")
