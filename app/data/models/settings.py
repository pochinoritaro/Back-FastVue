from os import getenv

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

load_dotenv("./data/env/.env")

DATABASE = getenv("DATABASE")
USER = getenv("USER")
PASSWORD = getenv("PASSWORD")
HOST = getenv("HOST")
PORT = getenv("PORT")
DB_NAME = getenv("DB_NAME")

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
