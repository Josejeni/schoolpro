from datetime import date
from pydantic import BaseModel


#For loginpage
class login(BaseModel):
    username:str
    password:str



#For registerpage
class regis(BaseModel): 
    name:str
    age:int
    gender:str
    dob:date
    mailid:str
    username:str
    password:str



class info(BaseModel):
    schoolName:str   
    post:str
    district:str
    state:str
    city:str
    schoolPhoneNumber:int
    schoolUrl:str
    schoolEmail:str
    pinCode:int
    schoolLocation:str
    specialChild:str
    academicYear:int
    estabilshedYear:int
    schoolLevel:str
    medium:str
    natureAffiliation:str
    teachingStaff:int
    gender:str
    girls:int
    boys:int
    students:int
    nonTeachingStaff:int
    correspondentName:str
    correspondentPhoneNumber:int
    principleName:str
    principleEmail:str
    principlePhoneNumber:int
    officialPhoneNumber:int
    governmentRecognized:str
    affiliatedBoard:str
    affiiation_no:int
    affiiation_year:int
    affiiation_condition:str
    stateAffiliationCondition:int
    statusCertificate:str
    hindhu:int
    cristian:int
    islam:int
    others:int
    nonBelievers:int
    fireCertificate:str
    sanitationCertificate:str
    buildingCertificate:str
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


#For User profile
class Put(BaseModel):
    name:str
    age:int
    gender:str
    dob:date
    mailid:str
    username:str
   


class Passwordreset(BaseModel):
    email: str
class pin(BaseModel):
    otp:int


class token(BaseModel):
    access_token:str
    token_type:str 