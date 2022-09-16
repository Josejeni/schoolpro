from .database import client,session , test_register
from app import utils
from jose import jwt
from app.config import settings
from app import file1

def test_root(client):
   res= client.get("/")
   print(res.json())



def test_login(client,test_register):
    print(test_register['user_name'])
    print(test_register['password'])
    res=client.post("/log_encrypt",data={"username":test_register['user_name'],"password":test_register['password']})
    print(res.json())
    res_token_detail = file1.token(** res.json())
    payload=jwt.decode(res_token_detail.access_token,settings.secret_key,settings.algorithm)
    username=payload.get('user_name')
    print(username)
    assert username == test_register['user_name']
  

