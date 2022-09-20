from datetime import date
from pydantic import BaseModel

class login(BaseModel):
    user_name:str
    password:str


class regis(BaseModel): 
    name:str
    age:int
    gender:str
    # father_name:str
    # mother_name:str
    dob:date
    mailid:str
    user_name:str
    password:str


class Post(BaseModel):
    
    name:str
    age:int
    gender:str
    father_name:str
    mother_name:str
    password:str
    user_name:str

class Get(BaseModel):
    user_name:str
    password:str

class info(BaseModel):
    sname:str   
    post:str
    district:str
    state:str
    city:str
    pno:int
    url:str
    email:str
    pcode:int
    slocation:str
    need:str
    ayear:int
    year:int
    slevel:str
    medium:str
    nature:str
    tstaff:int
    gender:str
    girls:int
    boys:int
    students:int
    nstaff:int
    cname:str
    cpno:int
    pname:str
    pemail:str
    ppno:int
    opno:int
    institute_govt:str
    board_affiliated:str
    affiiation_no:int
    affiiation_year:int
    affiiation_condition:str
    affiliation_cons:int
    status_certificate:str
    hindhu:int
    cristian:int
    islam:int
    others:int
    non_believers:int
    fire_certificate:str
    sanitation_certificate:str
    building_certificate:str
    school_owned:str
    name_trust:str
    registered:str
    under_act:str
    registration_year:int
    registration_no:int
    period_validity:int
    name_chairman:str
    designation:str
    address_chairman:str
    pno_chairman:int
    eamil_chairman:str

class Put(BaseModel):
    
    name:str
    age:int
    gender:str
    dob:date
    mailid:str
    user_name:str
    # password:str