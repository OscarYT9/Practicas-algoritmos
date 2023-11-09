from Algoritmos import *
from FuncionesAuxiliares import *
from FuncionesTests import *


# Importa las funciones desde los otros archivos
from FuncionesTests import *

def test(iteraciones):                  # Función que prueba los algoritmos 
    print("\nTest 1 (Casos de Prueba):")
    probar_operaciones_monticulo(5,"ascendente")
    probar_operaciones_monticulo(5,"descendente")
    probar_operaciones_monticulo(5,"aleatorio")
    
    probar_algoritmo_ordenacion(5,"ascendente")
    probar_algoritmo_ordenacion(5,"descendente")
    probar_algoritmo_ordenacion(5,"aleatorio")
    

    for i in range(iteraciones):        # Bucle para comprobar la eficacia de los algoritmos
        print(f"\nTest 2 (Análisis de Complejidad): (Iteración nº {i+1})")
        imprimir_complejidad_crearMonticulo(1,"ascendente",0.8, 1, 1.2)   ##Se ejecuta muy rapido, y como se puede ver al ejecutarse tan rapido, es tambiñén más neceasrio hacer el promedio, es la función que tiene más *
        imprimir_complejidad_crearMonticulo(1,"descendente",0.8, 1, 1.2)#
        imprimir_complejidad_crearMonticulo(1,"aleatorio",0.8, 1, 1.2)#
        imprimir_complejidad_ordenacionPorMonticulos(2,"ascendente")
        imprimir_complejidad_ordenacionPorMonticulos(2,"descendente")
        imprimir_complejidad_ordenacionPorMonticulos(2,"aleatorio")
# Llama a las funciones que deseas ejecutar
if __name__ == "__main__":
    #Puedes elegir el número de iteraciones que deseas.
    test(10)