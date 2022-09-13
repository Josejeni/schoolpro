from fastapi import HTTPException,status
from jose import JWTError,jwt
from datetime import datetime,timedelta
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from typing import Optional

from sqlalchemy.orm import Session
from . import model
from .database import Base, engine,Sessionlocal
from .config import settings

oAuth = OAuth2PasswordBearer(tokenUrl='log_encrypt',scheme_name="JWT")
# oAuth = OAuth2PasswordBearer(tokenUrl="log_encrypt")
def get_db():
    db=Sessionlocal()
    try:
        yield db
    except:
        db.close()

class Token_data(BaseModel):
    username:Optional[str] = None


 
def create_token(data:dict):
    encode=data.copy()
    exp=datetime.utcnow()+timedelta(minutes=settings.expire_time)
    encode.update({"exp":exp})
    value=jwt.encode(encode,settings.secret_key,algorithm=settings.algorithm)
    return value

def verify_token(token:str,credential_exception):
    try:
        print(token)
        payload=jwt.decode(token,settings.secret_key,settings.algorithm)
        username=payload.get('user_name')
        if username is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
        token_data=username
        
    except Exception as error:
        # print(error)
        raise credential_exception
    return token_data

def get_current_user(token:str=Depends(oAuth),db:Session = Depends(get_db)):
    credential_exception=HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invaild ...")
    token=verify_token(token,credential_exception)
    cur_user=db.query(model.register).filter(model.register.user_name == token).first()
    print(cur_user)
    return cur_user
