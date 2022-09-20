from fastapi import FastAPI
from .routers import post, user
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"] #"*" allows every single domain to be able to access our API.
                #If we have an exclusive list of domains we want to have access to our API, then we put them in our list.

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
#uvicorn app.main:app --reload

app.include_router(post.router)
app.include_router(user.router)
 