from copy import deepcopy


class Monticulo:
    def __init__(self):
         # Inicializa un montículo vacío con un vector vacío y un tamaño cero.
        self.Vector_monticulo = []
        self.Tamano_monticulo = 0

    def __str__(self):
        # Devuelve una representación en cadena del montículo que muestra su tamaño y el vector.
        return f"Tamaño montículo: {self.Tamano_monticulo}, Vector montículo: {self.Vector_monticulo}"

    def crearMonticulo(self, v):
        # Crea un montículo a partir de un vector 'v'.
        # Hace una copia profunda del vector 'v' y luego construye el montículo a partir de él.
        # Utiliza el método '__hundir' para organizar el montículo.
        z = deepcopy(v)
        self.Vector_monticulo = z
        self.Tamano_monticulo = len(v)

        # Comienza a organizar el montículo desde el medio hacia la izquierda.
        for i in range(self.Tamano_monticulo // 2, -1, -1):  # Modifica el rango para incluir 0
            self.__hundir(i)

    def consultarMenor(self):
        # Devuelve el elemento más pequeño en el montículo (la raíz).
        if self.Tamano_monticulo == 0:
            return None

        return self.Vector_monticulo[0]

    def quitarMenor(self):
        # Elimina el elemento más pequeño en el montículo (la raíz) y lo devuelve.
        if self.Tamano_monticulo == 0:
            return None

        menor = self.consultarMenor()                                                # Almacena el valor menor antes de eliminarlo
        self.Vector_monticulo[0] = self.Vector_monticulo[self.Tamano_monticulo - 1]  # Copia el último elemento al índice 0
        self.Tamano_monticulo -= 1                                                   # Reduce el tamaño del montículo
        self.Vector_monticulo.pop()                                                  # Elimina el último elemento, que ahora está duplicado al principio
        self.__hundir(0)                                                             # Vuelve a organizar el montículo después de eliminar el elemento más pequeño.

        return menor

    def __hundir(self, i):
        # Método privado para organizar el montículo comenzando desde el índice 'i'.
        while True:
            # Calcula los índices de los hijos izquierdo y derecho
            HijoIzq = 2 * i + 1 
            HijoDer = 2 * i + 2
            j = i # Almacena el índice actual antes de realizar comparaciones
            
            # Compara el valor del hijo derecho e izquierdo con el valor en el índice actual (i), si es menor actualiza i
            if HijoDer < self.Tamano_monticulo and self.Vector_monticulo[HijoDer] < self.Vector_monticulo[i]:
                i = HijoDer

            if HijoIzq < self.Tamano_monticulo and self.Vector_monticulo[HijoIzq] < self.Vector_monticulo[i]:
                i = HijoIzq

            if j != i:
                # Intercambia los valores de los nodos 'i' y 'j' para restaurar la propiedad del montículo.
                self.Vector_monticulo[j], self.Vector_monticulo[i] = self.Vector_monticulo[i], self.Vector_monticulo[j]
            else:
                break

def ordenacionPorMonticulos(V):
    # Ordena un vector 'V' utilizando un montículo.
    mi_monticulo = Monticulo()
    mi_monticulo.crearMonticulo(V)

    for i in range(len(V)):
        # Extrae el elemento más pequeño del montículo y lo coloca en la posición 'i' del vector.
        V[i] = mi_monticulo.consultarMenor()
        mi_monticulo.quitarMenor()


