from fastapi import status, HTTPException, APIRouter
from typing import List
from .. import schemas, database

router = APIRouter(
    tags=['Posts']
)

cursor = database.cursor
conn = database.conn

@router.get("/posts", response_model=List[schemas.PostResponse])
def get_posts(limit: int = 2):
    cursor.execute("""SELECT * FROM posts LIMIT %s""",(str(limit)))
    posts = cursor.fetchall()
    return posts

@router.post("/posts", status_code=status.HTTP_201_CREATED, response_model=schemas.PostResponse)
def create_post(post: schemas.PostCreate):
    cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING *""",(post.title, post.content, post.published))
    new_post = cursor.fetchone()
    conn.commit()
    return new_post

@router.get("/posts/{id}", response_model=schemas.PostResponse)
def get_post(id: int):
    cursor.execute("""SELECT * FROM posts WHERE id = %s""", (str(id)))
    posts = cursor.fetchone()
    if not posts:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Post with id {id} was not found!")
    return posts

@router.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING *""",(str(id)))
    deleted_post = cursor.fetchone()
    conn.commit() 

    if deleted_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} does not exist!")

    return{"message":f"post {id} was successfully deleted."}

@router.put("/posts/{id}", response_model=schemas.PostResponse)
def update_post(id: int, post: schemas.PostCreate):
    cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *""",(post.title, post.content, post.published, str(id)))
    updated_post = cursor.fetchone()
    conn.commit()

    if updated_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} does not exist!")

    return updated_post