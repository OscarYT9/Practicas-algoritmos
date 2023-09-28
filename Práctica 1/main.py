# Importa las funciones desde los otros archivos
from FuncionesTests import *

def test(iteraciones):
    # Ejecutar las funciones test1 y test2 con los casos de prueba y vectores aleatorios
    print("\nTest 1 (Casos de Prueba):")
    test1(test_cases)
    
    print("\nTest 2 (Vectores Aleatorios):")
    test1(vectores_aleatorios)
    
    # Llamar a la función test_algoritmos con el algoritmo especificado
    print("\nTest de Tiempo de Ejecución:")
    test_tiempo_complejidad(1,1)
    print("")
    test_tiempo_complejidad(2,1)
    
    # Llamar a la función para analizar la complejidad con el algoritmo especificado
    for i in range(iteraciones):
        print(f"\nAnálisis de Complejidad: (Iteración nº {i+1})")
        test_tiempo_complejidad(1,2)
        print("")
        test_tiempo_complejidad(2,2)

# Llama a las funciones que deseas ejecutar
if __name__ == "__main__":
    #Puedes elegir el número de iteraciones que deseas.
    test(10)














# def ejecutar_pruebas(veces):
#     for _ in range(veces):
#         print("Ejecución ", _ + 1)
#         print("------------")
#         print("Pruebas Algoritmo 1:")
#         test1()
#         print("Pruebas Algoritmo 2:")
#         test2()
#         print("-" * 20)


#_______________________________________________________________________________________________________________________________________________________________________________________________________________________________
#Hacer funcion axiliar para imprimir bien el vector
#Hacer que en la misma ejecución saque varias veces las mismas tablas(para comprobar que están bien las mediciones)


# Imprimimos el vector aleatorio, las sumas calculadas y hacemos una comparación (operación constante) para comprobar si los resultados son iguales

#a mitad del desarrollo nos dimos cuenta que era mucho más eficiente crear una sola función para comprobar los vecores aleatorios y los definidos