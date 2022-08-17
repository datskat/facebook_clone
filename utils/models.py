from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from typing import Union
from utils.database import Base

class Post(BaseModel):

    title: Union[str, None] = None
    content: str

class Post_db(Base):

    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
