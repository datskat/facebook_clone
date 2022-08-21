from datetime import date
from pydantic import BaseModel, EmailStr
from sqlalchemy import Column, Integer, String, Date, DateTime
from sqlalchemy.sql import func
from sqlalchemy_utils import EmailType
from typing import Union
from utils.database import Base

class Post(BaseModel):

    title: Union[str, None] = None
    content: str

class UserSignIn(BaseModel):

    first_name: str
    last_name: str
    birth_date: date
    email: EmailStr
    password: str

class UsersDb(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(EmailType, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    birth_date = Column(Date)
    password = Column(String)
    created_at = Column(DateTime,
                        nullable=False,
                        server_default=func.now())

class PostDb(Base):

    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String, nullable=False)
    created_at = Column(DateTime,
                        nullable=False,
                        server_default=func.now())
