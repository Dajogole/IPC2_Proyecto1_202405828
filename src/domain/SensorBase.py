from src.tda.Lista import Lista

class SensorBase:
    def __init__(self, id_, nombre):
        self.__id = id_
        self.__nombre = nombre
        self.__frecuencias = Lista()  

    def get_id(self): return self.__id
    def get_nombre(self): return self.__nombre
    def set_nombre(self, n): self.__nombre = n
    def frecuencias(self): return self.__frecuencias

    def add_frecuencia(self, frec):
        self.__frecuencias.append(frec)
