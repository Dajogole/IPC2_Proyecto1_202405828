import os
from src.utils.Mensajes import info, error

class GraphvizRenderer:
    def __init__(self, out_dir="out"):
        self.out_dir = out_dir
        if not os.path.isdir(out_dir):
            os.makedirs(out_dir)

        
        self.dot = os.environ.get("DOT_BIN") or self._guess_dot()

        if not self.dot:
            error("No se encontró el binario 'dot' de Graphviz. "
                  "Instale Graphviz o defina DOT_BIN con la ruta completa.\n"
                  "Ejemplos macOS:\n"
                  "  brew install graphviz\n"
                  "  export DOT_BIN=/opt/homebrew/bin/dot   # Apple Silicon\n"
                  "  export DOT_BIN=/usr/local/bin/dot      # Intel")

    def _guess_dot(self):
        posibles = [
            "/opt/homebrew/bin/dot",  
            "/usr/local/bin/dot",     
            "/opt/local/bin/dot",   
            "/usr/bin/dot"           
        ]
        for p in posibles:
            if os.path.exists(p):
                return p
        try:
            import shutil
            w = shutil.which("dot")
            if w:
                return w
        except Exception:
            pass
        return None

    def _render_dot(self, dot_path, png_path):
       
        if not self.dot:
            msg = ("Graphviz no está disponible. Instale Graphviz y/o defina DOT_BIN.\n"
                   f"DOT esperado para renderizar: {png_path}\n"
                   "Ej.: brew install graphviz  |  export DOT_BIN=/opt/homebrew/bin/dot")
            error(msg)
            try:
                with open(png_path + ".ERROR.txt", "w", encoding="utf-8") as f:
                    f.write(msg)
            except Exception:
                pass
            return

        
        cmd = f'"{self.dot}" -Tpng "{dot_path}" -o "{png_path}"'
        rc = os.system(cmd)
        if rc != 0:
            error(f"Fallo al ejecutar: {cmd}\nCódigo de salida: {rc}")
            try:
                with open(png_path + ".ERROR.txt", "w", encoding="utf-8") as f:
                    f.write(f"Fallo al ejecutar: {cmd}\nCódigo de salida: {rc}\n")
            except Exception:
                pass
        else:
            info("Gráfica generada: " + png_path)

    def graficar_F(self, campo, Fs, Ft):
        dot = 'digraph G {\nrankdir=LR;\nnode[shape=box];\nlabel="F matrices - ' + campo.get_nombre() + '";\n'
       
        
        for i in range(Fs.filas()):
            dot += f'  "E{i}" [label="Estación {i}"];\n'
        
        
        for j in range(Fs.cols()):
            dot += f'  "Ss{j}" [shape=ellipse,label="S_suelo {j}"];\n'
       
        
        for j in range(Ft.cols()):
            dot += f'  "St{j}" [shape=ellipse,label="S_cultivo {j}"];\n'
        
      
        for i in range(Fs.filas()):
            for j in range(Fs.cols()):
                v = Fs.get(i,j)
                if v > 0:
                    dot += f'  "E{i}" -> "Ss{j}" [label="{v}"];\n'
       
      
        for i in range(Ft.filas()):
            for j in range(Ft.cols()):
                v = Ft.get(i,j)
                if v > 0:
                    dot += f'  "E{i}" -> "St{j}" [label="{v}"];\n'

        dot += "}\n"
        p = os.path.join(self.out_dir, "F.dot")
        with open(p, "w", encoding="utf-8") as f:
            f.write(dot)
        self._render_dot(p, os.path.join(self.out_dir, "F.png"))

    def graficar_Fp(self, campo, Fps, Fpt):
        dot = 'digraph G {\nrankdir=LR;\nnode[shape=box];\nlabel="Fp matrices - ' + campo.get_nombre() + '";\n'
        
       
        for i in range(Fps.filas()):
            dot += f'  "E{i}" [label="E{i}"];\n'
       
        for j in range(Fps.cols()):
            dot += f'  "Ss{j}" [shape=ellipse,label="Ss{j}"];\n'
    
        for j in range(Fpt.cols()):
            dot += f'  "St{j}" [shape=ellipse,label="St{j}"];\n'

        
        for i in range(Fps.filas()):
            for j in range(Fps.cols()):
                v = Fps.get(i,j)
                dot += f'  "E{i}" -> "Ss{j}" [label="{v}"];\n'
        
        for i in range(Fpt.filas()):
            for j in range(Fpt.cols()):
                v = Fpt.get(i,j)
                dot += f'  "E{i}" -> "St{j}" [label="{v}"];\n'

        dot += "}\n"
        p = os.path.join(self.out_dir, "Fp.dot")
        with open(p, "w", encoding="utf-8") as f:
            f.write(dot)
        self._render_dot(p, os.path.join(self.out_dir, "Fp.png"))

    def graficar_Fr(self, campo, ids_reduc, Frs, Frt):
        dot = 'digraph G {\nrankdir=LR;\nnode[shape=box];\nlabel="Fr matrices - ' + campo.get_nombre() + '";\n'
        
      
        for i in range(Frs.filas()):
            dot += f'  "ER{i}" [label="{ids_reduc.get(i)}"];\n'
     
        for j in range(Frs.cols()):
            dot += f'  "SsR{j}" [shape=ellipse,label="Ss{j}"];\n'
      
        for j in range(Frt.cols()):
            dot += f'  "StR{j}" [shape=ellipse,label="St{j}"];\n'

       
        for i in range(Frs.filas()):
            for j in range(Frs.cols()):
                v = Frs.get(i,j)
                if v > 0:
                    dot += f'  "ER{i}" -> "SsR{j}" [label="{v}"];\n'
       
        for i in range(Frt.filas()):
            for j in range(Frt.cols()):
                v = Frt.get(i,j)
                if v > 0:
                    dot += f'  "ER{i}" -> "StR{j}" [label="{v}"];\n'

        dot += "}\n"
        p = os.path.join(self.out_dir, "Fr.dot")
        with open(p, "w", encoding="utf-8") as f:
            f.write(dot)
        self._render_dot(p, os.path.join(self.out_dir, "Fr.png"))

