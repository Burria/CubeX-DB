from interact import * 
 

def loadedDB(d):
	with open(d+'/headersconf.cxdb','r')as db:
		
		#here we are gonna store the db name
		datal =''
		for line in db:
			
			databaseNameMark= '#database_name:'
			if databaseNameMark in line:
				datal = line
				break
			
	
	if databaseNameMark in datal:
		datal=datal.replace(databaseNameMark, "").strip()
		print('Database: '+datal+' succesfully loaded')
		
			
		def whatTodo():
			print("(Q)uery de database, (C)reate"\
			"/edit column or (P)opulate de database? EXIT to quit")
			todoNow=input()
			todo=todoNow.lower()
							
			if todo=='q' or todo=='query':
				queryDB(d)
			if todo=='c' or todo=='create':
				createCol(d)
			if todo=='p' or todo=='populate':
				populate()
			if todo=='exit':
				pass
				#it should go to home menu
			else:
				whatTodo()
		
		whatTodo()
	
	else:
		
		print("Sorry this is not a valid CubeX DB or the database is" \
		" more corrupt than a Russian politician")
		

		
		
	
