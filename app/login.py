from asyncio.windows_events import NULL
import re
from typing import Optional
from urllib import response
from colorama import Cursor
from fastapi import Body, FastAPI,Response,status,HTTPException
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from . import model
from .database import engine,Sessionlocal
from sqlalchemy.orm import Session
from fastapi import Depends

model.Base.metadata.create_all(bind=engine)


app=FastAPI()
try:
    con=psycopg2.connect(host='localhost',database='fastapi',user='postgres',password='postgres',cursor_factory=RealDictCursor)
    print("Databse is connected successfully..")
    cursor=con.cursor()
except Exception as error:
    print("Can not connect the database")
    print("Error :",error)
    time.sleep(3)
    
    
class post(BaseModel):
    username:str
    password:str
    

@app.get("/post/{id}")
def get_one(id):
    cursor.execute(f"""SELECT * FROM log WHERE username= {id} """)
    one=cursor.fetchone()
    if not one:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT)
    return{"details:":one}