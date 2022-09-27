from sqlalchemy import Column,Integer,String,Date
from Database.database import Base



class Register(Base):
    __tablename__="register"
    id=Column(Integer,auto_increment=True)
    name=Column(String,nullable=False,)
    age=Column(Integer,nullable=False,)
    gender=Column(String,nullable=False,)
    mailid=Column(String,nullable=False,unique=True)
    dob=Column(Date)
    password=Column(String,nullable=False,)
    user_name=Column(String, primary_key= True ,nullable=False,)