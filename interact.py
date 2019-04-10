
import fileinput
import sys
from sanitize import *
from pathlib import Path

def queryDB():
	pass
	
def newCConfig(n):
	return '#column_name: '+n
	
def createCol(r):
	colCreated=0;
	print('Name the column')
	ColName=input()
	if ColName.lower()=='exit':
		#go back
		return
	isSane=namingSaniT(ColName)
	if not isSane:
		print ('this is not a valid name')
	
	#if the table already exist do something
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
	


			
			
