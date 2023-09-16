from sqlalchemy import Column, Integer, ForeignKey, Boolean, TIMESTAMP as Timestamp
from sqlalchemy.orm import relationship
from datetime import datetime
from .settings import Base

class LoginUser(Base):
	__tablename__ = 'login_user_table'
	
	login_id = Column(Integer, primary_key=True)
	user_id = Column(Integer, ForeignKey('user_table.user_id'))
	
	is_login = Column(Boolean)
	login_at = Column(Timestamp, default=datetime.now())
	logout_at = Column(Timestamp, default=datetime.now())
	
	user_table = relationship("User", back_populates='login_user_table')
