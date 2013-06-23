
from sawguq import sawguq
from sawgeq import sawgeq

def add_index_number(string):
	tlist=string.rsplit("\n")
	result=""
	n=1
	for i in tlist:
		if i != "":
			result+="%d.%s\n"%(n,i)
		n+=1
	return result

def newSearch(key):
	try:
		result="A:\n"
		result+=searchCuengh(key,sawguq[key[0].upper()])
		result+="\nB:\n"
		result+=search(key)
		result+="\nC:\n"
		result+=search(key,sawgeq,True)
	except:
		result=search(key)
	return result

def searchCuengh(key,string):
	tlist=string.rsplit("\n")
	result=""
	for i in tlist:
		if i.startswith(key):
			result+=i
			result+="\n"
	return add_index_number(result)

def search(key,guq=sawguq,AeuCohSaw=False):
	result=""
	for i in guq:
		string=guq[i]
		tlist=string.rsplit("\n")
		for j in tlist:
			if key in j:
				result+=j
				if AeuCohSaw:
					result+="    --<<"+i+">>"
				result+="\n"
	return add_index_number(result)
