from re import search

def varidate_password(password):
	if all(((search('[0-9]', password)),
					(search('[a-z]', password)),
					(search('[A-Z]', password)))) and len(password) > 8:
		return  True
	else:
		return False
