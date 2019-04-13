from programFiles.query import toLoad

def mainmenu():
	print('#MAIN MENU# What do you want to do?')
	print('(L)oad a database/(C)reate a database/(EXIT)')
	mmInput=input('>>>')
	
	if mmInput.lower()=='exit':
		#Exit
		return
	if mmInput.lower()=='l':
		toLoad()
		#this is a hack, but a smart one, because went we return from 
		#functions we dont want to show a wrong command message
		mmInput='ignore'
	if mmInput.lower()=='c':
		toCreate()
		mmInput='ignore'
	elif mmInput!='ignore':
		print('This is not an accepted command')
		
	mainmenu()
