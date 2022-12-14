from email import header
from fastapi.testclient import TestClient
from Utils import utils
from Controller.main import app
from Configuration.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Controller.main import get_db
from Database.database import Base
import pytest
from sqlalchemy.ext.declarative import declarative_base
from Authentication import oauth2



SQLALCHEMY_DATABASE_URL='postgresql+psycopg2://postgres:postgres@localhost:5432/fastapi_test'
engine=create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionlocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)


client=TestClient(app)

@pytest.fixture
def session():
    # Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db=TestingSessionlocal()
    return db
    

@pytest.fixture
def client(session):
    def override_get_db():
        try:
            yield session
        finally:
            session.close()
    app.dependency_overrides[get_db]=override_get_db
    yield TestClient(app)

@pytest.fixture
def test_register(client):

    user_data={"username":"Sherina","password":"jose@123","name":"josephin","age":22,"gender":"female","dob":"2000-3-3","mailid":"jose@gmail.com"}
    res=client.post("/pwd_encrypt",json=user_data)
    new_user = res.json()
    new_user['password'] = user_data['password']
    return new_user
    # return res.json()

@pytest.fixture
def token(test_register):
    a = oauth2.create_token({'username':test_register["username"]})
    print(a)
    return a

@pytest.fixture
def autherized_client(client,token):
    print("Haiii")
    client.headers = {
        **client.headers,
        "Authorization":f'Bearer {token}'
    }
    return client





            
    






   
    