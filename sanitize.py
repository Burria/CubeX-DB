import re
strictIlegal= ['/n','headersconf']

def namingSani(s):
	return re.match('^[A-Za-z0-9_-]+$', s)
		
def namingSaniT(t):	
	pass
	
