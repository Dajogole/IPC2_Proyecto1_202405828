import xml.etree.ElementTree as ET
from xml.dom import minidom
from src.utils.Mensajes import info

class WriterXML:
    def __init__(self): pass

    def escribir_multi(self, ruta_archivo, resultados_lista):
        info("Escribiendo XML salida (todos los campos): " + ruta_archivo)
        root = ET.Element("camposAgricolas")

        i = 0
        while i < resultados_lista.length():
            res = resultados_lista.get(i)
            campo = res.campo()

            campo_el = ET.SubElement(root, "campo", {"id": campo.get_id(), "nombre": campo.get_nombre()})

           
            ebr = ET.SubElement(campo_el, "estacionesBaseReducidas")
            gi = 0
            while gi < res.ids_reduc().length():
                eid = res.ids_reduc().get(gi)
                ename = res.nombres_reduc().get(gi)
                ET.SubElement(ebr, "estacion", {"id": eid, "nombre": ename})
                gi += 1

    
            ss_el = ET.SubElement(campo_el, "sensoresSuelo")
            si = 0
            while si < res.Frs().cols():
                sensor = campo.sensores_s().get(si)
                s_el = ET.SubElement(ss_el, "sensorS", {"id": sensor.get_id(), "nombre": sensor.get_nombre()})
                gi = 0
                while gi < res.Frs().filas():
                    val = res.Frs().get(gi, si)
                    if val > 0:
                        ET.SubElement(s_el, "frecuencia", {"idEstacion": res.ids_reduc().get(gi)}).text = str(val)
                    gi += 1
                si += 1

            
            st_el = ET.SubElement(campo_el, "sensoresCultivo")
            ti = 0
            while ti < res.Frt().cols():
                sensor = campo.sensores_t().get(ti)
                t_el = ET.SubElement(st_el, "sensorT", {"id": sensor.get_id(), "nombre": sensor.get_nombre()})
                gi = 0
                while gi < res.Frt().filas():
                    val = res.Frt().get(gi, ti)
                    if val > 0:
                        ET.SubElement(t_el, "frecuencia", {"idEstacion": res.ids_reduc().get(gi)}).text = str(val)
                    gi += 1
                ti += 1

            i += 1

        xml_str = minidom.parseString(ET.tostring(root)).toprettyxml(indent="  ", encoding="utf-8")
        with open(ruta_archivo, "wb") as f:
            f.write(xml_str)

    def escribir(self, ruta_archivo, campo, ids_reduc, nombres_reduc, FrS, FrT):
        info("Escribiendo XML salida: " + ruta_archivo)
        root = ET.Element("camposAgricolas")
        campo_el = ET.SubElement(root, "campo", {"id": campo.get_id(), "nombre": campo.get_nombre()})

        
        ebr = ET.SubElement(campo_el, "estacionesBaseReducidas")
        gi = 0
        for _ in ids_reduc:
            eid = ids_reduc.get(gi)
            ename = nombres_reduc.get(gi)
            ET.SubElement(ebr, "estacion", {"id": eid, "nombre": ename})
            gi += 1

      
        ss_el = ET.SubElement(campo_el, "sensoresSuelo")
        si = 0
        for sensor in campo.sensores_s():
            s_el = ET.SubElement(ss_el, "sensorS", {"id": sensor.get_id(), "nombre": sensor.get_nombre()})
            gi = 0
            while gi < FrS.filas():
                val = FrS.get(gi, si)
                if val > 0:
                    ET.SubElement(s_el, "frecuencia", {"idEstacion": ids_reduc.get(gi)}).text = str(val)
                gi += 1
            si += 1


        st_el = ET.SubElement(campo_el, "sensoresCultivo")
        ti = 0
        for sensor in campo.sensores_t():
            t_el = ET.SubElement(st_el, "sensorT", {"id": sensor.get_id(), "nombre": sensor.get_nombre()})
            gi = 0
            while gi < FrT.filas():
                val = FrT.get(gi, ti)
                if val > 0:
                    ET.SubElement(t_el, "frecuencia", {"idEstacion": ids_reduc.get(gi)}).text = str(val)
                gi += 1
            ti += 1

        xml_str = minidom.parseString(ET.tostring(root)).toprettyxml(indent="  ", encoding="utf-8")
        with open(ruta_archivo, "wb") as f:
            f.write(xml_str)
