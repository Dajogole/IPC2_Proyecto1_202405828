from src.core.MatrizBase import MatrizBase

class MatrizFrecuencia(MatrizBase):
    @staticmethod
    def construir_para_suelo(campo):
        n = campo.estaciones().length()
        s = campo.sensores_s().length()
        F = MatrizFrecuencia(n, s)
        
        est_ids = []
        
        from src.tda.Lista import Lista
        est_lista_ids = Lista()
        for est in campo.estaciones():
            est_lista_ids.append(est.get_id())

        si = 0
        for sensor in campo.sensores_s():
          
            for frec in sensor.frecuencias():
                fila_index, _ = est_lista_ids.find(lambda eid: eid == frec.get_id_estacion())
                if fila_index >= 0:
                    F.set(fila_index, si, frec.get_valor())
            si += 1
        return F

    @staticmethod
    def construir_para_cultivo(campo):
        n = campo.estaciones().length()
        t = campo.sensores_t().length()
        F = MatrizFrecuencia(n, t)
        from src.tda.Lista import Lista
        est_lista_ids = Lista()
        for est in campo.estaciones():
            est_lista_ids.append(est.get_id())
        ti = 0
        for sensor in campo.sensores_t():
            for frec in sensor.frecuencias():
                fila_index, _ = est_lista_ids.find(lambda eid: eid == frec.get_id_estacion())
                if fila_index >= 0:
                    F.set(fila_index, ti, frec.get_valor())
            ti += 1
        return F
