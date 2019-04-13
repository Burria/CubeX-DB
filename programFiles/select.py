import re
def toSelect(q,l):
	#for ad in d:
		#print(ad)
	
	with open(l+'/headersconf.cxdb','r')as db:
		for line in db:
			#find id if
			
			#clean this, it's embarasing
			line=line.strip()
			line=line[1:]
			line=line[:-1]
			idSelect=line.split('#')
			
			lineS=line.replace(idSelect[0]+'#', '')
			
			if lineS==q[4]:
				#and now we have the id
				print (idSelect[0])
		return




	
