'''
Created on Dec 3, 2019

@author: robertohg
'''


#class Database:
    
class RoomTable:
    def __init__(self):


class Doctor:
    def __init__(self,matricula_doctor,apellido_doctor,nombre_doctor,nombre_especialidad):
        self._matricula_doctor = matricula_doctor
        self._apellido_doctor  = apellido_doctor
        self._nombre_doctor = nombre_doctor
        self._nombre_especialidad = nombre_especialidad


class Patient:
    def __init__(self,pName,pLastName,pIDType,pID,pDOB,pAddress,pPhone):
        self._pName = pName
        self._pLastName = pLastName
        self._pIDType = pIDType
        self._pID = pID
        self._pDOB = pDOB
        self._pAddress = pAddress
        self._pPhone = pPhone
        
    
class Room:
    def __init__(self,rRoomNumber,rIsEmpty,rAdmittedDate,rAdmittedHour,rPatient):
        self._rRoomNumber = rRoomNumber
        self._rIsEmpty = rIsEmpty
        self._rAdmittedDae = rAdmittedDate
        self._rAdmittedHour = rAdmittedHour
        self._rPatient = rPatient

class Rx:
    def __init__(self,rDrugName,rInstructions,rPrescriptionDate,rDosage):
        self._rDrugName = rDrugName
        self._rInstructions = rInstructions
        self.rPrescriptionDate = rPrescriptionDate
        self._rDosage = rDosage

