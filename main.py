from fastapi import FastAPI
from utils.models import Post

app = FastAPI()


@app.get('/')
async def root():

    return {'API': 'created'}


@app.post('/createpost')
async def create_post(post: Post):

    print(f'Created post with title: {post.title}')
    print(f'Content of the post: {post.content}')
    return post
