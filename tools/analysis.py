import jpype

jvmPath = jpype.getDefaultJVMPath()
ext_class_dir = "jars/"
jvmArg = '-Djava.ext.dirs=' + ext_class_dir
jpype.startJVM(jvmPath, jvmArg)

cuengh_tokenizer = jpype.JPackage('org.roeg.cytokenizer').CuenghTokenizer()

vlist = open("tools/sawguq.txt").read().strip().split("\n")
vset = set()
for line in vlist:
    key = line.split("　")[0]
    klist = cuengh_tokenizer.tokenize(key)
    klist = map(lambda x: x.toString(), klist)
    vset |= set(klist)

print(len(vset))
