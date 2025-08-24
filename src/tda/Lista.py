from src.tda.Nodo import Nodo

class Lista:
    def __init__(self):
        self._cabeza = None
        self._tam = 0

    def is_empty(self):
        return self._cabeza is None

    def length(self):
        return self._tam

    def append(self, valor):
        nuevo = Nodo(valor)
        if self._cabeza is None:
            self._cabeza = nuevo
        else:
            actual = self._cabeza
            while actual.get_siguiente() is not None:
                actual = actual.get_siguiente()
            actual.set_siguiente(nuevo)
        self._tam += 1
        return self

    def insert_at(self, index, valor):
        if index < 0 or index > self._tam:
            raise IndexError("Índice fuera de rango")
        nuevo = Nodo(valor)
        if index == 0:
            nuevo.set_siguiente(self._cabeza)
            self._cabeza = nuevo
        else:
            prev = self._nodo_en(index - 1)
            nuevo.set_siguiente(prev.get_siguiente())
            prev.set_siguiente(nuevo)
        self._tam += 1
        return self

    def get(self, index):
        return self._nodo_en(index).get_valor()

    def set(self, index, valor):
        self._nodo_en(index).set_valor(valor)

    def find(self, predicate):
        i = 0
        actual = self._cabeza
        while actual is not None:
            if predicate(actual.get_valor()):
                return i, actual.get_valor()
            actual = actual.get_siguiente()
            i += 1
        return -1, None

    def clear(self):
        self._cabeza = None
        self._tam = 0

    def _nodo_en(self, index):
        if index < 0 or index >= self._tam:
            raise IndexError("Índice fuera de rango")
        actual = self._cabeza
        i = 0
        while i < index:
            actual = actual.get_siguiente()
            i += 1
        return actual

    def __iter__(self):
        actual = self._cabeza
        while actual is not None:
            yield actual.get_valor()
            actual = actual.get_siguiente()
