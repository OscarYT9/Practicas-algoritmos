def crear_monticulo(v, M):
    M.Vector_monticulo = v.copy()  # Copia los elementos de v a M.Vector_monticulo
    M.Tamaño_monticulo = len(v)
    
    for i in range(M.Tamaño_monticulo // 2, 0, -1):
        hundir(M, i)

    return M.Vector_monticulo

def hundir(M, i):
    while True:
        izquierda = 2 * i
        derecha = 2 * i + 1
        minimo = i

        if izquierda <= M.Tamaño_monticulo and M.Vector_monticulo[izquierda - 1] < M.Vector_monticulo[minimo - 1]:
            minimo = izquierda

        if derecha <= M.Tamaño_monticulo and M.Vector_monticulo[derecha - 1] < M.Vector_monticulo[minimo - 1]:
            minimo = derecha

        if minimo == i:
            break
        else:
            M.Vector_monticulo[i - 1], M.Vector_monticulo[minimo - 1] = M.Vector_monticulo[minimo - 1], M.Vector_monticulo[i - 1]
            i = minimo

# Uso del código:
class Monticulo:
    pass

v=[5,33,17,27,9,14,18,11,21,19]
M = Monticulo()
crear_monticulo(v, M)
print(M.Vector_monticulo)
