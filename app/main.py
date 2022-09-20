from urllib import response
from fastapi import FastAPI,status,HTTPException
from pydantic import BaseModel
from .import loginpage, model
from .database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends
from fastapi.middleware.cors import CORSMiddleware
from .import jwt
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from app import schemas 
from app.loginpage import router
from . import userprofile,loginpage,generalinformation,register




# model.Base.metadata.create_all(bind=engine)


app=FastAPI()


app.include_router(userprofile.router)
app.include_router(loginpage.router)
app.include_router(generalinformation.router)
app.include_router(register.router)


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

# @app.post("/login")
# def login(post:schemas.Get,db:Session=Depends(get_db)):
#     print(post)
#     data=db.query(model.register).filter(model.register.user_name==post.user_name).first()
#     if data:
#         pwd=db.query(model.register).filter(model.register.password==post.password).first()
#         if pwd:
#             return {"id":pwd.id}
#     return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Invalid Credentials")        



@app.post("/sqlalchemy")
def crate_post(post:schemas.Post,db:Session=Depends(get_db)):
    new_post=model.register( **post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return{"data":new_post}


