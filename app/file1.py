from sre_constants import SUCCESS
from typing import Optional
from urllib import response
from colorama import Cursor
from fastapi import Body, FastAPI,Response,status,HTTPException
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
from .import model
from .database import Base, engine,Sessionlocal
from sqlalchemy.orm import Session
from fastapi import Depends
from fastapi.middleware.cors import CORSMiddleware
from .import utils,jwt
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from socket import socket
from app import schemas
from .model import register


# model.Base.metadata.create_all(bind=engine)


app=FastAPI()

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

def get_db():
    db=Sessionlocal()
    try:
        yield db
    except:
        db.close()


@app.get("/")
def root():
    return{"msg":
    "success"}

class encrypted(BaseModel):
    user_name:str
    password:str

class regis(BaseModel): 
    name:str
    age:int
    gender:str
    father_name:str
    mother_name:str
    user_name:str
    password:str

# for register
@app.get("/")
def root():
    return{"msg":"helllooooooo"}

@app.post("/pwd_encrypt")
def pwd_hashing(post:regis,db:Session=Depends(get_db)):
    pwd=utils.hash(post.password)
    post.password=pwd
    data=db.query(register).filter(post.user_name==register.user_name).first()
    if data:
        return {"msg":"alreday existed"}
    else:
        data=register(**post.dict())
        db.add(data)
        db.commit()
        db.refresh(data)
        return data

# For login

@app.post('/log_encrypt')
def log(post:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    print(post.username)
    data=db.query(model.register).filter(model.register.user_name==post.username)
    data1=data.first()
   
    
    if not data1:
        return {"detail":"Not Found"}   
    print(data1.password , post.password)
    data2=utils.Verify( post.password , data1.password)
    # data2=post.password

    if not data2:
        return {"detail2":"Not Found"}
        
    access_token=jwt.create_token({"user_name":post.username}) 
    return{"access_token": access_token, "token_type":"bearer"}

# For getting user profile

@app.get("/user_profile/")
def userprofile(db:Session=Depends(get_db), user=Depends(jwt.get_current_user)):
    data=db.query(model.register).filter(model.register.user_name == user.user_name).first()
    return data

# For getting general information

@app.get("/generalinfo/")
def test_post(db:Session=Depends(get_db), user=Depends(jwt.get_current_user)):
    new_post=db.query(model.general).filter(model.general.user_name==user.user_name).first()
    if new_post==None:
        return"not valid"
    return new_post

# For posting the general information


@app.post('/general/')
def gen(post:dict,db:Session=Depends(get_db),user=Depends(jwt.get_current_user)):
    print(post)
    print("works")
    new_post=model.general(user_name=user.user_name,**post)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return{"successful"}

#For Updating the user profile

@app.put("/update/")
def updated(post:schemas.Put,db:Session=Depends(get_db),user=Depends(jwt.get_current_user)):
    print("hii")
    updated_post=db.query(model.register).filter(model.register.user_name==user.user_name)
    up=updated_post.first()
    if up==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Page not found")
    new=updated_post.update(post.dict(),synchronize_session=False)
    db.commit()
    return new

  # For deleting the user
   
@app.delete("/user_deleted")
def delete_post(db:Session=Depends(get_db),user=Depends(jwt.get_current_user)):
    print("hiiii")
    new_post=db.query(model.register).filter(model.register.user_name==user.user_name)
    if new_post.first()==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"the user_name:{user.user_name} does not exist")
    new_post.delete(synchronize_session=False)
    db.commit()   
    return response(status_code=status.HTTP_204_NO_CONTENT)






class token(BaseModel):
    access_token:str
    token_type:str 

class access_token(BaseModel):
    title:str
    content:str
   
@app.post("/token_post")
def token_post(post:access_token,db:Session=Depends(get_db), user=Depends(jwt.get_current_user)):
    print(user.username)
    new_post=model.post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return{"data":user}

@app.get("/token_get/{id}")
def gen(id:str,db:Session=Depends(get_db), user=Depends(jwt.get_current_user)):
    data=db.query(model.post).filter(model.post.id==id).first()
    return{"data":data}


@app.put("/token_put/{id}")
def updated(id:int,post:access_token,db:Session=Depends(get_db),user=Depends(jwt.get_current_user)):
    updated_post=db.query(model.post).filter(model.post.id==id)
    up=updated_post.first()
    if up==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Page not found")
    new=updated_post.update(post.dict(),synchronize_session=False)
    db.commit()
    return new
  
@app.delete("/token_delete/{id}")
def delete_post(id:int,db:Session=Depends(get_db),user = Depends(jwt.get_current_user)):
    new_post=db.query(model.post).filter(model.post.id==id)
    if new_post.first()==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"the id:{id} does not exist")
    try :    
        check = new_post.delete(synchronize_session=False)
        db.commit()   
        return response(status_code=status.HTTP_204_NO_CONTENT)
    except Exception as error:
        print(error)    

# code for Academic info

@app.post("/post_academic")
def post_academic(post:dict,db:Session=Depends(get_db)):
    new_post=model.academic(**post)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return{"data":new_post}


# for staff details
@app.post("/post_staffdetails")
def post_academic(post:dict,db:Session=Depends(get_db)):
    new_post=model.staff(**post)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return{"data":new_post}

@app.post("/login")
def login(post:schemas.Get,db:Session=Depends(get_db)):
    print(post)
    data=db.query(model.register).filter(model.register.user_name==post.user_name).first()
    if data:
        pwd=db.query(model.register).filter(model.register.password==post.password).first()
        if pwd:
            return {"id":pwd.id}
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Invalid Credentials")        



@app.post("/sqlalchemy")
def crate_post(post:schemas.Post,db:Session=Depends(get_db)):
    new_post=model.register( **post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return{"data":new_post}
