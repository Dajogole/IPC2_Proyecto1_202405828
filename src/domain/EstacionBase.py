class EstacionBase:
    def __init__(self, id_, nombre):
        self.__id = id_
        self.__nombre = nombre

    def get_id(self): return self.__id
    def get_nombre(self): return self.__nombre
    def set_nombre(self, n): self.__nombre = n
