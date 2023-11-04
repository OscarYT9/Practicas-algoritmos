# from ALgoritmos import *
# from FuncionesAuxiliares import *
# from FuncionesTest import *


# v=[1,2,3,4,3,53,53,2,4,32,35,36]
# tamaño_maximo=len(v)

# crear_monticulo(v,Monticulo(v))

# v = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# M = Monticulo(11)
# crear_Monticulo(v, M)
# print(M.Vector_monticulo)

# class MinHeap:
#     def __init__(self):
#         self.heap = []

#     def parent(self, i):
#         return (i - 1) // 2

#     def left_child(self, i):
#         return 2 * i + 1

#     def right_child(self, i):
#         return 2 * i + 2

#     def insert(self, value):
#         self.heap.append(value)
#         i = len(self.heap) - 1
#         while i > 0 and self.heap[i] < self.heap[self.parent(i)]:
#             self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
#             i = self.parent(i)

#     def extract_min(self):
#         if not self.heap:
#             return None
#         root = self.heap[0]
#         self.heap[0] = self.heap[-1]
#         self.heap.pop()
#         self._heapify(0)
#         return root

#     def _heapify(self, i):
#         left = self.left_child(i)
#         right = self.right_child(i)
#         smallest = i
#         if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
#             smallest = left
#         if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
#             smallest = right
#         if smallest != i:
#             self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
#             self._heapify(smallest)

# # Ejemplo de uso
# heap = MinHeap()
# heap.insert(5)
# heap.insert(3)
# heap.insert(8)
# heap.insert(1)

# print("Elementos extraídos en orden ascendente:")
# while heap.heap:
#     print(heap.extract_min())

class MonticuloBinario:
    def __init__(self):
        self.listaMonticulo = [0]
        self.tamanoActual = 0

    def __str__(self):
        return f"Tamaño montículo: {self.tamanoActual}, Vector montículo: {self.listaMonticulo}"

    def infiltArriba(self,i):
        while i // 2 > 0:
          if self.listaMonticulo[i] < self.listaMonticulo[i // 2]:
             tmp = self.listaMonticulo[i // 2]
             self.listaMonticulo[i // 2] = self.listaMonticulo[i]
             self.listaMonticulo[i] = tmp
          i = i // 2

    def insertar(self,k):
      self.listaMonticulo.append(k)
      self.tamanoActual = self.tamanoActual + 1
      self.infiltArriba(self.tamanoActual)

    def infiltAbajo(self,i):
      while (i * 2) <= self.tamanoActual:
          hm = self.hijoMin(i)
          if self.listaMonticulo[i] > self.listaMonticulo[hm]:
              tmp = self.listaMonticulo[i]
              self.listaMonticulo[i] = self.listaMonticulo[hm]
              self.listaMonticulo[hm] = tmp
          i = hm

    def hijoMin(self,i):
      if i * 2 + 1 > self.tamanoActual:
          return i * 2
      else:
          if self.listaMonticulo[i*2] < self.listaMonticulo[i*2+1]:
              return i * 2
          else:
              return i * 2 + 1

    def eliminarMin(self):
      valorSacado = self.listaMonticulo[1]
      self.listaMonticulo[1] = self.listaMonticulo[self.tamanoActual]
      self.tamanoActual = self.tamanoActual - 1
      self.listaMonticulo.pop()
      self.infiltAbajo(1)
      return valorSacado

    def construirMonticulo(self,unaLista):
      i = len(unaLista) // 2
      self.tamanoActual = len(unaLista)
      self.listaMonticulo = [0] + unaLista[:]
      while (i > 0):
          self.infiltAbajo(i)
          i = i - 1

miMonticulo = MonticuloBinario()
miMonticulo.construirMonticulo([9,5,6,2,3])
print(miMonticulo)

print(miMonticulo.eliminarMin())
print(miMonticulo)
print(miMonticulo.eliminarMin())
print(miMonticulo)
print(miMonticulo.eliminarMin())
print(miMonticulo)
print(miMonticulo.eliminarMin())
print(miMonticulo)
print(miMonticulo.eliminarMin())
print(miMonticulo)
