from fastapi import APIRouter,Depends,status,HTTPException
from Schemas import schemas
from Database.database import get_db
from Models import registermodel
import random
from Utils import utils
from sqlalchemy.orm import Session


router=APIRouter()



@router.post("/password_reset")
def Password_reset(data:schemas.Passwordreset,db:Session=Depends(get_db)):
    print(data)
    data = db.query(registermodel.Register).filter(registermodel.Register.mailid == data.email)
    data1=data.first()
    global num 
    if data1: 
        
        num = random.randint(1000,9999)
        return {"msg":num}
    else :
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invaild Email id")




@router.post("/pin_check")
def post(number:dict,db:Session=Depends(get_db)): 
    print(type(number['pin'])) 
    if(number['pin'] == num):
        new=db.query(registermodel.Register).filter(registermodel.Register.mailid==number['email'])
        newpwd=new.first()
        hashed=utils.hash(number['password'])
        newpwd.password=hashed
        print(newpwd)
        print("success")
        return newpwd                                                                                      
    else:
        print("fail")
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Invalid")

@router.put("/update_pwd")
def updated(pwd:dict,db:Session=Depends(get_db)):
    new=db.query(registermodel.Register).filter(registermodel.Register.mailid==pwd['mailid'])
    newspwd=new.first()
    new_pwd=new.update(pwd,synchronize_session=False)
    db.commit()
    print(new_pwd)