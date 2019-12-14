'''


Created on Dec 3, 2019

@author: robertohg
'''
import pandas as pd
import numpy as np
import csv


class Patient:
    
    def __init__(self,pName,pLastName,pIDEnsurance,pID,pDOB,pAddress):
        self._pName = ""
        self._pLastName = ""
        self._pIDEnsurance = ""
        self._pID = ""
        self._pDOB = ""
        self._pAddress = ""

    def setPatientName(self,Name):
        self.pName = Name
    def setPatientLastName(self,LastName):
        self.pLastName = LastName
    def setPatientEnsurance(self,Ensurance):
        self.pIDEnsurance = Ensurance
    def setPatientID(self,ID):
        self.pID = ID
    def setPatientDOB(self,DOB):
        self.pDOB = DOB
    def setPatientAddress(self,Address):
        self.pAddress = Address


    
class Room:
    
    patient = Patient("","","","","","")
    
    def __init__(self,rRoomNumber,rAdmitted,rDischarge):
        self._rRoomNumber = rRoomNumber
        self._rAdmitted = ""
        self._rDischarge = ""
    def setDischarge(self,Discharge):
        self.rDischarge = Discharge
    def SetAdmitted(self,Admitted):
        self.rAdmitted = Admitted
    def setNumber(self,roomNumber):
        self.rRoomNumber = roomNumber
    
def mergeSort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2  
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L) # izquierda
        mergeSort(R) # derecha
  
        i = j = k = 0
          
        # copiar info a array temporal
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1
          
        # revisar si falto algun elemento
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1


    

patientsdf = pd.read_csv('example.csv', header = 0)
patientsdf['Seguro'] = patientsdf['Seguro'].astype('Int64')
patientsdf['Phone'] = patientsdf['Phone'].astype('Int64')

roomsdf = pd.read_csv('Room.csv', header = 0)
roomsdf['Seguro'] = roomsdf['Seguro'].astype('Int64')

roomList = roomsdf.values.tolist()
patientList = patientsdf.values.tolist()



sortRoom = roomsdf[['Room']].to_numpy()

sortRoomT = sortRoom.transpose()


def Reporte():
    flat_list = []
    for sublist in sortRoomT:
        for item in sublist:
            flat_list.append(item)
    mergeSort(flat_list)
    print(flat_list)
    
    roomListOrder = []
    
    for i in flat_list:
        for j in roomList:
            if(i == j[0]):
                roomListOrder.append(j)
    

    
    roomOrder = pd.DataFrame(roomListOrder)
    
    roomOrder.columns = ["Room","First_Name","Last_Name","Seguro","Ingreso","Salida"]
    roomOrder['Seguro'] = roomOrder['Seguro'].astype('Int64')
    print(roomOrder)
    

def agregarPaciente():
    tmp = []
    tmp.append(input("Ingrese Numbre"))
    tmp.append(input("Ingrese Apellido"))
    tmp.append(input("Ingrese Seguro"))
    tmp.append(input("Ingrese ID"))
    tmp.append(input("Ingrese Ano de nacimiento"))
    tmp.append(input("Ingrese Direccion"))
    tmp.append(input("Ingrese Telefono"))
    patientList.append(tmp)
    
    
def Exit():
    patientListdf = pd.DataFrame(patientList)
    patientListdf.columns =["First_Name","Last_Name","Seguro","ID","Year","Address","Phone"]
    #patientListdf['Seguro'] = patientListdf['Seguro'].astype('Int64')
    #patientListdf['Phone'] = patientListdf['Phone'].astype('Int64')
    patientListdf.to_csv('example.csv', index=False)
    
    roomListdf = pd.DataFrame(roomList)
    roomListdf.columns = ["Room","First_Name","Last_Name","Seguro","Ingreso","Salida"]
    roomListdf['Seguro'] = roomListdf['Seguro'].astype('Int64')
    roomListdf.to_csv('Room.csv', index=False)



def actualizarHabitacion():
    obj = Room()
    cont = 0
    tmp = []
    hab = input("Elija habitacion a actualizar: (101-509")
    for i in roomList:
        cont += 1
        if(hab == i[0]):
            roomList.pop(cont)
            print ("""
            1.Eliminar paciente
            2.Agregar Paciente
            """)
            awns=input("Elija una opcion")
            if(awns == 1):
                tmp[0]= obj.setNumber(hab)
                tmp[1]= obj.patient.pName = ""
                tmp[2]= obj.patient.pLastName = ""
                tmp[3]= obj.patient.pIDEnsurance = ""
                tmp[4]= obj.SetAdmitted("")
                tmp[5]= obj.setDischarge("")
            else:
                tmp[0]= obj.setNumber(hab)     
                tmp[1]= input("Ingrese Nombre del paciente")     
                tmp[2]= input("Ingrese Apellido del paciente")           
                tmp[3]= input("Ingrese en Numero del Seguro")
                tmp[4]= input("Ingrese la fecha de admicion")
                tmp[5]= obj.setDischarge("")
            roomList.append(tmp)

ans=True
while ans:
    print ("""
    1.Imrpimer reporte 6 am
    2.Agregar Paciente
    3.Actualizar habitacion
    4.Exit/Quit
    """)
    ans=input("Elija una opcion") 
    if ans=="1": 
        Reporte() 
    elif ans=="2":
        agregarPaciente()
    elif ans=="3":
        actualizarHabitacion()
    elif ans=="4":
        Exit()
        break
    elif ans !="":
        print("\n Opcion invalida") 









