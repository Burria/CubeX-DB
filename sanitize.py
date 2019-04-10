import re
strictIlegal= ['/n','headersconf','exit','#columns']

def namingSani(s):
	return re.match('^[A-Za-z0-9_-]+$', s)
		
def namingSaniT(t):	
	if t.lower() in strictIlegal:
		return 0
	else:
		return re.match('^[A-Za-z0-9_-]+$', t)
	
