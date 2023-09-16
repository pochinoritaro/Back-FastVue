from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

DATABASE = 'postgresql'
USER = 'postgres'
PASSWORD = 'password'
HOST = 'postgresql'
PORT = '5432'
DB_NAME = 'fast_vue'

CONNECT_STR = '{}://{}:{}@{}:{}/{}'.format(DATABASE, USER, PASSWORD, HOST, PORT, DB_NAME)

#engine = create_engine('sqlite:///Test.db', echo=True)
engine = create_engine(CONNECT_STR, echo=True)

session = scoped_session(
					sessionmaker(
							autocommit = False,
							autoflush = True,
							bind = engine
						)
					)

Base = declarative_base()
Base.query = session.query_property()
