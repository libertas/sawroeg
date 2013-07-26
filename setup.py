#!/usr/bin/env python3

import os
import sys

if os.name == "posix":
    python_name = "python3"  # change it if it's not "python3"
    os.system("cp -r ./ /opt/sawroeg/")
    os.system("ln /opt/sawroeg/sawroeg.desktop /usr/share/applications/sawroeg.desktop")
    os.system('echo "cd /opt/sawroeg/\n'+python_name+' /opt/sawroeg/sawroeg.py" > /usr/local/bin/sawroeg')
    os.system("chmod +rx /opt/sawroeg")
    os.system("chmod +x /usr/local/bin/sawroeg")
elif os.name == "nt":
    if len(sys.argv) == 1:
        os.system("setup.py build")
    else:
        import cx_Freeze
        base = "Win32GUI"
        cx_Freeze.setup(
            name="sawroeg",
            version="0.1",
            description="Aen Sawloih Cuengh-Gun ndeu",
            executables=[cx_Freeze.Executable("sawroeg.py", base=base, icon="sawroeg.png")]
        )
else:
    raise RuntimeError('Unknown operating system type: %s' % repr(os.name))
