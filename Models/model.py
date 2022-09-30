from sqlalchemy import Column,Integer,String,Boolean,ForeignKey,Time,Date
from Database.database import Base
    
class encrypt(Base):
    __tablename__="pwdencrypt" 
    username=Column(String,primary_key=True)
    password=Column(String)

  



