from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

SQLALCHEMY_DATABASE_URL = 'sqlite:///./app_database.db'

engine = create_engine(url=SQLALCHEMY_DATABASE_URL,
                       connect_args= {'check_same_thread': False})

Base = declarative_base()

def get_db():

    try:

        db = Session(bind=engine, autocommit=False, autoflush=False)
        yield db

    finally:

        db.close()