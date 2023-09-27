# Importa las funciones desde los otros archivos
from FuncionesTests import *

# Llama a las funciones que deseas ejecutar
if __name__ == "__main__":

    print("")
    test1(test_cases)
    print("")
    test1(vectores_aleatorios)



    # Luego puedes llamar a la función test_algoritmos con algoritmo 1 o 2
    test_algoritmos(1)
    test_algoritmos(2)

    # Llama a la función para analizar la complejidad
    analizar_complejidad(1)
    analizar_complejidad(2)














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