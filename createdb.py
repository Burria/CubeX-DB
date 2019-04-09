from sanitize import *
import os

def createDb():
	
	print('Lets create a new database')
	print("In what directory we should"\
	" install it? write EXIT to return")
	directoryToInstall=input()
	
	if (directoryToInstall=='EXIT' or directoryToInstall=='Exit'	
	or directoryToInstall=='exit'):
		#go back to main menu
		import functions
		functions.homeMenu()
	
	print('Name the new database')
	nameofdatabase=input()	
	#no funky names
	nameIsSane=namingSani(nameofdatabase)
	if not nameIsSane: 
		print('Sorry, only alphanumeric characters, dashes and underscores')
		import functions
		functions.homeMenu()
	
	if nameIsSane:
		pathToDB = directoryToInstall+'/'+nameofdatabase
				
		if not os.path.exists(pathToDB):
			os.mkdir(pathToDB)			
			newcubexdb = open(pathToDB+'/headersconf.cxdb','w+')
			newcubexdb.write(newDb(nameofdatabase))
			newcubexdb.close()
		else:
			print("It seems the database already exist"\
			" or a folder with the name of the database")
			import functions
			functions.homeMenu()
			
def newDb(n):
	return '#database_name: '+n+'\n #columns:'
	
	
