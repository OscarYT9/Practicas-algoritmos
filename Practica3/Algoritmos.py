

# Uso del código:
class Monticulo:
    def __init__(self, tamano_maximo):
        self.Tamano_monticulo = tamano_maximo
        self.Vector_monticulo = [None] * (tamano_maximo + 1)

    def __str__(self):
        return f"Tamaño montículo: {self.Tamano_monticulo}, Vector montículo: {self.Vector_monticulo}"
#______________________________________________________________________________________________________________________

# def crear_monticulo(v: list, M: Monticulo):
#     M.Vector_monticulo = v
#     M.Tamaño_monticulo = len(v)
#     i = M.Tamaño_monticulo/2
#     for i in range(-1,1):
#         __hundir(M,i)
#     return M.Vector_monticulo


def crear_Monticulo(v: list, M: Monticulo):
    M.Vector_monticulo = v.copy()  # Copia los elementos de v a M.Vector_monticulo
    M.Tamano_monticulo = len(v)
    
    for i in range(M.Tamano_monticulo // 2, 0, -1):
        __hundir(M, i)

    return M.Vector_monticulo

def consultar_menor(M: Monticulo):
    if M.Tamano_monticulo == 0:
        return None
    
    return M.Vector_monticulo[1]

# def quitarMenor(M: Monticulo):
#     if M.Tamano_monticulo == 0:
#         return None
    
#     menor = M.Vector_monticulo[1]
#     M.Vector_monticulo[1] = M.Vector_monticulo[M.Tamano_monticulo]
#     M.Tamano_monticulo -= 1
#     __hundir(M, 1)
    
#     return menor

#______________________________________
def __hundir(M: Monticulo, i):
    while True:
        HijoIzq = 2 * i
        HijoDer = 2 * i + 1
        j = i

        if HijoDer <= M.Tamano_monticulo and M.Vector_monticulo[HijoDer - 1] < M.Vector_monticulo[i - 1]:
            i = HijoDer

        if HijoIzq <= M.Tamano_monticulo and M.Vector_monticulo[HijoIzq - 1] < M.Vector_monticulo[i - 1]:
            i = HijoIzq

        if j == i:
            break
        else:
            M.Vector_monticulo[j - 1], M.Vector_monticulo[i - 1] = M.Vector_monticulo[i - 1], M.Vector_monticulo[j - 1]


v=[12, 11, 13, 5, 6, 7]
M = Monticulo(len(v))

print(crear_Monticulo(v, M))
print(consultar_menor(M))
# print(quitarMenor(M))
# print(M)