
from Authentication import oauth2
from Controller import main
from Models import registermodel
from Schemas import schemas
from Database import database
from fastapi import Depends
from sqlalchemy.orm import Session
from fastapi import status,HTTPException
from urllib import response
from fastapi import APIRouter


router= APIRouter()

# For getting the user profile

@router.get("/user_profile")
def test_post(db:Session=Depends(database.get_db), user=Depends(oauth2.get_current_user)):
    new_post=db.query(registermodel.Register).filter(registermodel.Register.username==user.username).first()
    if new_post==None:
        return"not valid"
    return new_post

#For Updating the user profile

@router.put("/update")
def updated(post:schemas.Put,db:Session=Depends(database.get_db),user=Depends(oauth2.get_current_user)):
    updated_post=db.query(registermodel.Register).filter(registermodel.Register.username==user.username)
    up=updated_post.first()
    if up==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Page not found")
    new=updated_post.update(post.dict(),synchronize_session=False)
    db.commit()
    return new

  # For deleting the user
   
@router.delete("/user_deleted",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(db:Session=Depends(database.get_db),user=Depends(oauth2.get_current_user)):
    new_post=db.query(registermodel.Register).filter(registermodel.Register.username==user.username)
    if new_post.first()==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"the username:{user.username} does not exist")
    new_post.delete(synchronize_session=False)
    db.commit()   
    