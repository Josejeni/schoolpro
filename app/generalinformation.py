from app import database,main,model,jwt
from fastapi import Depends
from sqlalchemy.orm import Session
from fastapi import APIRouter

router=APIRouter()

# For getting general information

@router.get("/generalinfo/")
def test_post(db:Session=Depends(database.get_db), user=Depends(jwt.get_current_user)):
    new_post=db.query(model.general).filter(model.general.user_name==user.user_name).first()
    if new_post==None:
        return"not valid"
    return new_post

# For posting the general information


@router.post('/general/')
def gen(post:dict,db:Session=Depends(database.get_db),user=Depends(jwt.get_current_user)):
    print(post)
    print("works")
    new_post=model.general(user_name=user.user_name,**post)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return{"successful"}