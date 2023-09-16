from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, TIMESTAMP as Timestamp
from sqlalchemy.orm import relationship
from datetime import datetime
from .settings import Base


class Schedule(Base):
    __tablename__ = 'schedule_table'
    
    schedule_id = Column(Integer, primary_key=True)
    schedule_create_at = Column(Timestamp, default=datetime.now())
    schedule_hold_at = Column(Timestamp)
    schedule_is_done = Column(Boolean, default=False)
    schedule_description = Column(String(255))

    schedule_user_table = relationship("ScheduleUser", back_populates='schedule_table')

class ScheduleUser(Base):
    __tablename__ = 'schedule_user_table'
    member_id = Column(Integer, primary_key=True)
    schedule_id = Column(Integer, ForeignKey('schedule_table.schedule_id'))
    user_id = Column(Integer, ForeignKey('user_table.user_id'))
    
    schedule_table = relationship("Schedule", back_populates='schedule_user_table')
    user_table = relationship("User", back_populates='schedule_user_table')