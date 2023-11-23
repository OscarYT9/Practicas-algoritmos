from Algoritmos import *
from FuncionesAuxiliares import *
from FuncionesTest import *

def test(j):

    #ejecuta el primer test, el que comprueba que los resultados después de aplicar el algoritmo dijkstra son correctos
    test_matrices_minimas()
    
    #10 iteraciones donde se muestra el tiempo de ejecución (t(n)) y t(n)/n^(cota)
    for i in range(j):
        imprimir_complejidad(2.8,2.95,3.1)

if __name__ == "__main__":
    test(10)