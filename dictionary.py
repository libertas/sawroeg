
def searchCuengh(key,string):
	tlist=string.rsplit("\n")
	result=""
	for i in tlist:
		if i.startswith(key):
			result+=i
			result+="\n"
	return result

def search(key):
	string=""
	result=""
	import sawguq
	for i in sawguq.sawguq:
		string+=sawguq.sawguq[i]
	tlist=string.rsplit("\n")
	for i in tlist:
		if key in i:
			result+=i
			result+="\n"
	return result
