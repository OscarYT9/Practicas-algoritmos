from Algoritmos import *
from FuncionesAuxiliares import *
from FuncionesTests import *


# # Crear un montículo
# mi_monticulo = Monticulo()
# print(mi_monticulo)

# # Agregar elementos al montículo
# elementos = [9, 5, 6, 2, 3]
# mi_monticulo.crear_Monticulo(elementos)
# print(mi_monticulo)

# menor_eliminado = mi_monticulo.quitarMenor()
# print(f"El menor elemento eliminado es: {menor_eliminado}")
# print(mi_monticulo)

# menor = mi_monticulo.quitarMenor()
# print(f"El menor elemento eliminado es: {menor}")
# print(mi_monticulo)

# menor_nuevo = mi_monticulo.quitarMenor()
# print(f"El menor elemento eliminado es: {menor_nuevo}")
# print(mi_monticulo)

# menor_eliminado = mi_monticulo.quitarMenor()
# print(f"El menor elemento eliminado es: {menor_eliminado}")
# print(mi_monticulo)

# menor_eliminado = mi_monticulo.quitarMenor()
# print(f"El menor elemento eliminado es: {menor_eliminado}")
# print(mi_monticulo)

# menor_eliminado = mi_monticulo.quitarMenor()
# print(f"El menor elemento eliminado es: {menor_eliminado}")
# print(mi_monticulo)

# menor_eliminado = mi_monticulo.quitarMenor()
# print(f"El menor elemento eliminado es: {menor_eliminado}")
# print(mi_monticulo)

# menor_eliminado = mi_monticulo.quitarMenor()
# print(f"El menor elemento eliminado es: {menor_eliminado}")
# print(mi_monticulo)


# Importa las funciones desde los otros archivos
from FuncionesTests import *

def test(iteraciones):                  # Función que prueba los algoritmos 
    # print("\nTest 1 (Casos de Prueba):")
    # probar_algoritmos(10)

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