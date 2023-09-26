from Algoritmos import *
from FuncionesAuxiliares import *

#2. Valide que los algoritmos funcionan correctamente. Chequee las siguientes secuencias:

def test1():
    test_cases=[[-9,2,-5,-4,6],
                [4,0,9,2,5],
                [-2,-1,-9,-7,-1],
                [9,-2,1,-7,-8],
                [15,-2,-5,-4,16],
                [7,-5,6,7,-7]] # Definimos una lista de casos de prueba que consisten en arreglos de números enteros

    for test_case in test_cases:         # Iteramos a través de los casos de prueba
        a = sumaSubMax1(test_case)       # Calculamos la suma máxima usando el Algoritmo 1
        b = sumaSubMax2(test_case)       # Calculamos la suma máxima usando el Algoritmo 2
        imprimirVector(test_case,a,b)    # Llamamos a la función auxiliar que nos imprimirá cada vector

#2.1 Así mismo realice una segunda comprobación con vectores generados de forma aleatoria (figura 1) comprobando que ambos algoritmos devuelven el mismo resultado

def test2():
    l = [aleatorio(9) for _ in range(9)]    # Generamos una lista de 9 vectores aleatorios utilizando la función aleatorio(9)

    for arr in l:                           # Iteramos a través de los vectores aleatorios
        a = sumaSubMax1(arr)                # Calculamos la suma máxima usando el Algoritmo 1
        b = sumaSubMax2(arr)                # Calculamos la suma máxima usando el Algoritmo 2
        imprimirVector(arr,a,b)            # Imprimimos el vector aleatorio, las sumas calculadas y hacemos una comparación (operación constante) para comprobar si los resultados son iguales

    
#_______________________________________________________________________________________________________________________________________________________________________________________________________________________________
print("")
test1()
print("")
test2()
#_______________________________________________________________________________________________________________________________________________________________________________________________________________________________
#Hacer funcion axiliar para imprimir bien el vector
#Hacer que en la misma ejecución saque varias veces las mismas tablas(para comprobar que están bien las mediciones)