from typing import List
from pydantic import BaseModel as Base
"""
class UserBase(Base):
    id: int
    name: str

class User(Base):
    id: int
    name: str
    
    class Config():
        orm_mode = True 

class UserDisplay(Base):
    id: int
    name: str
    
    class Config():
        orm_mode = True
"""