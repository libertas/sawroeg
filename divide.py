#!/usr/bin/env python3
from sawguq_old import sawguq

r=list()
for j in sawguq:
	i=sawguq[j]
	l=i.rsplit("\n")
	r.append(l)

r1=dict()
for k in r:
	for i in k:
		try:
			n=i.index("　")
		except:
			continue
		
		j=i[:n]
		if not j in r1:
			r1[j]=list()
		else:
			pass
		r1[j].append(i)

print(repr(r1))


