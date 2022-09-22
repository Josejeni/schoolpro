# from .conftest import client,session , test_register,autherized_client
import re
from Utils import utils
from jose import jwt
from Configuration.config import settings
from Controls import main

def test_root(client):
   res= client.get("/")
   print(res.json())



def test_login(client,test_register):
    print(test_register['user_name'])
    print(test_register['password'])
    res=client.post("/log_encrypt",data={"username":test_register['user_name'],"password":test_register['password']})
    print(res.json())
    res_token_detail = main.token(** res.json())
    payload=jwt.decode(res_token_detail.access_token,settings.secret_key,settings.algorithm)
    username=payload.get('user_name')
    print(username)
    assert username == test_register['user_name']


def test_userproifleupdate(autherized_client):  
   res=autherized_client.put("/update",json={"user_name":"Sherina","name":"Josephinjenifer","age":20,"gender":"female","dob":"2000-3-3","mailid":"jose@gmail.com"})
   new_user = res.json()
   return res.json()

def test_userprofiledelete(autherized_client):
   res = autherized_client.delete("/user_deleted")
   assert res.status_code == 204
   print( {"msg":"deleted"})
  

