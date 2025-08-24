class Nodo:
    __slots__ = ("_valor", "_siguiente")

    def __init__(self, valor):
        self._valor = valor
        self._siguiente = None

    def get_valor(self):
        return self._valor

    def set_valor(self, v):
        self._valor = v

    def get_siguiente(self):
        return self._siguiente

    def set_siguiente(self, n):
        self._siguiente = n
