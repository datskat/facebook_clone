from turtle import title
from fastapi import FastAPI
from sqlalchemy import Column, Integer, String
from utils.models import Post
from utils.database import Base


app = FastAPI()

class Post_db(Base):

    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    

@app.get('/')
async def root():

    return {'API': 'created'}


@app.post('/createpost')
async def create_post(post: Post):

    print(f'Created post with title: {post.title}')
    print(f'Content of the post: {post.content}')
    return post
