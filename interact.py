import fileinput
import sys
from sanitize import *
from pathlib import Path

def queryDB(r):
	queryEntered=input('>>>')
	queryEnteredCommand=queryEntered.split()
	if queryEnteredCommand[0].lower()=='exit':
		#go back
		return
	if queryEnteredCommand[0]=='SELECT':
		querySelect(r,queryEnteredCommand)
	
	else:
		print(queryEnteredCommand[0])
		queryDB(r)
	
def newCConfig(n):
	return '#column_name: '+n
	
def createCol(r):
	#THIS WILL BE DElETED WHEN QUERYDB IS FINISHED
	colCreated=0;
	print('Name the column')
	ColName=input()
	if ColName.lower()=='exit':
		#go back
		return
	isSane=namingSaniT(ColName)
	if not isSane:
		print ('this is not a valid name')
	
	#if the table already exist do something CODE LATER
	
	else:
		routeToCol=r+'/cols/'+ColName+'.cxdb'
		if Path(routeToCol).is_file():
			print("sorry, the column already exists")
			createCol(r)
		newcubexC = open(routeToCol,'w+')
		newcubexC.write(newCConfig(ColName))
		newcubexC.close()
		
		filedb=fileinput.input(r+'/headersconf.cxdb','w+')
		for line in filedb:
			if '#columns#' in line:
				colCreated = 1
				line=(ColName+'\n'+line)
			sys.stdout.write(line)
					
		filedb.close()
				
		if colCreated:
			print ('column succesfully created')
		else:
			print('Something went wrong')
		
	
def populate():
	pass
	
def querySelect(r,q):
	
	with open(r+'/cols/'+q[5]+'.cxdb','r') as cl:
		idList=[]
		for line in cl:
			line=line[1:]
			
			lineTag=[]
	
			lineTag=line.split('#')
			
			
			#this is hacky
			lineTag.append('')
			lineTag.append('')
			
			#rstrip removes \n doesn't work directly on line
			#not sure why, it's hacky too but works
			if lineTag[1].rstrip()==q[3] and lineTag[1].rstrip()!='':
				idList.append(lineTag[0])
				
	
	with open(r+'/cols/'+q[5]+'.cxdb','r') as cl:
		for line in cl:
			line=line[1:]
			lineTag=[]
			lineTag=line.split('#')
			
			#this is hacky
			lineTag.append('')
			lineTag.append('')
				
			if lineTag[0] in idList:
				print (lineTag[1])

			
			
