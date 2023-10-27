
#_____________________________________________________________________________________

def hundir(M, i):
    while True:
        HijoIzq = 2 * i
        HijoDer = 2 * i + 1
        j = i

        if HijoDer <= M.Tamaño_monticulo and M.Vector_monticulo[HijoDer - 1] > M.Vector_monticulo[i - 1]:
            i = HijoDer

        if HijoIzq <= M.Tamaño_monticulo and M.Vector_monticulo[HijoIzq - 1] > M.Vector_monticulo[i - 1]:
            i = HijoIzq

        if j == i:
            break
        else:
            M.Vector_monticulo[j - 1], M.Vector_monticulo[i - 1] = M.Vector_monticulo[i - 1], M.Vector_monticulo[j - 1]
#__________________________________________________________________________________________________________________________________
# Uso del código:
class Monticulo:
    def __init__(self, tamano_maximo):
        self.Tamano_monticulo = tamano_maximo
        self.Vector_monticulo = [None] * (tamano_maximo + 1)

    def __str__(self):
        return f"Tamaño montículo: {self.Tamano_monticulo}, Vector montículo: {self.Vector_monticulo}"


