import re
def toSelect(q,l):
	#for ad in d:
		#print(ad)
	idFound = None
	
	#lets check where we should compare
	

	try: 
		if q[8]=='at':
			directoryToCompare=l+'/'+q[9]+'/'+q[2]+'.cxdb'
	except:
		directoryToCompare=l+'/'+q[2]+'.cxdb'
		
	
	
	
	with open(directoryToCompare,'r')as db:
		for line in db:
			#find id if
			
			#clean this, it's embarasing
			line=line.strip()
			line=line[1:]
			line=line[:-1]
			idSelect=line.split('#')
			
			
			lineS=line.replace(idSelect[0]+'#', '')
			
			#all operators, probably there is a cleaner way to do this
			#but I don't know how to do it
			if q[7]=='=':
				
				if lineS==q[3]:
					#and now we have the id
					
					idFound=(idSelect[0])
					break
			
			if q[7]=='>':
				if lineS>q[3]:
					idFound=(idSelect[0])	
					break
			
			if q[7]=='<':
				if lineS<q[3]:
					idFound=(idSelect[0])
					break	
				
			if q[7]=='<=':
				if lineS<=q[3]:
					idFound=(idSelect[0])
					break
					
			if q[7]=='>=':
				if lineS>=q[3]:
					idFound=(idSelect[0])	
					break
			
			if q[7]=='!=':
				if lineS!=q[3]:
					idFound=(idSelect[0])
					break	
				
		
		#now we have the id probably, lets check
		
		if idFound== None:
			print("Sorry couldn't be found")
			return
		
		
		
		#lets split destiny columns into a new list 
		destinyCol=q[1].split(',')
		
		#xd array
		resultOfQuery=[]
		for col in destinyCol:
			resultOfQuery.append([])
		
		
		
		
		index=0;
		for col in destinyCol:
			index+=1
			if q[5]=='dimension0':
				directiryDestiny=l+'/'+q[1]+'.cxdb'
			else:
				directiryDestiny=l+'/'+q[5]+'/'+col+'.cxdb'
			
			with open(directiryDestiny,'r')as db:
				for line in db:
					
					line=line.strip()
					line=line[1:]
					
					idSelect=line.split('#')
					
					if idSelect[0]==idFound:
						resultOfQuery[index-1].append(idSelect[1])
				
		print (resultOfQuery)




	
