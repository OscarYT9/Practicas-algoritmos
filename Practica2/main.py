# Importa las funciones desde los otros archivos
from FuncionesTests import *


def test(iteraciones):
    
    # Ejecutar las funciones test1 y test2 con los casos de prueba y vectores aleatorios
    print("\nTest 1 (Casos de Prueba):")
    test_resultados(test_cases)
    
    print("\nTest 2 (Vectores Aleatorios):")
    test_resultados(vectores_aleatorios)
    
    # Llamar a la función test_algoritmos con el algoritmo especificado
    print("\nTest 3 (Tiempo de Ejecución):")
    test_tiempo_complejidad(1,"Si") #Test exclusivamente de tiempo de ejecución del algoritmo 1
    print("")
    test_tiempo_complejidad(2,"Si") #Test exclusivamente de tiempo de ejecución del algoritmo 2
    
    # Llamar a la función para analizar la complejidad con el algoritmo especificado
    for i in range(iteraciones):
        print(f"\nTest 4 (Análisis de Complejidad): (Iteración nº {i+1})")
        test_tiempo_complejidad(1,"No") #Test exclusivamente de tiempo de ejecución del algoritmo 1
        print("")
        test_tiempo_complejidad(2,"No")

# Llama a las funciones que deseas ejecutar
if __name__ == "__main__":
    #Puedes elegir el número de iteraciones que deseas.
    test(20)
