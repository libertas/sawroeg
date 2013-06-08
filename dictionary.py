
def searchCuengh(key,string):
	tlist=string.rsplit("\n")
	result=""
	for i in tlist:
		if i.startswith(key):
			result+=i
			result+="\n"
	return result
