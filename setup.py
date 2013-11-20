#!/usr/bin/env python3

import os
import sys
import getopt

def print_help():
    print("""Usage:%s [-h|-H] [--help|--prefix|--pyname|--remove]"""%sys.argv[0])

if os.name == "posix":
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hH", ["help", "prefix=","pyname=","remove"])
    except getopt.GetoptError:
        print("Option Error")
        exit()
    
    python_name = "python3"
    REMOVE=False
    
    for opt,result in opts:
        if opt in ("--remove"):
            REMOVE=True
        
        if opt in ("-h","-H","--help"):
            print_help()
            exit()
        
        if opt in ("--prefix="):
            prefix=result
        else:
            prefix="/usr/local/"
        
        if opt in ("--pyname="):
            python_name=result
    
    if REMOVE:
        os.system("rm -fr /opt/sawroeg")
        os.system("rm %s/bin/sawroeg %s/share/applications/sawroeg.desktop"%(prefix,prefix))
    else:
        os.system("mkdir -p /opt/sawroeg/")
        os.system("cp -r ./ /opt/sawroeg/")
        os.system("ln /opt/sawroeg/sawroeg.desktop %s/share/applications/sawroeg.desktop"%prefix)
        os.system('echo "cd /opt/sawroeg/\n'+python_name+' /opt/sawroeg/sawroeg.py" > %s/bin/sawroeg'%prefix)
        os.system("chmod +rx /opt/sawroeg")
        os.system("chmod +x %s/bin/sawroeg"%prefix)
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
            executables=[cx_Freeze.Executable("sawroeg.py", base=base, icon="icons/sawroeg.ico")]
        )
else:
    raise RuntimeError('Unknown operating system type: %s' % repr(os.name))
