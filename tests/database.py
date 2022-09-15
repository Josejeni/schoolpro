from fastapi.testclient import TestClient
from app.file1 import app
from app.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.file1 import get_db
from app.database import Base
import pytest
from sqlalchemy.ext.declarative import declarative_base
from app import utils



SQLALCHEMY_DATABASE_URL='postgresql://postgres:postgres@localhost:5432/fastapi_test'
engine=create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionlocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)


client=TestClient(app)

@pytest.fixture
def session():
    Base.metadata.drop_all(bind=engine)
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
    # print("hii")
    user_data={"user_name":"sneha","password":"jose@123","name":"josephin","age":22,"gender":"female","father_name":"selvam","mother_name":"selvi"}
    res=client.post("/pwd_encrypt",json=user_data)
    new_user = res.json()
    new_user['password'] = user_data['password']
    return new_user
    # return res.json()
    



            
    






   
    