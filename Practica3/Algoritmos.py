class Monticulo:
    def __init__(self):
        self.Vector_monticulo = []
        self.Tamano_monticulo = 0

    def __str__(self):
        return f"Tamaño montículo: {self.Tamano_monticulo}, Vector montículo: {self.Vector_monticulo[1:]}"
    
    def crear_Monticulo(self, v):
        self.Vector_monticulo = [0] + v
        self.Tamano_monticulo = len(v)

        for i in range(self.Tamano_monticulo // 2, 0, -1):
            self.__hundir(i)

    def consultar_menor(self):
        if self.Tamano_monticulo == 0:
            return None

        return self.Vector_monticulo[1]

    def quitarMenor(self):
        if self.Tamano_monticulo == 0:
            return None

        menor = self.consultar_menor()  # Utiliza la función consultar_menor
        self.Vector_monticulo[1] = self.Vector_monticulo[self.Tamano_monticulo]
        self.Tamano_monticulo -= 1
        self.Vector_monticulo.pop()
        self.__hundir(1)

        return menor

    def __hundir(self, i):
        while True:
            HijoIzq = 2 * i
            HijoDer = 2 * i + 1
            j = i

            if HijoDer <= self.Tamano_monticulo and self.Vector_monticulo[HijoDer] < self.Vector_monticulo[i]:
                i = HijoDer

            if HijoIzq <= self.Tamano_monticulo and self.Vector_monticulo[HijoIzq] < self.Vector_monticulo[i]:
                i = HijoIzq

            if j != i:
                self.Vector_monticulo[j], self.Vector_monticulo[i] = self.Vector_monticulo[i], self.Vector_monticulo[j]
            else:
                break

