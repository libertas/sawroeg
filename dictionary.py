
from sawguq import sawguq
from sawgeq import sawgeq

def remove_the_same(string):
	tlist=string.rsplit("\n")
	result=""
	for i in tlist:
		tlist_2=result.rsplit("\n")
		n=True
		for j in tlist_2:
			if i==j:
				n=False
		if n:
			result+=i+"\n"
	return result

def add_index_number(string):
	tlist=string.rsplit("\n")
	result=""
	n=1
	for i in tlist:
		if i != "":
			result+="%d.%s\n"%(n,i)
		n+=1
	return result

def newSearch(key,group=""):
	if key=="":
		return ""
	
	result=""
	
	if "A" in group:
		try:
			result+="A:\n"
			result+=searchCuengh(key,sawguq[key[0].upper()])
			result+="\n"
		except:
			return search(key)
	
	if "B" in group:
		try:
			result+="B:\n"
			result+=search(key)
			result+="\n"
		except:
			return search(key)
	
	if "C" in group:
		try:
			result+="C:\n"
			result+=search(key,sawgeq,True)
			result+="\n"
		except:
			return search(key)
			
	return result

def searchCuengh(key,string):
	tlist=string.rsplit("\n")
	result=""
	for i in tlist:
		if i.startswith(key):
			result+=i
			result+="\n"
	return add_index_number(remove_the_same(result))

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
	return add_index_number(remove_the_same(result))
