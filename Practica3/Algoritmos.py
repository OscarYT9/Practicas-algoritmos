from copy import deepcopy


class Monticulo:
    def __init__(self):
        self.Vector_monticulo = []
        self.Tamano_monticulo = 0

    def __str__(self):
        return f"Tamaño montículo: {self.Tamano_monticulo}, Vector montículo: {self.Vector_monticulo}"

    def crear_Monticulo(self, v):
        z = deepcopy(v)
        self.Vector_monticulo = z
        self.Tamano_monticulo = len(v)

        for i in range(self.Tamano_monticulo // 2, -1, -1):  # Modifica el rango para incluir 0
            self.__hundir(i)

    def consultar_menor(self):
        if self.Tamano_monticulo == 0:
            return None

        return self.Vector_monticulo[0]

    def quitarMenor(self):
        if self.Tamano_monticulo == 0:
            return None

        menor = self.consultar_menor()
        #print(self)
        self.Vector_monticulo[0] = self.Vector_monticulo[self.Tamano_monticulo - 1]  # Modifica el índice
        #print(self)
        self.Tamano_monticulo -= 1
        self.Vector_monticulo.pop()
        #print(self)
        self.__hundir(0)  # Modifica el índice

        return menor

    def __hundir(self, i):
        while True:
            HijoIzq = 2 * i + 1  # Modifica los cálculos de los hijos izquierdos y derechos
            HijoDer = 2 * i + 2
            j = i

            if HijoDer < self.Tamano_monticulo and self.Vector_monticulo[HijoDer] < self.Vector_monticulo[i]:
                i = HijoDer

            if HijoIzq < self.Tamano_monticulo and self.Vector_monticulo[HijoIzq] < self.Vector_monticulo[i]:
                i = HijoIzq

            if j != i:
                self.Vector_monticulo[j], self.Vector_monticulo[i] = self.Vector_monticulo[i], self.Vector_monticulo[j]
            else:
                break

def ordenacionPorMonticulos(V):
    mi_monticulo = Monticulo()
    mi_monticulo.crear_Monticulo(V)

    for i in range(len(V)):
        V[i] = mi_monticulo.consultar_menor()
        mi_monticulo.quitarMenor()


# L=[]
# def ordenacionPorMonticulos(V):
#     mi_monticulo = Monticulo()
#     mi_monticulo.crear_Monticulo(V)

#     for i in range(len(V)):
#         #print(i)
#         menor = mi_monticulo.consultar_menor()
#         L.append(menor)
        
#         if menor is not None:
#             mi_monticulo.quitarMenor()
#             print(V)
#             #print(V)
#         else:
#             break  # Agregar una condición para salir si no hay más elementos en el montículo

# Ejemplo de uso
V = [9, 5, 6, 2, 3]
ordenacionPorMonticulos(V)
print("Arreglo ordenado:", V)
