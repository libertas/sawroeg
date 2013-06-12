
def add_index_number(string):
	tlist=string.rsplit("\n")
	result=""
	n=1
	for i in tlist:
		if i != "":
			result+="%d.%s\n"%(n,i)
		n+=1
	return result

def searchCuengh(key,string):
	tlist=string.rsplit("\n")
	result=""
	for i in tlist:
		if i.startswith(key):
			result+=i
			result+="\n"
	return add_index_number(result)

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
	return add_index_number(result)
