
from Models import registermodel
from Schemas import schemas
from Utils import utils
from Controls import main
from sqlalchemy.orm import Session
from fastapi import Depends
from Database.database import get_db
from fastapi import APIRouter



router=APIRouter()

@router.post("/pwd_encrypt")
def pwd_hashing(post:schemas.regis,db:Session=Depends(get_db)):
    pwd=utils.hash(post.password)
    post.password=pwd
    data=db.query(registermodel.register).filter(post.user_name==registermodel.register.user_name).first()
    if data:
        return {"msg":"alreday existed"}
    else:
        data=registermodel.register(**post.dict())
        db.add(data)
        db.commit()
        db.refresh(data)
        return data