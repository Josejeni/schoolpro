
from app import main,schemas,utils,model
from sqlalchemy.orm import Session
from fastapi import Depends
from .database import get_db
from fastapi import APIRouter



router=APIRouter()

@router.post("/pwd_encrypt")
def pwd_hashing(post:schemas.regis,db:Session=Depends(get_db)):
    pwd=utils.hash(post.password)
    post.password=pwd
    data=db.query(model.register).filter(post.user_name==model.register.user_name).first()
    if data:
        return {"msg":"alreday existed"}
    else:
        data=model.register(**post.dict())
        db.add(data)
        db.commit()
        db.refresh(data)
        return data