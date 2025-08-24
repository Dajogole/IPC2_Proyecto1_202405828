from src.tda.Lista import Lista

class CampoAgricola:
    def __init__(self, id_, nombre):
        self.__id = id_
        self.__nombre = nombre
        self.__estaciones = Lista()
        self.__sensores_s = Lista()
        self.__sensores_t = Lista()

    def get_id(self): return self.__id
    def get_nombre(self): return self.__nombre
    def set_nombre(self, n): self.__nombre = n

    def estaciones(self): return self.__estaciones
    def sensores_s(self): return self.__sensores_s
    def sensores_t(self): return self.__sensores_t
