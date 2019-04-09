from createdb import *
from loadeddb import *

def homeMenu():
	print("What do you want to do?")
	firstLevel=input()
	firstLevelF(firstLevel)

def firstLevelF(a):
	a=a.lower()
	if a=='0' or a=='c' or a=='create':
		createDb()
		print("Database created succesfully")
		homeMenu()
		
	if a=='1' or a=='l' or a=='load':
		print("Select the database you want to load")
		databaseFulldirectory=input()
		
		#clear ' and empty spaces for drag and drop into terminal
		databaseFulldirectory= databaseFulldirectory.replace("'", "").strip()
		
		loadedDB(databaseFulldirectory)		
		homeMenu()
