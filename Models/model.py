from sqlalchemy import Column,Integer,String,Boolean,ForeignKey,Time,Date
from Database.database import Base
    
class encrypt(Base):
    __tablename__="pwdencrypt" 
    user_name=Column(String,primary_key=True)
    password=Column(String)

  



