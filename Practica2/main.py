# Importa las funciones desde los otros archivos
from FuncionesTests import *


def test(iteraciones):
    for i in range(iteraciones):
        print(f"\nTest 4 (Análisis de Complejidad): (Iteración nº {i+1})")
        test_tiempo_complejidad(1 ,"asc", 1.8, 2, 2.2)
        test_tiempo_complejidad(1 ,"desc", 1.8, 2, 2.2)#
        test_tiempo_complejidad(1 ,"alet", 1.8, 2, 2.2)#
        test_tiempo_complejidad(2 ,"asc",0.9,1.2,1.3)#
        test_tiempo_complejidad(2 ,"desc",0.9,1.2,1.3)#
        test_tiempo_complejidad(2 ,"alet",1,1.2,1.4)
# Llama a las funciones que deseas ejecutar
if __name__ == "__main__":
    #Puedes elegir el número de iteraciones que deseas.
    test(5)
