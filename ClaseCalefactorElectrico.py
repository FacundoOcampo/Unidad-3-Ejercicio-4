from ClaseCalefactor import Calefactor
class CalefactorE(Calefactor):
    __PotenciaMax=None
    def __init__(self,Marca,Modelo,Potencia):
        super().__init__(Marca,Modelo)
        self.__PotenciaMax=Potencia
    def GetPot(self):
        return self.__PotenciaMax
    def __str__(self):
        return "{} Potencia:{}".format(self.Listar(),self.__PotenciaMax)
