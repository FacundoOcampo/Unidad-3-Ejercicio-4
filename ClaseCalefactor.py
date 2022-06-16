class Calefactor:
    __Marca=None
    __Modelo=None
    __Consumo=None
    def __init__(self,Marca,Modelo):
        self.__Marca=Marca
        self.__Modelo=Modelo
        self.__Consumo=1
    def Listar(self):
        return "Marca: {:15} Modelo:{:15}".format(self.__Marca,self.__Modelo)
    def AgregarConsumo(self,Num):
        self.__Consumo=Num
    def GetConsumo(self):
        return self.__Consumo
