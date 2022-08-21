from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from utils.database import Base, engine, get_db
from utils.models import Post, PostDb, UserSignIn, UsersDb

app = FastAPI()

Base.metadata.create_all(bind=engine) #Creating db and tables

@app.get('/')
async def root():

    return {'User': 'Not logged'}

@app.get('/all_posts')
async def get_posts(db: Session=Depends(get_db)): #db to otwarcie sesji database
    
    return db.query(PostDb).all()

@app.get('/all_users')
async def get_users(db: Session=Depends(get_db)):

    return db.query(UsersDb).all()

@app.post('/sign_in')
async def sign_in(user: UserSignIn, db: Session=Depends(get_db)):

    user_model = UsersDb()#Initializes instance of the schema
    user_model.email = user.email
    user_model.password = user.password
    user_model.first_name = user.first_name
    user_model.last_name = user.last_name
    user_model.birth_date = user.birth_date#Assigns data to the schema

    db.add(user_model)
    db.commit()

    return {'User created': user}

@app.post('/createpost')
async def create_post(post: Post, db: Session=Depends(get_db)):

    post_model = PostDb()#Initializes instance of schema
    post_model.title = post.title
    post_model.content = post.content#Assigns data to the schema

    db.add(post_model)
    db.commit()

    print(f'Created post with title: {post.title}')
    print(f'Content of the post: {post.content}')

    return HTTPException(status_code=200,
                         detail='Succesfully created post!',
                         headers=post_model.title)

@app.put('/update/{post_id}')
async def update_post(post_id: int, post: Post, db: Session=Depends(get_db)):

    post_to_update = db.query(PostDb).filter(PostDb.id==post_id).first()

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

@app.delete('/delete_post/{post_id}')
async def delete_post(post_id: int, db: Session=Depends(get_db)):

    post_to_delete = db.query(PostDb).filter(PostDb.id==post_id).first()

    if post_to_delete:

        db.delete(post_to_delete)
        db.commit()

    else:

        raise HTTPException(status_code=404,
                            detail=f'Post with id {post_id} not found')