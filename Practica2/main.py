# Importa las funciones desde los otros archivos
from FuncionesTests import *

def test(iteraciones):
    print("\nTest 1 (Casos de Prueba):")
    probar_algoritmos(10)

    for i in range(iteraciones):
        print(f"\nTest 2 (Análisis de Complejidad): (Iteración nº {i+1})")
        test_tiempo_complejidad(1 ,"asc", 0.5, 1, 1.5)   ##Se ejecuta muy rapido, y como se puede ver al ejecutarse tan rapido, es tambiñén más neceasrio hacer el promedio, es la función que tiene más *
        test_tiempo_complejidad(1 ,"desc", 1.8, 2, 2.2)#
        test_tiempo_complejidad(1 ,"alet", 1.8, 2, 2.2)#
        test_tiempo_complejidad(2 ,"asc",0.9,1.2,1.3)#   ##En cambio el algoritmo del shell parece que se prácticamente todas sus ejecuciones tienen el mismo tiempo de ejecución y por lo tanto la misma complejidad
        test_tiempo_complejidad(2 ,"desc",0.9,1.2,1.3)#
        test_tiempo_complejidad(2 ,"alet",1,1.2,1.4)
        
# Llama a las funciones que deseas ejecutar
if __name__ == "__main__":
    #Puedes elegir el número de iteraciones que deseas.
    test(5)
