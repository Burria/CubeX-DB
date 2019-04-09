def loadedDB(d):
	with open(d,'r')as db:
		
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
	
	else:
		
		print("Sorry this is not a valid CubeX DB or the database is" \
		" more corrupt than a Russian politician")
		

		
		
	
