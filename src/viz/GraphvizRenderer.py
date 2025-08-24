import os
from src.utils.Mensajes import info

class GraphvizRenderer:
    def __init__(self, out_dir="out"):
        self.out_dir = out_dir
        if not os.path.isdir(out_dir):
            os.makedirs(out_dir)

    def _render_dot(self, dot_path, png_path):
        os.system(f'dot -Tpng "{dot_path}" -o "{png_path}"')
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
                if v>0: dot += f'  "E{i}" -> "Ss{j}" [label="{v}"];\n'
       
        for i in range(Ft.filas()):
            for j in range(Ft.cols()):
                v = Ft.get(i,j)
                if v>0: dot += f'  "E{i}" -> "St{j}" [label="{v}"];\n'
        dot += "}\n"
        p = os.path.join(self.out_dir,"F.dot")
        with open(p,"w",encoding="utf-8") as f: f.write(dot)
        self._render_dot(p, os.path.join(self.out_dir,"F.png"))

    def graficar_Fp(self, campo, Fps, Fpt):
        
        import os
        dot = 'digraph G {\nrankdir=LR;\nnode[shape=box];\nlabel="Fp matrices - ' + campo.get_nombre() + '";\n'
        for i in range(Fps.filas()): dot += f'  "E{i}" [label="E{i}"];\n'
        for j in range(Fps.cols()): dot += f'  "Ss{j}" [shape=ellipse,label="Ss{j}"];\n'
        for j in range(Fpt.cols()): dot += f'  "St{j}" [shape=ellipse,label="St{j}"];\n'
        for i in range(Fps.filas()):
            for j in range(Fps.cols()):
                v = Fps.get(i,j)
                dot += f'  "E{i}" -> "Ss{j}" [label="{v}"];\n'
        for i in range(Fpt.filas()):
            for j in range(Fpt.cols()):
                v = Fpt.get(i,j)
                dot += f'  "E{i}" -> "St{j}" [label="{v}"];\n'
        dot += "}\n"
        p = os.path.join(self.out_dir,"Fp.dot")
        with open(p,"w",encoding="utf-8") as f: f.write(dot)
        self._render_dot(p, os.path.join(self.out_dir,"Fp.png"))

    def graficar_Fr(self, campo, ids_reduc, Frs, Frt):
        dot = 'digraph G {\nrankdir=LR;\nnode[shape=box];\nlabel="Fr matrices - ' + campo.get_nombre() + '";\n'
        for i in range(Frs.filas()):
            dot += f'  "ER{i}" [label="{ids_reduc.get(i)}"];\n'
        for j in range(Frs.cols()): dot += f'  "SsR{j}" [shape=ellipse,label="Ss{j}"];\n'
        for j in range(Frt.cols()): dot += f'  "StR{j}" [shape=ellipse,label="St{j}"];\n'
        for i in range(Frs.filas()):
            for j in range(Frs.cols()):
                v = Frs.get(i,j)
                if v>0: dot += f'  "ER{i}" -> "SsR{j}" [label="{v}"];\n'
        for i in range(Frt.filas()):
            for j in range(Frt.cols()):
                v = Frt.get(i,j)
                if v>0: dot += f'  "ER{i}" -> "StR{j}" [label="{v}"];\n'
        dot += "}\n"
        p = os.path.join(self.out_dir,"Fr.dot")
        with open(p,"w",encoding="utf-8") as f: f.write(dot)
        self._render_dot(p, os.path.join(self.out_dir,"Fr.png"))
