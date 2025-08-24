import xml.etree.ElementTree as ET
from src.tda.Lista import Lista
from src.domain.CampoAgricola import CampoAgricola
from src.domain.EstacionBase import EstacionBase
from src.domain.SensorSuelo import SensorSuelo
from src.domain.SensorCultivo import SensorCultivo
from src.domain.Frecuencia import Frecuencia
from src.utils.Mensajes import info, warn

class ParserXML:
    def __init__(self): pass

    def leer(self, ruta_archivo):
        info("Leyendo XML: " + ruta_archivo)
        tree = ET.parse(ruta_archivo)
        root = tree.getroot()
        campos = Lista()

        for campo_el in root.findall("campo"):
            cid = campo_el.get("id")
            cname = campo_el.get("nombre")
            info(f"➢ Cargando campo agricola {cid}")
            campo = CampoAgricola(cid, cname)

            ests_el = campo_el.find("estacionesBase")
            if ests_el is None: warn("Campo sin estacionesBase")
            else:
                for e in ests_el.findall("estacion"):
                    eid = e.get("id"); ename = e.get("nombre")
                    info(f"➢ Creando estación base {eid}")
                    campo.estaciones().append(EstacionBase(eid, ename))

            ss_el = campo_el.find("sensoresSuelo")
            if ss_el is not None:
                for s in ss_el.findall("sensorS"):
                    sid = s.get("id"); sname = s.get("nombre")
                    sensor = SensorSuelo(sid, sname)
                    for f in s.findall("frecuencia"):
                        sensor.add_frecuencia(Frecuencia(f.get("idEstacion"), f.text.strip()))
                    campo.sensores_s().append(sensor)

            st_el = campo_el.find("sensoresCultivo")
            if st_el is not None:
                for t in st_el.findall("sensorT"):
                    tid = t.get("id"); tname = t.get("nombre")
                    sensor = SensorCultivo(tid, tname)
                    for f in t.findall("frecuencia"):
                        sensor.add_frecuencia(Frecuencia(f.get("idEstacion"), f.text.strip()))
                    campo.sensores_t().append(sensor)

            campos.append(campo)
        return campos
