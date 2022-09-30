from sqlalchemy import Integer,String,Column,ForeignKey,Time
# from Database.database import Base
from Models.registermodel import Base




class General(Base):
    __tablename__='schoolprofile'
    id = Column(Integer,primary_key=True,autoincrement=True)
    username=Column(String,ForeignKey("register.username",ondelete="CASCADE"))
    schoolName=Column(String)
    post=Column(String)
    district=Column(String)
    state=Column(String)
    city=Column(String)
    schoolPhoneNumber=Column(String)
    schoolUrl=Column(String)
    schoolEmail=Column(String)
    pinCode=Column(String)
    schoolLocation=Column(String)
    specialChild=Column(String)
    academicYear=Column(String)
    estabilshedYear=Column(String)
    schoolLevel=Column(String)
    medium=Column(String)
    natureAffiliation=Column(String)
    teachingStaff=Column(String)
    gender=Column(String)
    girls=Column(String)
    boys=Column(String)
    students=Column(String)
    nonTeachingStaff=Column(String)
    correspondentName=Column(String)
    correspondentPhoneNumber=Column(String)
    principalName=Column(String)
    principalEmail=Column(String)
    principalPhoneNumber=Column(String)
    officialPhoneNumber=Column(String)
    governmentRecognized=Column(String)
    affiliatedBoard=Column(String)
    affiliationNumber=Column(String)
    affiliationYear=Column(String)
    affiliationCondition=Column(String)
    stateAffiliationCondition=Column(String)
    statusCertificate=Column(String)
    hindhu=Column(String)
    cristian=Column(String)
    islam=Column(String)
    others=Column(String)
    nonBelievers=Column(String)
    fireCertificate=Column(String)
    sanitationCertificate=Column(String)
    buildingCertificate=Column(String)
    schoolOwnedBy=Column(String)
    trustName=Column(String)
    trustRegistered=Column(String)
    underAct=Column(String)
    registrationYear=Column(String)
    registrationNumber=Column(String)
    registrationValidity=Column(String)
    chairmanName=Column(String)
    designation=Column(String)
    chairmainAddress=Column(String)
    chairmanPhoneNumber=Column(String)
    chairmanEmail=Column(String)
    governingBody=Column(String)
    trustMember=Column(String)
    tenureMember=Column(String)
    epcc=Column(String)
    epccMember=Column(String)
    epccTenureMember=Column(String)
    parentTeacherAssociation=Column(String)
    parentTeacherAssociationMember=Column(String)
    parentTeacherTenureMember=Column(String)
    studentCouncil=Column(String)
    studentCouncilMembers=Column(String)
    studentCouncilTenureMember=Column(String)
    generalGrievance=Column(String)
    schoolCommittee=Column(String)
    committeeCondition=Column(String)
    committeeConditionMembers=Column(String)
    committeeTenureMember=Column(String)
    schoolBuilding=Column(String)
    campusArea=Column(String)
    builtArea=Column(String)
    playArea=Column(String)
    numberOfBuilding=Column(String)
    provisions=Column(String)
    staircasesNumber=Column(String)
    liftNumber=Column(String)
    classRooms=Column(String)
    staffrooms=Column(String)
    physicsLab=Column(String)
    chemistrylab=Column(String)
    biologylab=Column(String)
    mathslab=Column(String)
    computerscienceLab=Column(String)
    languageLab=Column(String)
    homescienceLab=Column(String)
    library=Column(String)
    auditorium=Column(String)
    counselorroom=Column(String)
    parlor=Column(String)
    chapel=Column(String)
    sickroom=Column(String)
    canteen=Column(String)
    securityroom=Column(String)
    otherroom=Column(String)
    staffToilet=Column(String)
    studenttoilet=Column(String)
    rooms=Column(String)
    specialStudent=Column(String)
    wall=Column(String)
    wallCondition=Column(String)
    cctv=Column(String)
    datasaved=Column(String)
    cameraCount=Column(String)
    maleguard=Column(String)
    maleGuardCount=Column(String)
    femaleguard=Column(String)
    femaleguardCount=Column(String)
    water=Column(String)
    drainage=Column(String)
    middayMeal=Column(String)
    ownedBuses=Column(String)
    gps=Column(String)
    ladyAttendance=Column(String)
    firstaid=Column(String)
    drinkingWater=Column(String)
    subcontracted=Column(String)
    freeTransport=Column(String)
    campusArea=Column(String)
    buspass=Column(String)
    malePrincipal=Column(String)
    femalePrincipal=Column(String)
    temporaryMalePrincipal=Column(String)
    temporaryFemalePrincipal=Column(String)
    maleViceprincipal=Column(String)
    femaleViceprincipal=Column(String)
    temporaryMaleViceprincipal=Column(String)
    temporaryFemaleViceprincipal=Column(String)
   
    postgraduateTeachers=Column(String)
    postgraduateFemaleTeachers=Column(String)
    temporaypgmaleStaff=Column(String)
    temporaypgFemaleStaff=Column(String)
  
    tgMaleStaff=Column(String)
    tgFemaleStaff=Column(String)
    temporarytgMaleStaff=Column(String)
    temporarytgFemaleStaff=Column(String)
   
    primaryMaleStaff=Column(String)
    primaryFemaleStaff=Column(String)
    temporaryPrimarymale=Column(String)
    temporaryPrimaryfemale=Column(String)
   
    nurseryMaleStaff=Column(String)
    nurseryFemaleStaff=Column(String)
    ntTemporaryMale=Column(String)
    ntTemporaryFemale=Column(String)
   
    MaleLibraian=Column(String)
    FemaleLibraian=Column(String)
    temporaryMaleLibrarian=Column(String)
    temporaryFemaleLibrarian=Column(String)
    
    artMaleStaff=Column(String)
    artFemaleStaff=Column(String)
    artTemporaryMalestaff=Column(String)
    artTemporaryFemalestaff=Column(String)
 
    maleCounseller=Column(String)
    femaleCounseller=Column(String)
    temporaryMaleCounseller=Column(String)
    temporaryFemaleCounseller=Column(String)
    
  
    MaleComputerLiteracy=Column(String)
    FemaleComputerLiteracy=Column(String)
    temporaryMaleComputerLiteracy=Column(String)
    temporaryFemaleComputerLiteracy=Column(String)
    
    MaleFaithminister=Column(String)
    FemaleFaithminister=Column(String)
    temporaryMaleFaithminister=Column(String)
    temporaryFemaleFaithminister=Column(String)
 
    maleNurse=Column(String)
    femaleNurse=Column(String)
    temporaryMalenurse=Column(String)
    temporaryFemalenurse=Column(String)

    malePtTeacher=Column(String)
    femalePtTeacher=Column(String)
    temporaryMalept=Column(String)
    temporaryFemalept=Column(String)

  
   
    permanentofficeManager=Column(String)
    temporaryofficeManager=Column(String)
    partimeofficeManager=Column(String)
  
    permanentOfficialAssitent=Column(String)
    temporaryOfficialAssitent=Column(String)
    partimeOfficialAssitent=Column(String)
    # oa_total=Column(String)
    temporaryClerk=Column(String)
    permanentClerk=Column(String)
    partimeClerk=Column(String)
  
    permanentLabAttendants=Column(String)
    temporaryLabAttendants=Column(String)
    partimeLabAttendants=Column(String)
 
    permanentAccountant=Column(String)
    temporaryAccountant=Column(String)
    partimeAccountant=Column(String)
 
    permanentPeon=Column(String)
    temporaryPeon=Column(String)
    partimePeon=Column(String)
    
    permanentOthers=Column(String)
    temporaryOthers=Column(String)
    partimeOthers=Column(String)
    
    untrainMalestaff=Column(String)
    untrainFemalestaff=Column(String)
    untrainedTemporaryMale=Column(String)
    untrainedTemporaryFemale=Column(String)

    curricularActivities=Column(String)
    groups=Column(String)
    communityCount=Column(String)

    lastyearSchoolLevel=Column(String)
    lastyearZonalLevel=Column(String)
    lastyearDistrictLevel=Column(String)
    lastyearStateLevel=Column(String)
    lastyearNationalLevel=Column(String)
    lastyearInternationalLevel=Column(String)

    schoolLevelCompetitions=Column(String)
    zonalLevelCompetitions=Column(String)
    districtLevelCompetitions=Column(String)
    stateLevelCompetitions=Column(String)
    nationalLevelCompetitions=Column(String)
    internationalLevelCompetitions=Column(String)

    schoolLevelProgrammes=Column(String)
    zonalLevelProgrammes=Column(String)
    districtLevelProgrammes=Column(String)
    stateLevelProgrammes=Column(String)
    nationalLevelProgrammes=Column(String)
    internationalLevelProgrammes=Column(String)

    academicYearBegins=Column(String)
    academicYearEnds=Column(String)
    workingdays21=Column(String)
    workingdays20=Column(String)
    workingdays19=Column(String)
    hours21=Column(String)
    hours20=Column(String)
    hours19=Column(String)
    instructionalHours21=Column(String)
    instructionalHours20=Column(String)
    instructionalHours19=Column(String)
    noninstructionalHours21=Column(String)
    noninstructionalHours20=Column(String)
    noninstructionalHours19=Column(String)
    holidays21=Column(String)
    holidays20 =Column(String)
    holidays19=Column(String)

    subjectPerWeek=Column(String)
    morelPerWeek=Column(String)
    teachingDuration=Column(String)
    clubsCount=Column(String)
    timeInSummer=Column(Time)
    totimeInSummer=Column(Time)
    timeInWinter=Column(Time)
    totimeInWinter=Column(Time)
    shifts=Column(Time)
