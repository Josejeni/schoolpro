from urllib import response
from fastapi import FastAPI,status,HTTPException
from pydantic import BaseModel
from .Router import login, login, schoolprofile
from Models import model
from Database.database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from Schemas import schemas
from .Router.login import router
from .Router import userprofile,register,forgotpassword
import random
from Utils import utils
from Database.database import engine




model.Base.metadata.create_all(bind=engine)
# num:int

app=FastAPI()


app.include_router(userprofile.router)
app.include_router(login.router)
app.include_router(schoolprofile.router)
app.include_router(register.router)
app.include_router(forgotpassword.router)



origins = [
  
    "http://localhost:4200",
    "https://edustar-profile.herokuapp.com"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return{"msg":"hellloo"}






