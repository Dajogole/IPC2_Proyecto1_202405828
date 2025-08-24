from src.tda.Lista import Lista

class Grupo:
    def __init__(self):
        self.__indices = Lista()  
    def indices(self): return self.__indices

class Agrupador:
    
    @staticmethod
    def agrupar(FpS, FpT):
        n = FpS.filas()
        grupos = Lista()  
        asignado = Lista() 
        for _ in range(n): asignado.append(0)

        for i in range(n):
            if asignado.get(i) == 1: continue
            g = Grupo()
            g.indices().append(i)
            asignado.set(i, 1)
            # buscar iguales a i
            for j in range(i+1, n):
                if asignado.get(j) == 1: continue
                igualesS = True
                for c in range(FpS.cols()):
                    if FpS.get(i,c) != FpS.get(j,c):
                        igualesS = False; break
                if not igualesS: continue
                igualesT = True
                for c in range(FpT.cols()):
                    if FpT.get(i,c) != FpT.get(j,c):
                        igualesT = False; break
                if igualesT:
                    g.indices().append(j)
                    asignado.set(j, 1)
            grupos.append(g)
        return grupos  
