from passlib.context import CryptContext


pwd_context=CryptContext(schemes=['bcrypt'],deprecated='auto')
def hash(pwd:str):
    return pwd_context.hash(pwd)


def Verify(plain_pwd:any,hashed_pwd:any):
    return pwd_context.verify(plain_pwd,hashed_pwd)
