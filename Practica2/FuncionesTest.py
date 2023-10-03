from FuncionesAuxiliares import *
def ordenado(v):
    for i in range(len(v) - 1):
        if v[i] > v[i + 1]:
            return False
    return True

v = [1, 2]
print(ordenado(v))  # True, la lista está ordenada ascendentemente
