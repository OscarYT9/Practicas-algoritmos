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
    
    probar_algoritmo_ordenación(5,"ascendente")
    probar_algoritmo_ordenación(5,"descendente")
    probar_algoritmo_ordenación(5,"aleatorio")
    

    for i in range(iteraciones):        # Bucle para comprobar la eficacia de los algoritmos
        print(f"\nTest 2 (Análisis de Complejidad): (Iteración nº {i+1})")
        test_tiempo_complejidad_crearMonticulo("ascendente",0.8, 1, 1.2)   ##Se ejecuta muy rapido, y como se puede ver al ejecutarse tan rapido, es tambiñén más neceasrio hacer el promedio, es la función que tiene más *
        test_tiempo_complejidad_crearMonticulo("descendente",0.8, 1, 1.2)#
        test_tiempo_complejidad_crearMonticulo("aleatorio",0.8, 1, 1.2)#
        test_tiempo_complejidad_ordenacionPorMonticulos("ascendente")
        test_tiempo_complejidad_ordenacionPorMonticulos("descendente")
        test_tiempo_complejidad_ordenacionPorMonticulos("aleatorio")
# Llama a las funciones que deseas ejecutar
if __name__ == "__main__":
    #Puedes elegir el número de iteraciones que deseas.
    test(10)