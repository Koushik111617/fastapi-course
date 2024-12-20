from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine
from .router import post, user, auth, vote
from .config import settings

# models.Base.metadata.create_all(bind=engine)
app = FastAPI()
# origins = ["https://www.google.com", "https://www.youtube.com"]
origins = ["*"]
# before every function this CORSMiddleware (basically its a function that runs before every request) is going to run first
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message": "bind mount worked"}







