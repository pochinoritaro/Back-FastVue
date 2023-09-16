from fastapi import FastAPI
from fastapi import HTTPException,status
from typing import List
import uvicorn

#import CRUD
from data.crud import *

#import schema
#user.py
#from data import schemas

app = FastAPI()

@app.post("/")
def read_root():
    return {"Hello": "World"}
"""
@app.post("/user/{user_id}", response_model=List[schemas.User])
def read_user(user_id: int):
    user_data = read_userdata(user_id)
    if user_data is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="User data is not found.")
    return user_data
"""
@app.post("/test/{test_id}")
def test(test_id):
    user = read_userdata(test_id)
    return dict(id = user[0], name = user[1])

@app.post("/event/{event}")
def read_event(event):
    members =[]
    member_tuple = read_schedule(event)

    for member_data in member_tuple:
        members.append(dict(id=member_data[0], name=member_data[1]))
        
    return dict(member_info = members)