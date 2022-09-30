from Authentication import oauth2
from Controller import main
from Models import schoolprofilemodel
from Database import database
from fastapi import Depends
from sqlalchemy.orm import Session
from fastapi import APIRouter

router=APIRouter()

# For getting general information

@router.get("/generalinfo/")
def test_post(db:Session=Depends(database.get_db), user=Depends(oauth2.get_current_user)):
    retrieved=db.query(schoolprofilemodel.General).filter(schoolprofilemodel.General.username==user.username).first()
    if retrieved==None:
        return"not valid"
    return {
        "schoolprofilepage1":{'schoolName':retrieved.schoolName,   
      'post':retrieved.post,
      'district':retrieved.district,
      'state':retrieved.state,
      'city':retrieved.city,
      'schoolPhoneNumber':retrieved.schoolPhoneNumber,
      'schoolUrl':retrieved.schoolUrl,
      'schoolEmail':retrieved.schoolEmail,
      'schoolEmail':retrieved.schoolEmail,
      'schoolLocation':retrieved.schoolLocation,
      'specialChild':retrieved.specialChild,
      'academicYear':retrieved.academicYear,},

        "schoolprofilepage2":{
        'estabilshedYear':retrieved.estabilshedYear,
        'schoolLevel':retrieved.schoolLevel,
        'medium':retrieved.medium,
        'natureAffiliation':retrieved.natureAffiliation,
        'teachingStaff':retrieved.teachingStaff,
        'gender':retrieved.gender,
        'girls':retrieved.girls,
        'boys':retrieved.boys,
        'students':retrieved.students,
        'nonTeachingStaff':retrieved.nonTeachingStaff,
        'correspondentName':retrieved.correspondentName,
        'correspondentPhoneNumber':retrieved.correspondentPhoneNumber,

        },
        "schoolprofilepage3":{
        'principalName':retrieved.principalName,
        'principalEmail':retrieved.principalEmail,
        'principalPhoneNumber':retrieved.principalPhoneNumber,
        'officialPhoneNumber':retrieved.officialPhoneNumber,
        },
        "schoolprofilepage4":{
        'governmentRecognized':retrieved.governmentRecognized,
        'affiliatedBoard':retrieved.affiliatedBoard,
        'affiliationNumber':retrieved.affiliationNumber,
        'affiliationYear':retrieved.affiliationYear,
        'affiliationCondition':retrieved.affiliationCondition,
        'stateAffiliationCondition':retrieved.stateAffiliationCondition,
        'statusCertificate':retrieved.statusCertificate,
        'hindhu':retrieved.hindhu,
        'cristian':retrieved.cristian,
        'islam':retrieved.islam,
        'others':retrieved.others,
        'nonBelievers':retrieved.nonBelievers,
        'fireCertificate':retrieved.fireCertificate,
        'sanitationCertificate':retrieved.sanitationCertificate,
        'buildingCertificate':retrieved.buildingCertificate,
        },
        "schoolprofilepage5":{
        'schoolOwnedBy':retrieved.schoolOwnedBy,
        'trustName':retrieved.trustName,
        'trustRegistered':retrieved.trustRegistered,
        'underAct':retrieved.underAct,
        'registrationYear':retrieved.registrationYear,
        'registrationNumber':retrieved.registrationNumber,
        'registrationValidity':retrieved.registrationValidity,
        'chairmanName':retrieved.chairmanName,
        'designation':retrieved.designation,
        'chairmainAddress':retrieved.chairmainAddress,
        'chairmanPhoneNumber':retrieved.chairmanPhoneNumber,
        'chairmanEmail':retrieved.chairmanEmail,
        },
        "schoolprofilepage6":{
        'governingBody':retrieved.governingBody,
        'trustMember':retrieved.trustMember,
        'tenureMember':retrieved.tenureMember,
        'epcc':retrieved.epcc,
        'epccMember':retrieved.epccMember,
        'epccTenureMember':retrieved.epccTenureMember,
        'parentTeacherAssociation':retrieved.parentTeacherAssociation,
        'parentTeacherAssociationMember':retrieved.parentTeacherAssociationMember,
        'parentTeacherTenureMember':retrieved.parentTeacherTenureMember,
        },
        "schoolprofilepage7":{
        'studentCouncil':retrieved.studentCouncil,
        'studentCouncilMembers':retrieved.studentCouncilMembers,
        'studentCouncilTenureMember':retrieved.studentCouncilTenureMember,
        'generalGrievance':retrieved.generalGrievance,
        'schoolCommittee':retrieved.schoolCommittee,
        'committeeCondition':retrieved.committeeCondition,
        'committeeConditionMembers':retrieved.committeeConditionMembers,
        'committeeTenureMember':retrieved.committeeTenureMember,
        },
        "schoolprofilepage8":{
        'schoolBuilding':retrieved.schoolBuilding,
        'campusArea':retrieved.campusArea,
        'builtArea':retrieved.builtArea,
        'playArea':retrieved.playArea,
        'numberOfBuilding':retrieved.numberOfBuilding,
        'provisions':retrieved.provisions,
        'staircasesNumber':retrieved.staircasesNumber,
        'liftNumber':retrieved.liftNumber,
        },
        "schoolprofilepage9":{
        'classRooms':retrieved.classRooms,
        'staffrooms':retrieved.staffrooms,
        'physicsLab':retrieved.physicsLab,
        'chemistrylab':retrieved.chemistrylab,
        'biologylab':retrieved.biologylab,
        'mathslab':retrieved.mathslab,
        'computerscienceLab':retrieved.computerscienceLab,
        'languageLab':retrieved.languageLab,
        'homescienceLab':retrieved.homescienceLab,
        'library':retrieved.library,
        'auditorium':retrieved.auditorium,
        'counselorroom':retrieved.counselorroom,
        'parlor':retrieved.parlor,
        'chapel':retrieved.chapel,
        'sickroom':retrieved.sickroom,
        'canteen':retrieved.canteen,
        'securityroom':retrieved.securityroom,
        'otherroom':retrieved.otherroom,
        'staffToilet':retrieved.staffToilet,
        'studenttoilet':retrieved.studenttoilet,
        'rooms':retrieved.rooms,
        'specialStudent':retrieved.specialStudent,
        },
        "schoolprofilepage10":{
        'wall':retrieved.wall,
        'wallCondition':retrieved.wallCondition,
        'cctv':retrieved.cctv,
        'datasaved':retrieved.datasaved,
        'cameraCount':retrieved.cameraCount,
        'maleguard':retrieved.maleguard,
        'maleGuardCount':retrieved.maleGuardCount,
        'femaleguard':retrieved.femaleguard,
        'femaleguardCount':retrieved.femaleguardCount,
        'water':retrieved.water,
        'drainage':retrieved.drainage,
        },
        "schoolprofilepage11":{
        'middayMeal':retrieved.middayMeal,
        'ownedBuses':retrieved.ownedBuses,
        'gps':retrieved.gps,
        'ladyAttendance':retrieved.ladyAttendance,
        'firstaid':retrieved.firstaid,
        'drinkingWater':retrieved.drinkingWater,
        'subcontracted':retrieved.subcontracted,
        'buspass':retrieved.buspass,
        'freeTransport':retrieved.freeTransport,
        },
        "schoolprofilepage12":{
        'malePrincipal':retrieved.malePrincipal,
        'femalePrincipal':retrieved.femalePrincipal,
        'temporaryMalePrincipal':retrieved.temporaryMalePrincipal,
        'temporaryFemalePrincipal':retrieved.temporaryFemalePrincipal,
      
      
        'maleViceprincipal':retrieved.maleViceprincipal,
        'femaleViceprincipal':retrieved.femaleViceprincipal,
        'temporaryMaleViceprincipal':retrieved.temporaryMaleViceprincipal,
        'temporaryFemaleViceprincipal':retrieved.temporaryFemaleViceprincipal,
         
        'postgraduateTeachers':retrieved.postgraduateTeachers,
        'postgraduateFemaleTeachers':retrieved.postgraduateFemaleTeachers,
        'temporaypgmaleStaff':retrieved.temporaypgmaleStaff,
        'temporaypgFemaleStaff':retrieved.temporaypgFemaleStaff,
       
        'tgMaleStaff':retrieved.tgMaleStaff,
        'tgFemaleStaff':retrieved.tgFemaleStaff,
        'temporarytgFemaleStaff':retrieved.temporarytgFemaleStaff,
        'temporarytgMaleStaff':retrieved.temporarytgMaleStaff,
        
        'untrainMalestaff':retrieved.untrainMalestaff,
        'untrainFemalestaff':retrieved.untrainFemalestaff,
        'untrainedTemporaryMale':retrieved.untrainedTemporaryMale,
        'untrainedTemporaryFemale':retrieved.untrainedTemporaryFemale,
      
        'primaryMaleStaff':retrieved.primaryMaleStaff,
        'primaryFemaleStaff':retrieved.primaryFemaleStaff,
        'temporaryPrimarymale':retrieved.temporaryPrimarymale,
        'temporaryPrimaryfemale':retrieved.temporaryPrimaryfemale,
        
        'nurseryMaleStaff':retrieved.nurseryMaleStaff,
        'nurseryFemaleStaff':retrieved.nurseryFemaleStaff,
        'ntTemporaryMale':retrieved.ntTemporaryMale,
        'ntTemporaryFemale':retrieved.ntTemporaryFemale,
       
        
        'MaleLibraian':retrieved.MaleLibraian,
        'FemaleLibraian':retrieved.FemaleLibraian,
        'temporaryMaleLibrarian':retrieved.temporaryMaleLibrarian,
        'temporaryFemaleLibrarian':retrieved.temporaryFemaleLibrarian,
       
        'artMaleStaff':retrieved.artMaleStaff,
        'artFemaleStaff':retrieved.artFemaleStaff,
        'artTemporaryMalestaff':retrieved.artTemporaryMalestaff,
        'artTemporaryFemalestaff':retrieved.artTemporaryFemalestaff,
       
        'maleCounseller':retrieved.maleCounseller,
        'femaleCounseller':retrieved.femaleCounseller,
        'temporaryMaleCounseller':retrieved.temporaryMaleCounseller,
        'temporaryFemaleCounseller':retrieved.temporaryFemaleCounseller,
        
        'MaleComputerLiteracy':retrieved.MaleComputerLiteracy,
        'FemaleComputerLiteracy':retrieved.FemaleComputerLiteracy,
        'temporaryMaleComputerLiteracy':retrieved.temporaryMaleComputerLiteracy,
        'temporaryFemaleComputerLiteracy':retrieved.temporaryFemaleComputerLiteracy,
       
        'MaleFaithminister':retrieved.MaleFaithminister,
        'FemaleFaithminister':retrieved.FemaleFaithminister,
        'temporaryMaleFaithminister':retrieved.temporaryMaleFaithminister,
        'temporaryFemaleFaithminister':retrieved.temporaryFemaleFaithminister,
       
        'maleNurse':retrieved.maleNurse,
        'femaleNurse':retrieved.femaleNurse,
        'temporaryMalenurse':retrieved.temporaryMalenurse,
        'temporaryFemalenurse':retrieved.temporaryFemalenurse,
      
        'malePtTeacher':retrieved.malePtTeacher,
        'femalePtTeacher':retrieved.femalePtTeacher,
        'temporaryMalept':retrieved.temporaryMalept,
        'temporaryFemalept':retrieved.temporaryFemalept,
        },
        "schoolprofilepage13":{
        'permanentofficeManager':retrieved.permanentofficeManager,
        'temporaryofficeManager':retrieved.temporaryofficeManager,
        'partimeofficeManager':retrieved.partimeofficeManager,
    
        'permanentOfficialAssitent':retrieved.permanentOfficialAssitent,
        'temporaryOfficialAssitent':retrieved.temporaryOfficialAssitent,
        'partimeOfficialAssitent':retrieved.partimeOfficialAssitent,
   
        'permanentClerk':retrieved.permanentClerk,
        'temporaryClerk':retrieved.temporaryClerk,
        'partimeClerk':retrieved.partimeClerk,
       
        'permanentLabAttendants':retrieved.permanentLabAttendants,
        'temporaryLabAttendants':retrieved.temporaryLabAttendants,
        'partimeLabAttendants':retrieved.partimeLabAttendants,
       
        'permanentAccountant':retrieved.permanentAccountant,
        'temporaryAccountant':retrieved.temporaryAccountant,
        'partimeAccountant':retrieved.partimeAccountant,
       
        'permanentPeon':retrieved.permanentPeon,
        'temporaryPeon':retrieved.temporaryPeon,
        'partimePeon':retrieved.partimePeon,
       
        'temporaryOthers':retrieved.temporaryOthers,
        'permanentOthers':retrieved.permanentOthers,
        'partimeOthers':retrieved.partimeOthers,
        },
        "schoolprofilepage14":{
        'curricularActivities':retrieved.curricularActivities,
        'groups':retrieved.groups,
        'communityCount':retrieved.communityCount,
    
        'lastyearSchoolLevel':retrieved.lastyearSchoolLevel,
        'lastyearZonalLevel':retrieved.lastyearZonalLevel,
        'lastyearDistrictLevel':retrieved.lastyearDistrictLevel,
        'lastyearNationalLevel':retrieved.lastyearNationalLevel,
        'lastyearInternationalLevel':retrieved.lastyearInternationalLevel,
        'lastyearStateLevel':retrieved.lastyearStateLevel,
    
        'schoolLevelCompetitions':retrieved.schoolLevelCompetitions,
        'zonalLevelCompetitions':retrieved.zonalLevelCompetitions,
        'districtLevelCompetitions':retrieved.districtLevelCompetitions,
        'nationalLevelCompetitions':retrieved.nationalLevelCompetitions,
        'stateLevelCompetitions':retrieved.stateLevelCompetitions,
        'internationalLevelCompetitions':retrieved.internationalLevelCompetitions,
    
        'schoolLevelProgrammes':retrieved.schoolLevelProgrammes,
        'schoolLevelProgrammes':retrieved.schoolLevelProgrammes,
        'zonalLevelProgrammes':retrieved.zonalLevelProgrammes,
        'nationalLevelProgrammes':retrieved.nationalLevelProgrammes,
        'stateLevelProgrammes':retrieved.stateLevelProgrammes,
        'districtLevelProgrammes':retrieved.districtLevelProgrammes,
        'internationalLevelProgrammes':retrieved.internationalLevelProgrammes,
        },
        "schoolprofilepage15":{
       'academicYearBegins':retrieved.academicYearBegins,
      'academicYearEnds':retrieved.academicYearEnds,

      'workingdays21':retrieved.workingdays21,
      'workingdays20':retrieved.workingdays20,
      'workingdays19':retrieved.workingdays19,

      'hours21':retrieved.hours21,
      'hours20':retrieved.hours20,
      'hours19':retrieved.hours19,

      'instructionalHours21':retrieved.instructionalHours21,
      'instructionalHours20':retrieved.instructionalHours20,
      'instructionalHours19':retrieved.instructionalHours19,

      'noninstructionalHours21':retrieved.noninstructionalHours21,
      'noninstructionalHours20':retrieved.noninstructionalHours20,
      'noninstructionalHours19':retrieved.noninstructionalHours19,
      
      'holidays21':retrieved.holidays21,
      'holidays20':retrieved.holidays20,
      'holidays19':retrieved.holidays19,
        },
       
        "schoolprofilepage16":{
       'subjectPerWeek':retrieved.subjectPerWeek,
      'morelPerWeek':retrieved.morelPerWeek,
      'teachingDuration':retrieved.teachingDuration,
      'clubsCount':retrieved.clubsCount,
      'timeInSummer':retrieved.timeInSummer,
      'totimeInSummer':retrieved.totimeInSummer,
      'timeInWinter':retrieved.timeInWinter,
      'totimeInWinter':retrieved.totimeInWinter,
      'shifts':retrieved.shifts,
        },

    }
# For posting the general information


@router.post('/general/')
def gen(post:dict,db:Session=Depends(database.get_db),user=Depends(oauth2.get_current_user)):
    print(post)
    print("works")
    data=db.query(schoolprofilemodel.General).filter(schoolprofilemodel.General.username==user.username).first()
    print(data.username)
    if data :
       return {"update":"true"}
    else:
        new_post=schoolprofilemodel.General(username=user.username,**post)
        db.add(new_post)
        db.commit()
        db.refresh(new_post)
        return{"successful"}


@router.put("/schoolprofile_update")
def updated(post:dict,db:Session=Depends(database.get_db),user=Depends(oauth2.get_current_user)):
    print("hii")
    updated_post=db.query(schoolprofilemodel.General).filter(schoolprofilemodel.General.username==user.username)
    up=updated_post.first()
    new=updated_post.update(post,synchronize_session=False)
    db.commit()
    return {"updated"} 