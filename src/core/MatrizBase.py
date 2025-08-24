from src.tda.Lista import Lista

class MatrizBase:
    def __init__(self, filas, cols):
        self._filas = filas
        self._cols = cols
        self._data = Lista()  
        for _ in range(filas):
            fila = Lista()
            for _ in range(cols):
                fila.append(0)
            self._data.append(fila)

    def filas(self): return self._filas
    def cols(self): return self._cols

    def get(self, i, j):
        return self._data.get(i).get(j)

    def set(self, i, j, val):
        self._data.get(i).set(j, val)

    def fila(self, i):
        return self._data.get(i)
