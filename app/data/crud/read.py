from ..decorator import *
from sqlalchemy.orm import joinedload

#import models
#user.py
from ..models import User

#schedule.py
from ..models import Schedule, ScheduleUser


def read_userdata(id):
    data = session.query(User.user_id, User.user_name).filter(User.user_id==id).first()
    return list(data)

def read_schedule(schedule_id):
    schedule_member = session.query(
        ScheduleUser.user_id, User.user_name).filter(

				ScheduleUser.schedule_id == schedule_id,
                ScheduleUser.user_id == User.user_id).all()

    
    print(schedule_member)
        
    return schedule_member