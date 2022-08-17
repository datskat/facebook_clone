from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from utils.database import engine, SessionLocal, Base
from utils.models import Post, Post_db

app = FastAPI()

Base.metadata.create_all(bind=engine) #Creating db and table

def get_db():#Spróbować context manager

    try:

        db = SessionLocal()
        yield db

    finally:

        db.close()
    
@app.get('/')
async def root(db: Session=Depends(get_db)):

    return db.query(Post_db).all()


@app.post('/createpost')
async def create_post(post: Post, db: Session=Depends(get_db)):

    post_model = Post_db()
    post_model.title = post.title
    post_model.content = post.content

    db.add(post_model)
    db.commit()

    print(f'Created post with title: {post.title}')
    print(f'Content of the post: {post.content}')

    return post

@app.put('/{post_id}')
async def update_post(post_id: int, post: Post, db: Session=Depends(get_db)):

    post_to_update = db.query(Post_db).filter(Post_db.id==post_id).first()

    if post_to_update:

        post_to_update.title = post.title
        post_to_update.content = post.content

        db.add(post_to_update)
        db.commit()

        return post_to_update

    else:

        raise HTTPException(
            status_code=404,
            detail=f'Post with ID {post_id} does not exist')
    

    
