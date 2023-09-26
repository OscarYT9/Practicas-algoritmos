from Algoritmos import *

#2. Valide que los algoritmos funcionan correctamente. Chequee las siguientes secuencias:

def test1():
    test_cases=[[-9,2,-5,-4,6],[4,0,9,2,5],[-2,-1,-9,-7,-1],[9,-2,1,-7,-8],[15,-2,-5,-4,16],[7,-5,6,7,-7]] # Definimos una lista de casos de prueba que consisten en arreglos de números enteros

    for test_case in test_cases:         # Iteramos a través de los casos de prueba
        a = sumaSubMax1(test_case)       # Calculamos la suma máxima usando el Algoritmo 1
        b = sumaSubMax2(test_case)       # Calculamos la suma máxima usando el Algoritmo 2
        print(test_case, a, b, a == b )  # Imprimimos el arreglo de entrada, las sumas calculadas y hacemos una comparación (operación constante) para comprobar si los resultados son iguales
        

#2.1 Así mismo realice una segunda comprobación con vectores generados de forma aleatoria (figura 1) comprobando que ambos algoritmos devuelven el mismo resultado

def aleatorio(n):
    '''
    Genera un vector de longitud n con números pseudoaleatorios en el rango [-n, n]
    '''
    import random
    v=list(range(n))
    for i in v:
        v[i] = random.randint(-n, n)
    return v


def test2():
    l = [aleatorio(9) for _ in range(9)]    # Generamos una lista de 9 vectores aleatorios utilizando la función aleatorio(9)

    for arr in l:                           # Iteramos a través de los vectores aleatorios
        a = sumaSubMax1(arr)                # Calculamos la suma máxima usando el Algoritmo 1
        b = sumaSubMax2(arr)                # Calculamos la suma máxima usando el Algoritmo 2
        print(arr, a, b, a == b)            # Imprimimos el vector aleatorio, las sumas calculadas y hacemos una comparación (operación constante) para comprobar si los resultados son iguales

    
#_______________________________________________________________________________________________________________________________________________________________________________________________________________________________
test1()
test2()
#_______________________________________________________________________________________________________________________________________________________________________________________________________________________________