
from sawguq import sawguq
from sawgeq import sawgeq

def searchWord(key,method="HEAD"):#method can be "HEAD" or "MID"
	if method=="HEAD":
		if key in sawguq:
			for i in sawguq[key]:
				yield i
	if method=="MID":
		for i in sawguq.values():
			for j in i:
				if key in j:
					yield j
