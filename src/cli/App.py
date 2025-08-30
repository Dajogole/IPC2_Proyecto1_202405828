import os
from src.cli.Menu import mostrar_menu
from src.io.ParserXML import ParserXML
from src.io.WriterXML import WriterXML
from src.core.MatrizFrecuencia import MatrizFrecuencia
from src.core.MatrizPatron import MatrizPatron
from src.core.Agrupador import Agrupador
from src.core.MatrizReducida import MatrizReducida, EtiquetadorReduccion
from src.viz.GraphvizRenderer import GraphvizRenderer
from src.utils.Mensajes import info, error

class StudentInfo:
    def __init__(self):
        self.carnet = "202405828"
        self.nombre = "Danny Josué González Lémus"
        self.curso = "Introducción a la Programación y Computación 2"
        self.seccion = "Sección C"
        self.semestre = "4to. Semestre"
        self.doc = "https://github.com/Dajogole/IPC2_Proyecto1_202405828/tree/main/Documentaci%C3%B3n"

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
        self.arte = {}  

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
                elif op == "2":
                    if self.campos is None or self.campos.length()==0:
                        info("Cargue primero un archivo.")
                        continue
                    
                    campo = self.campos.get(0)
                    info("Procesando campo: " + campo.get_nombre())
                    self.Fs = MatrizFrecuencia.construir_para_suelo(campo)
                    self.Ft = MatrizFrecuencia.construir_para_cultivo(campo)
                    self.Fps = MatrizPatron.desde(self.Fs)
                    self.Fpt = MatrizPatron.desde(self.Ft)
                    self.grupos = Agrupador.agrupar(self.Fps, self.Fpt)
                    self.ids_reduc, self.nombres_reduc, self.mapping = EtiquetadorReduccion.etiquetar(campo.estaciones(), self.grupos)
                    self.Frs = MatrizReducida.desde(self.Fs, self.grupos)
                    self.Frt = MatrizReducida.desde(self.Ft, self.grupos)
                    info("Proceso completado.")
                elif op == "3":
                    if not hasattr(self, "Frs"):
                        info("Procese primero el archivo (opción 2).")
                        continue
                    out = input(" Opción generar archivo de salida\n Ingrese la ruta+nombre del archivo: ").strip()
                    campo = self.campos.get(0)
                    writer.escribir(out, campo, self.ids_reduc, self.nombres_reduc, self.Frs, self.Frt)
                    info("Archivo de salida creado.")
                elif op == "4":
                    StudentInfo().mostrar()
                elif op == "5":
                    if not hasattr(self, "Fs"):
                        info("Procese primero el archivo (opción 2).")
                        continue
                    campo = self.campos.get(0)
                    tipo = input(" Graficar [F|Fp|Fr]: ").strip().upper()
                    if tipo=="F": renderer.graficar_F(campo, self.Fs, self.Ft)
                    elif tipo=="FP": renderer.graficar_Fp(campo, self.Fps, self.Fpt)
                    elif tipo=="FR": renderer.graficar_Fr(campo, self.ids_reduc, self.Frs, self.Frt)
                    else: info("Tipo inválido.")
                elif op == "6":
                    break
                else:
                    info("Opción inválida.")
            except Exception as ex:
                error(str(ex))

if __name__ == "__main__":
    App().run()
