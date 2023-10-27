

def crear_monticulo(v: list, M: Monticulo):
    M.Vector_monticulo = v
    M.Tamaño_monticulo = len(v)
    i = M.Tamaño_monticulo/2
    for i in range(-1,1):
        __hundir(M,i)
    return M.Vector_monticulo


def crear_Monticulo(v, M):
    M.Vector_monticulo = v.copy()  # Copia los elementos de v a M.Vector_monticulo
    M.Tamaño_monticulo = len(v)
    
    for i in range(M.Tamaño_monticulo // 2, 0, -1):
        hundir(M, i)

    return M.Vector_monticulo

def consultarMenor(M: Monticulo): #????
    j=i
    for i in M.Vector_monticulo:

        

    return int

#def quitarMenor()



