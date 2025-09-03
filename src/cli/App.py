
import os
from src.cli.Menu import mostrar_menu
from src.io.ParserXML import ParserXML
from src.io.WriterXML import WriterXML
from src.core.MatrizFrecuencia import MatrizFrecuencia
from src.core.MatrizPatron import MatrizPatron
from src.core.Agrupador import Agrupador
from src.core.MatrizReducida import MatrizReducida, EtiquetadorReduccion
from src.core.ResultadoCampo import ResultadoCampo
from src.viz.GraphvizRenderer import GraphvizRenderer
from src.utils.Mensajes import info, error
from src.tda.Lista import Lista

class StudentInfo:
    def __init__(self):
        self.carnet = "202405828"
        self.nombre = "Danny Josué González Lémus"
        self.curso = "Introducción a la Programación y Computación 2"
        self.seccion = "Sección C"
        self.semestre = "4to. Semestre"
        self.doc = "https://github.com/Dajogole/IPC2_Proyecto1_202405828/tree/main/Documentación"

    def mostrar(self):
        print("➢ " + self.nombre)
        print("➢ Carnet " + self.carnet)
        print("➢ " + self.curso)
        print("➢ " + self.seccion)
        print("➢ " + self.semestre)
        print("➢ " + self.doc)

class App:
    def __init__(self):
        self.campos = None         
        self.resultados = Lista()  

    def _elegir_campo_indice(self):
        if self.campos is None or self.campos.length() == 0:
            info("Cargue primero un archivo.")
            return -1
        print("Campos disponibles:")
        i = 0
        while i < self.campos.length():
            c = self.campos.get(i)
            print(f" {i}. [{c.get_id()}] {c.get_nombre()}")
            i += 1
        try:
            idx = int(input("Seleccione el índice del campo: ").strip())
            if idx < 0 or idx >= self.campos.length():
                info("Índice inválido.")
                return -1
            return idx
        except Exception:
            info("Entrada inválida.")
            return -1

    def run(self):
        parser = ParserXML()
        writer = WriterXML()
        renderer = GraphvizRenderer()
        info("Sistema de agricultura de precisión - Proyecto 1")

        while True:
            mostrar_menu()
            try:
                op = input("Seleccione opción: ").strip()

                if op == "1":  
                    ruta = input(" Opción cargar archivo\n Ingrese la ruta+nombre del archivo: ").strip()
                    self.campos = parser.leer(ruta)
                    info("Archivo cargado. Campos: " + str(self.campos.length()))
                   
                    self.resultados.clear()

                elif op == "2": 
                    if self.campos is None or self.campos.length() == 0:
                        info("Cargue primero un archivo.")
                        continue

                    self.resultados.clear()
                    i = 0
                    while i < self.campos.length():
                        campo = self.campos.get(i)
                        info("Procesando campo: " + campo.get_nombre())

                        Fs = MatrizFrecuencia.construir_para_suelo(campo)
                        Ft = MatrizFrecuencia.construir_para_cultivo(campo)
                        Fps = MatrizPatron.desde(Fs)
                        Fpt = MatrizPatron.desde(Ft)
                        grupos = Agrupador.agrupar(Fps, Fpt)
                        ids_reduc, nombres_reduc, mapping = EtiquetadorReduccion.etiquetar(campo.estaciones(), grupos)
                        Frs = MatrizReducida.desde(Fs, grupos)
                        Frt = MatrizReducida.desde(Ft, grupos)

                        self.resultados.append(
                            ResultadoCampo(campo, Fs, Ft, Fps, Fpt, grupos, ids_reduc, nombres_reduc, Frs, Frt)
                        )
                        info("✓ Campo procesado: " + campo.get_nombre())
                        i += 1

                    info("Proceso completado para todos los campos. Total procesados: " + str(self.resultados.length()))

                elif op == "3":  
                    if self.resultados.length() == 0:
                        info("Procese primero el archivo (opción 2).")
                        continue
                    out = input(" Opción generar archivo de salida\n Ingrese la ruta+nombre del archivo: ").strip()
                    writer.escribir_multi(out, self.resultados)
                    info("Archivo de salida creado: " + out)

                elif op == "4":  
                    StudentInfo().mostrar()

                elif op == "5": 
                    if self.resultados.length() == 0:
                        info("Procese primero el archivo (opción 2).")
                        continue

                    
                    idx = self._elegir_campo_indice()
                    if idx < 0:
                        continue

                    
                    tipo = input(" Graficar [F|Fp|Fr]: ").strip().upper()
                    res = self.resultados.get(idx)

                    if tipo == "F":
                        renderer.graficar_F(res.campo(), res.Fs(), res.Ft())
                    elif tipo == "FP":
                        renderer.graficar_Fp(res.campo(), res.Fps(), res.Fpt())
                    elif tipo == "FR":
                        renderer.graficar_Fr(res.campo(), res.ids_reduc(), res.Frs(), res.Frt())
                    else:
                        info("Tipo inválido. Use F, Fp o Fr.")

                elif op == "6":
                    break

                else:
                    info("Opción inválida.")

            except Exception as ex:
                error(str(ex))

if __name__ == "__main__":
    App().run()
