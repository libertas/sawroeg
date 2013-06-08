
import sawguq

def searchCuengh(key):
	key0=key[0].upper()
	guq=sawguq.sawguq[key0]
	pos=guq.index(key)
	if pos!=0:
		pos=guq.index("\n"+key)+1
	return guq[pos:]

