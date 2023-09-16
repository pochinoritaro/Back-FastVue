from pydantic import BaseModel as Base
"""
class UserBase(Base):
    id: int
    name: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    name: str
    
    class Config:
        orm_mode = True
"""