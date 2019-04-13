from programFiles.select import toSelect
import re

#transforms query into list
def toList(q,l):
	#first lets store the columns
	dOne=re.findall('\((.+?)\)',q)
		
	#d1 is for maching on 0dimension
	
	#maybe there is no columns, lets give it None
	
	for i in range (0,2):
		try:
			if dOne[i]:
				#lets eliminate (column) from string 
				q=q.replace('('+dOne[i]+')', '')
		except:
			dOne.append('')
		
	
	#split everything into a list
	dsplited=q.split()
	#push into the list the columns 
	for i in range (0,2):
		dsplited.insert(i+1, dOne[i])
		
	#now 1 to 2 positions are columns
	
	#first position will tell us what to do
	#forced uppercase, this is not a language for aficionados
	
	if dsplited[0]=='SELECT':
		toSelect(dsplited,l)
	if dsplited[0]=='SELECTCOL':
		toSelectCol(dsplited,l)
	if dsplited[0]=='ERASE':
		toErase(dsplited,l)
	if dsplited[0]=='ERASECOL':
		toEraseCol(dsplited,l)
	if dsplited[0]=='ERASEDIM':
		toEraseDim(dsplited,l)
	if dsplited[0]=='ENTER':
		toEnter(dsplited,l)
	else:
		return


#querys the database
def toQuery(l):
	queryentered=input('>>>')
	if queryentered.lower()=='exit':
		return
	#transforms query into list
	qList=toList(queryentered,l)
	toQuery(l)

#Loads a database
def toLoad():
	print ('Select the directory of your Database/(EXIT)')
	dataBaseLoaded=input('>>>')
	if dataBaseLoaded.lower() == 'exit':
		return
	
	#clear ' and empty space for drag and drop into terminal
	dataBaseLoaded= dataBaseLoaded.replace("'", "").strip()
	
	
	#here we are gonna store the db name
	datal = 0
	#lets check if it's a real directory
	try:
		with open(dataBaseLoaded+'/headersconf.cxdb','r')as db:
				
				
			for line in db:
					
				databaseNameMark= '#database_name:'
				if databaseNameMark in line:
					datal = line
					break
	except:
		print("This is not a valid CXDB")
	
	if datal is not 0:
		print(datal+"Succesfully loaded")
		toQuery(dataBaseLoaded)
	
	toLoad()

