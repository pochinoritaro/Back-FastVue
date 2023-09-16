from .decorator import *

#models
from ..models import Base, session, engine
from ..models import User, UserInfo
from ..models import LoginUser
from ..models import Schedule, ScheduleUser

#schemas
#from ..schemas import UserBase

def create_db():
	Base.metadata.create_all(bind=engine)

@auto_commit
def create_user(user_name, password):
	user_data = User(user_name=user_name, user_password=password)
	session.add(user_data)

@auto_commit
def update_member(schedule_id, user_id):
    member = ScheduleUser(schedule_id=schedule_id, user_id=user_id)
    session.add(member)

@auto_commit
def create_schedule(description):
    schedule = Schedule(
        schedule_description = description
    )
    session.add(schedule)
    return schedule

@auto_commit
def create_member(schedule_id, user_id):
    member = ScheduleUser(schedule_id=schedule_id, user_id=user_id)
    session.add(member)

@auto_commit
def create_member_debug(user_id):
    member = ScheduleUser(user_id=user_id)
    session.add(member)