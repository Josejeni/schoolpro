from sqlalchemy import Column,Integer,String,Date
from Database.database import Base



class Register(Base):
    __tablename__="register"
    id=Column(Integer)
    name=Column(String,nullable=False,)
    age=Column(Integer,nullable=False,)
    gender=Column(String,nullable=False,)
    mailid=Column(String,nullable=False,unique=True)
    dob=Column(Date)
    password=Column(String,nullable=False,)
    username=Column(String, primary_key= True ,nullable=False,)