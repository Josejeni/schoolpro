
from app import database,schemas,main,model,jwt
from fastapi import Depends
from sqlalchemy.orm import Session
from fastapi import Body, FastAPI,Response,status,HTTPException
from urllib import response
from fastapi import APIRouter


router= APIRouter()

# For getting the user profile

@router.get("/user_profile/")
def test_post(db:Session=Depends(database.get_db), user=Depends(jwt.get_current_user)):
    new_post=db.query(model.register).filter(model.register.user_name==user.user_name).first()
    if new_post==None:
        return"not valid"
    return new_post

#For Updating the user profile

@router.put("/update")
def updated(post:schemas.Put,db:Session=Depends(database.get_db),user=Depends(jwt.get_current_user)):
    updated_post=db.query(model.register).filter(model.register.user_name==user.user_name)
    up=updated_post.first()
    if up==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Page not found")
    new=updated_post.update(post.dict(),synchronize_session=False)
    db.commit()
    return new

  # For deleting the user
   
@router.delete("/user_deleted",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(db:Session=Depends(database.get_db),user=Depends(jwt.get_current_user)):
    new_post=db.query(model.register).filter(model.register.user_name==user.user_name)
    if new_post.first()==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"the user_name:{user.user_name} does not exist")
    new_post.delete(synchronize_session=False)
    db.commit()   
    