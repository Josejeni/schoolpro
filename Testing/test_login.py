# from .conftest import client,session , test_register,autherized_client
from Utils import utils
from jose import oauth2
from Configuration.config import settings
from Controller import main
from Schemas import schemas

def test_root(client):
   res= client.get("/")
   print(res.json())



def test_login(client,test_register):
    print(test_register['username'])
    print(test_register['password'])
    res=client.post("/log_encrypt",data={"username":test_register['username'],"password":test_register['password']})
    print(res.json())
    res_token_detail = schemas.token(** res.json())
    payload=oauth2.decode(res_token_detail.access_token,settings.secret_key,settings.algorithm)
    username=payload.get('username')
    print(username)
    assert username == test_register['username']


def test_userproifleupdate(autherized_client):  
   res=autherized_client.put("/update",json={"username":"Sherina","name":"Josephinjenifer","age":20,"gender":"female","dob":"2000-3-3","mailid":"jose@gmail.com"})
   new_user = res.json()
   return res.json()

def test_userprofiledelete(autherized_client):
   res = autherized_client.delete("/user_deleted")
   assert res.status_code == 204
   print( {"msg":"deleted"})



def test_getuserprofile(autherized_client):
   res=autherized_client.get("/user_profile")
   print(res.json())

  

