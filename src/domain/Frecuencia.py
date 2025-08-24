class Frecuencia:
    def __init__(self, id_estacion, valor):
        self.__id_estacion = id_estacion
        self.__valor = int(valor)

    def get_id_estacion(self): return self.__id_estacion
    def get_valor(self): return self.__valor
    def set_valor(self, v): self.__valor = int(v)
