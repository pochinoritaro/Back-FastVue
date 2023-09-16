import data
from fastapi import FastAPI
import uvicorn
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/user/{username}")
def read_user(username: str):
    return data.read_userdata(username)

@app.post("/event/{description}")
def read_user(description: str):
    return data.create_schedule(description)

@app.post("/event/{event}")
def read_event(event):
    print(data.read_schedule(event))
    member = list(data.read_schedule(event)[0])
    infos = data.read_schedule(event)[1]
    member_list = []
    for i in member:
        member_list.append(i)
    return data.read_schedule(event)

if __name__ == '__main__':
    uvicorn.run(app=app)