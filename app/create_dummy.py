import data
from random import randrange, choice

#import CRUD
from data.crud import *

create_db()
#data.set_user('testUser1', 'TestUser1')
id_list=[]
for i in range(50):
    name = ('testUser' + str(i + 1))
    pswd = ('TestUser' + str(i + 1))
    create_user(name, pswd)
    id_list.append(i + 1)
    
for i in range(30):
    create_schedule('This is test Shedule No.' + str(i + 1))
    for member in range(randrange(2, 6)):
        create_member(i + 1, choice(id_list))