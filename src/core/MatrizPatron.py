from src.core.MatrizBase import MatrizBase

class MatrizPatron(MatrizBase):
    @staticmethod
    def desde(F):
        P = MatrizPatron(F.filas(), F.cols())
        for i in range(F.filas()):
            fila = F.fila(i)
            j = 0
            for val in fila:
                P.set(i, j, 1 if (val > 0) else 0)
                j += 1
        return P

    def fila_igual(self, i, otra, j):
       
        if self.cols() != otra.cols(): return False
        for c in range(self.cols()):
            if self.get(i, c) != otra.get(j, c):
                return False
        return True
