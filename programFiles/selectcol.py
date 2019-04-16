def toSelectCol(q,l):
	iteration=0
	resultOfQuery=[]
	directoryToSelect=l+'/'+q[4]+'/'+q[1]+'.cxdb'
	with open(directoryToSelect,'r')as db:
		for line in db:
			#jump the first iteration
			if (iteration!=0):
				line=line[1:]
				line=line.split('#')
				resultOfQuery.append(line[1])
			iteration+=1
	print (resultOfQuery)
			
