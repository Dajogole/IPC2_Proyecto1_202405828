from src.core.MatrizBase import MatrizBase
from src.tda.Lista import Lista

class MatrizReducida(MatrizBase):
   
    @staticmethod
    def desde(F, grupos):
        r = grupos.length()
        R = MatrizReducida(r, F.cols())
        gi = 0
        for grupo in grupos:
            for c in range(F.cols()):
                suma = 0
                for idx in grupo.indices():
                    suma += F.get(idx, c)
                R.set(gi, c, suma)
            gi += 1
        return R

class EtiquetadorReduccion:
   
    @staticmethod
    def etiquetar(estaciones_lista, grupos):
        nombres_reducidos = Lista()  
        ids_reducidos = Lista()      
        mapping = Lista()            

        gi = 0
        for grupo in grupos:
       
            nombre_concat = ""
            id_nuevo = None
            originales = Lista()
            first = True
            for idx in grupo.indices():
                est = estaciones_lista.get(idx)
                if first:
                    id_nuevo = est.get_id()
                    nombre_concat = est.get_nombre()
                    first = False
                else:
                    nombre_concat += ", " + est.get_nombre()
                originales.append(est.get_id())
            nombres_reducidos.append(nombre_concat)
            ids_reducidos.append(id_nuevo)
            mapping.append((id_nuevo, originales))  
            gi += 1
        return ids_reducidos, nombres_reducidos, mapping
