import re
strictIlegal= ['/n']

def namingSani(s):
	return re.match('^[A-Za-z0-9_-]+$', s)
		
	
	
