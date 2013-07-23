
from sawguq import sawguq
from sawgeq import sawgeq

def searchWord(key,from_begin=True):
	if from_begin:
		if key in sawguq:
			for i in sawguq[key]:
				yield i
	else:
		for i in sawguq.values():
			for j in i:
				if key in j:
					yield j

def searchExamples(key):
	result=""
	for i in sawgeq:
		string=sawgeq[i]
		tlist=string.rsplit("\n")
		for j in tlist:
			if key in j:
				result+="%s    --<<%s>>\n"%(j,i)
				yield result

def newSearch(key,group):
	if group=="Gyaeuj":
		result=searchWord(key,True)
	elif group=="Gyang":
		result=searchWord(key,False)
	elif group=="Laeh":
		result=searchExamples(key)
	value=""
	for i in result:
		value+=i
	return value

if __name__=="__main__":
	for i in searchExamples("goengbingz"):
		print(i)
