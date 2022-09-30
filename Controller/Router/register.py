
from Models import registermodel
from Schemas import schemas
from Utils import utils
from Controller import main
from sqlalchemy.orm import Session
from fastapi import Depends
from Database.database import get_db
from fastapi import APIRouter,HTTPException,status



router=APIRouter()

@router.post("/pwd_encrypt")
def pwd_hashing(post:schemas.regis,db:Session=Depends(get_db)):
    pwd=utils.hash(post.password)
    post.password=pwd
    data=db.query(registermodel.Register).filter(post.username==registermodel.Register.username).first()
    if data:
        return HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="User name is alredy existed")
    else:
        data=registermodel.Register(**post.dict())
        db.add(data)
        db.commit()
        db.refresh(data)
        return data