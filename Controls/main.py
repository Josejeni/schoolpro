from urllib import response
from fastapi import FastAPI,status,HTTPException
from pydantic import BaseModel
from .Router import loginpage
from Models import model
from Database.database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends
from fastapi.middleware.cors import CORSMiddleware
from Autentication import jwt
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from Schemas import schemas
from .Router.loginpage import router
from .Router import userprofile,loginpage,generalinformation,register
import random
from Utils import utils





# model.Base.metadata.create_all(bind=engine)
# num:int

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



@app.post("/password_reset")
def Password_reset(data:schemas.Passwordreset,db:Session=Depends(get_db)):
    print(data)
    data = db.query(model.register).filter(model.register.mailid == data.email)
    data1=data.first()
    global num 
    if data1: 
        
        num = random.randint(1000,9999)
        return {"msg":num}
    else :
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invaild Email id")

class pwd(BaseModel):
    email:str
    pin:str
    password:str


@app.post("/pin_check")
def post(number:dict,db:Session=Depends(get_db)): 
    print(type(number['pin'])) 
    if(number['pin'] == num):
        new=db.query(model.register).filter(model.register.mailid==number['email'])
        newpwd=new.first()
        hashed=utils.hash(number['password'])
        newpwd.password=hashed
        print(newpwd)
        print("success")
        return newpwd                                                                                      
    else:
        print("fail")
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Invalid")

@app.put("/update_pwd")
def updated(pwd:dict,db:Session=Depends(get_db)):
    new=db.query(model.register).filter(model.register.mailid==pwd['mailid'])
    newspwd=new.first()
    new_pwd=new.update(pwd,synchronize_session=False)
    db.commit()
    print(new_pwd)


