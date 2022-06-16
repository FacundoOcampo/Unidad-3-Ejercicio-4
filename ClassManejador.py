import csv

import numpy as np
from ClaseCalefactor import Calefactor
from ClaseCalefactorElectrico import CalefactorE
from ClaseCalefactorGas import CalefactorG

class Man:
    __Arr=None
    __Dim=0
    __Inc=1
    __Cant=0
    def __init__(self,Dim):
        self.__Dim=Dim
        self.__Arr=np.empty(self.__Dim,dtype=Calefactor)
    def CargarE(self):
        Archivo=open("CalefactoresElectrico.csv","r",encoding="utf-8")
        Reader=csv.reader(Archivo,delimiter=";")
        Band=True
        for fila in Reader:
            if(Band==True):
                Band=False
            else:
                if self.__Cant<self.__Dim:
                    NuevoC=CalefactorE(fila[0],fila[1],int(fila[2]))
                    self.__Arr[self.__Cant]=NuevoC
                    self.__Cant=self.__Cant+1
        Archivo.close()

    def CargarG(self):
        Archivo=open("CalefactoresAGas.csv","r",encoding="utf-8")
        Reader=csv.reader(Archivo,delimiter=";")
        Band=True
        for fila in Reader:
            if(Band==True):
                Band=False
            else:
                if self.__Cant<self.__Dim:
                    NuevoC=CalefactorG(fila[0],fila[1],fila[2],int(fila[3]))
                    self.__Arr[self.__Cant]=NuevoC
                    self.__Cant=self.__Cant+1
        Archivo.close()

    def MostrarG(self,Cost,Cant):
        Min=9999999999999
        Aux=None
        Total=None
        for fila in self.__Arr:
            if type(fila)==CalefactorG:
                Total=float((fila.GetCal()/1000)*Cant*Cost)
                if Total < Min:
                    Min=Total
                    Aux=fila
        Aux.AgregarConsumo(Total)
        print("Calefactor con menor consumo({}):\n       {} ".format(Total,Aux))
        return Total

    def MostrarE(self,Cost,Cant):
        Min=9999999999999
        Aux=None
        Total=None
        for fila in self.__Arr:
            if type(fila)==CalefactorE:
                Total=float((fila.GetPot()/1000)*Cant*Cost)
                if Total < Min:
                    Min=Total
                    Aux=fila
        Aux.AgregarConsumo(Total)
        print("Calefactor con menor consumo({}):\n       {} ".format(Total,Aux))
        return Total
    def MostrarMenor(self,CG,CE):
        Aux=None
        if CG<CE:
            Aux=CG
        elif CE<CG:
            Aux=CE
        else:
            print("Error")
        for fila in self.__Arr:
            if Aux==fila.GetConsumo():
                if type(fila)==CalefactorE:
                    print("Calefactor Electrico {}".format(fila))
                elif type(fila)==CalefactorG:
                    print("Calefactor a Gas \n {}".format(fila))
