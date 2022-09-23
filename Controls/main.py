from urllib import response
from fastapi import FastAPI,status,HTTPException
from pydantic import BaseModel
from .Router import loginpage, schoolprofile
from Models import model
from Database.database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends
from fastapi.middleware.cors import CORSMiddleware
from Autentication import jwt
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from Schemas import schemas
from .Router.loginpage import router
from .Router import userprofile,loginpage,register,forgotpassword
import random
from Utils import utils





# model.Base.metadata.create_all(bind=engine)
# num:int

app=FastAPI()


app.include_router(userprofile.router)
app.include_router(loginpage.router)
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






