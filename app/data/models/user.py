from sqlalchemy import Column, String, Integer, ForeignKey, TIMESTAMP as Timestamp
from sqlalchemy.orm import relationship
from datetime import datetime
from .settings import Base

#relations
from .login_user_history import LoginUser
from .schedule import ScheduleUser


class User(Base):
	__tablename__ = 'user_table'
	
	user_id = Column(Integer, primary_key=True)
	user_name = Column(String(255), nullable=False, unique=True)
	user_password = Column(String(255), nullable=False)
	
	user_create_at = Column(Timestamp, default=datetime.now())
	user_update_at = Column(Timestamp, default=datetime.now())
	
	user_info_table = relationship("UserInfo", back_populates='user_table')
	login_user_table = relationship("LoginUser", back_populates='user_table')
	schedule_user_table = relationship("ScheduleUser", back_populates='user_table')


class UserInfo(Base):
	__tablename__ = 'user_info_table'
	
	info_id = Column(Integer, primary_key=True)
	user_id = Column(Integer, ForeignKey('user_table.user_id'))
	

	first_name = Column(String(255))
	last_name = Column(String(255))
	
	info_create_at = Column(Timestamp, default=datetime.now())
	imfo_update_at = Column(Timestamp, default=datetime.now())
	
	user_table = relationship("User", back_populates='user_info_table')
