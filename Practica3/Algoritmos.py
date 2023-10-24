v=[1,2,3,4,3,53,53,2,4,32,35,36]
tamaño_maximo=len(v)

class Monticulo:
    def __init__(self, Vector_monticulo):
        self.Tamaño_monticulo = len(Vector_monticulo)
        self.Vector_monticulo = list(range(1, self.Tamaño_monticulo)) #de tipo elemento?¿??¿??

def __hundir(M, i):
    j = i
    while j != i:
        HijoIzq = 2 * i
        HijoDer = 2 * i + 1

        if HijoDer <= M.Tamaño_monticulo and M.Vector_monticulo[HijoDer - 1] > M.Vector_monticulo[i - 1]:
            i = HijoDer
        if HijoIzq <= M.Tamaño_monticulo and M.Vector_monticulo[HijoIzq - 1] > M.Vector_monticulo[i - 1]:
            i = HijoIzq
        if i != j:
            M.Vector_monticulo[i - 1], M.Vector_monticulo[j - 1] = M.Vector_monticulo[j - 1], M.Vector_monticulo[i - 1]
        else:
            break


#def colsultarMenor()??¿?¿?


def crear_monticulo(v: list, M: Monticulo):
    M.Vector_monticulo = v
    M.Tamaño_monticulo = len(v)
    i = M.Tamaño_monticulo/2
    for i in range(-1,1):
        __hundir(M,i)
    return M.Vector_monticulo

def consultarMenor(M: Monticulo):
    j=i
    for i in M.Vector_monticulo:

        

    return int

#def quitarMenor()


crear_monticulo(v,Monticulo(v))
