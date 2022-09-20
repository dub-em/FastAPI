from fastapi import status, HTTPException, APIRouter
from .. import schemas
from .. import utils, database

router = APIRouter(
    tags=['Users']
)

cursor = database.cursor
conn = database.conn

@router.post("/users", status_code=status.HTTP_201_CREATED, response_model=schemas.UserCreateResponse)
def create_user(user: schemas.UserCreate):

    #hash the password - user password
    hashed_password = utils.hash(user.password)
    user.password = hashed_password

    cursor.execute("""INSERT INTO users (email, password) VALUES (%s, %s) RETURNING *""",(user.email, user.password))
    new_user = cursor.fetchone()
    conn.commit()
    return new_user

@router.get('/users/{id}', response_model=schemas.GetUserResponse)
def get_user(id: int):
    cursor.execute("""SELECT * FROM users WHERE id = %s""", (str(id)))
    user = cursor.fetchone()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"User with id {id} was not found!")
    return user