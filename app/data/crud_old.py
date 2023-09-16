from .decorator import *
from .logics import varidate_password, makehash

#models
from .models import Base, session, engine
from .models import User, UserInfo
from .models import LoginUser
from .models import Schedule, ScheduleUser

#schemas
from .schemas import UserBase




def create_db():
	Base.metadata.create_all(bind=engine)
	
def get_user(user_name, password):
	pass

@auto_commit
def set_user(user_name, password):
	if varidate_password(password):
		user_data = User(user_name=user_name, user_password=makehash(password))
		session.add(user_data)
	
	else:
		raise ValueError('lol')

#test
def read_userdata(name):
	data = session.query(User.user_id, User.user_name).filter(User.user_name==name).first()	
	return list(data)

@auto_commit
def create_schedule(description):
    schedule = Schedule(
        schedule_description = description
    )
    session.add(schedule)
    return schedule

@auto_commit
def update_member(schedule_id, user_id):
    member = ScheduleUser(schedule_id=schedule_id, user_id=user_id)
    session.add(member)

def read_schedule(schedule_id):
    member = session.query(User.user_id, User.user_name).filter(ScheduleUser.schedule_id==schedule_id, User.user_id==ScheduleUser.user_id).all()
    schedule = session.query(Schedule.schedule_create_at, Schedule.schedule_description).filter(schedule_id==schedule_id).first()
    return member, schedule
