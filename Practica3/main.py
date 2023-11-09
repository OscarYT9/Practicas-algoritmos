from Algoritmos import *
from FuncionesAuxiliares import *
from FuncionesTests import *


# Importa las funciones desde los otros archivos
from FuncionesTests import *

def test(iteraciones):      
    # Función que prueba los algoritmos             
    print("\nTest 1 (Casos de Prueba):")
    # Ejecuta pruebas en diferentes casos de entrada
    probar_operaciones_monticulo(5,"ascendente")
    probar_operaciones_monticulo(5,"descendente")
    probar_operaciones_monticulo(5,"aleatorio")
    
    probar_algoritmo_ordenacion(5,"ascendente")
    probar_algoritmo_ordenacion(5,"descendente")
    probar_algoritmo_ordenacion(5,"aleatorio")
    

    for i in range(iteraciones):        
        # Bucle para comprobar la eficacia de los algoritmos

        print(f"\nTest 2 (Análisis de Complejidad): (Iteración nº {i+1})")

        # Imprime y analiza la complejidad del algoritmo para crear montículos en diferentes casos
        print("Creación montículo (orden ascendente)")
        imprimir_complejidad_crearMonticulo(1,"ascendente",0.8, 1, 1.2)   ##Se ejecuta muy rapido, y como se puede ver al ejecutarse tan rapido, es también más neceasrio hacer el promedio, es la función que tiene más *
        print("Creación montículo (orden descendente)")
        imprimir_complejidad_crearMonticulo(1,"descendente",0.8, 1, 1.2)
        print("Creación montículo (orden aleatorio)")
        imprimir_complejidad_crearMonticulo(1,"aleatorio",0.8, 1, 1.2)
        print("Ordenación del vector (orden ascendente)")

        # Imprime y analiza la complejidad del algoritmo de ordenación por montículos en diferentes casos
        imprimir_complejidad_ordenacionPorMonticulos(2,"ascendente")
        print("Ordenación del vector (orden descendente)")
        imprimir_complejidad_ordenacionPorMonticulos(2,"descendente")
        print("Ordenación del vector (orden aleatorio)")
        imprimir_complejidad_ordenacionPorMonticulos(2,"aleatorio")
        
# Llama a las funciones que deseas ejecutar
if __name__ == "__main__":
    #Puedes elegir el número de iteraciones que deseas.
    test(10)