from ClaseCalefactor import Calefactor

class CalefactorG(Calefactor):
    __Matricula=None
    __Calorias=None
    def __init__(self,Marca,Modelo,Matricula,Calorias):
        super().__init__(Marca,Modelo)
        self.__Calorias=Calorias
        self.__Matricula=Matricula
    def GetCal(self):
        return self.__Calorias
    def __str__(self):
        return "{} Matricula:{:20} Calorias:{}".format(self.Listar(),self.__Matricula,self.__Calorias)
