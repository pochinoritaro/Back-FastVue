import hashlib

def makehash(plain_text: str) -> str:
	return hashlib.sha256(plain_text.encode('utf-8')).hexdigest()

def checkhash(plain_text: str, hashed_txt: str) -> bool:
	if makehash(plain_text) == hashed_txt:
		return True
	else:
		return False
