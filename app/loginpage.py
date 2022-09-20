# from http.client import HTTPException
from app import main,model,utils,jwt
from .database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from fastapi import APIRouter,status,HTTPException


router=APIRouter()


@router.post('/log_encrypt')
def log(post:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    print(post.username)
    data=db.query(model.register).filter(model.register.user_name==post.username)
    data1=data.first()
   
    
    if not data1:
        return HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="invaild")  
    print(data1.password , post.password)
    data2=utils.Verify( post.password , data1.password)
    # data2=post.password

    if not data2:
        # raise {"data":"invaild"}
    
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Page not found") 
        
    access_token=jwt.create_token({"user_name":post.username}) 
    return{"access_token": access_token, "token_type":"bearer"}
