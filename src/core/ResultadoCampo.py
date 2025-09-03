
class ResultadoCampo:
   
    def __init__(self, campo, Fs, Ft, Fps, Fpt, grupos, ids_reduc, nombres_reduc, Frs, Frt):
        self.__campo = campo
        self.__Fs = Fs
        self.__Ft = Ft
        self.__Fps = Fps
        self.__Fpt = Fpt
        self.__grupos = grupos
        self.__ids_reduc = ids_reduc
        self.__nombres_reduc = nombres_reduc
        self.__Frs = Frs
        self.__Frt = Frt

    def campo(self): return self.__campo
    def Fs(self): return self.__Fs
    def Ft(self): return self.__Ft
    def Fps(self): return self.__Fps
    def Fpt(self): return self.__Fpt
    def grupos(self): return self.__grupos
    def ids_reduc(self): return self.__ids_reduc
    def nombres_reduc(self): return self.__nombres_reduc
    def Frs(self): return self.__Frs
    def Frt(self): return self.__Frt
