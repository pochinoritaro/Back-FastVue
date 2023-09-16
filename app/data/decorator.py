from .models import session

def auto_commit(func):
	def wrapper(*args, **kwargs):
		try:
			func(*args, **kwargs)
		
		except:
			session.rollback()
			raise
		
		finally:
			session.commit()
			session.close()
		
	return wrapper
