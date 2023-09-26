#Práctica 1
#Suma de la subsecuencia máxima: Dados n números enteros a1,a2,...,an encontrar el valor máximo de
#∑jk=iak con 1 ≤ i ≤ j ≤ n (por conveniencia, la suma de la subsecuencia máxima es 0 si todos los enteros
#son negativos).

#Se pide:
#1. Implemente en PYTHON los algoritmos propuestos:

#Algoritmo 1: O(n^2)
def sumaSubMax1(v:list) -> int: # v es el arreglo de entrada
    n=len(v)                    # n es la longitud del arreglo (en este caso, 5)
    sumaMax=0                   # Inicializa la suma máxima en 0

    for i in range(0,n):            # Itera a través de todos los índices de inicio del subarreglo (0....4)
        estaSuma = 0                # Inicializa la suma actual en 0

        for j in range(i,n):        # Itera a través de todos los índices de fin del subarreglo (0...4)
            estaSuma += v[j]        # Agrega el valor del elemento v[j] a la suma actual

            if estaSuma > sumaMax:  # Si la suma actual es mayor que la suma máxima registrada
                sumaMax=estaSuma    # Actualiza la suma máxima con la suma actual
    return sumaMax                  # Devuelve la máxima suma
            
#Si no encuentra ninguna convinación que de un número mayor que 0, entonces el valor que devuelve siempre es 0. (Que es valor orginal de SumaMax, aún así debe ejecutar todos las iteraciones del algoritmo para comprobar todas las convinaciones y así comprobar que no existe ninguna convinación que de mayor que cero, por lo que la complejidad viene siendo la misma que en los otros caso en los que encuentra una solución al problema)


#Algoritmo 2: O(n)
def sumaSubMax2(v:list) -> int: 
    n=len(v)                    # n es la longitud del arreglo
    estaSuma=0                  # Inicializa la suma actual en 0
    sumaMax=0                   # Inicializa la suma máxima en 0

    for j in range(0,n):            # Itera a través de todos los elementos del arreglo
        estaSuma+=v[j]              # Agrega el valor del elemento v[j] a la suma actual

        if estaSuma > sumaMax:      # Si la suma actual es mayor que la suma máxima registrada
            sumaMax=estaSuma        # Actualiza la suma máxima con la suma actual

        elif estaSuma < 0:          # Si la suma actual es negativa
            estaSuma=0              # Reinicia la suma actual a 0

    return sumaMax                  # Devuelve la suma máxima encontrada

#_______________________________________________________________________________________________________________________________________________________________________________________________________________________________

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

# 3. Determine los tiempos de ejecución con vectores aleatorios de tamaño n. Para el primer algoritmo
# n será igual a 500,1000,2000,4000 y 8000; para el segundo algoritmo añada también los valores
# 16000,32000,64000,128000 y 256000. Use el código de la figura 3 para obtener la hora del sistema.
# Para generar los datos de prueba utilice el código de la figura 1 que genera vectores de números
# pseudoaleatorios en el rango [−n,...,n].

import time

# Tamaños de n a probar
tamanos_n = [500, 1000, 2000, 4000, 8000, 16000, 32000, 64000, 128000, 256000]

for n in tamanos_n:
    # Genera un vector aleatorio de tamaño n
    vector = aleatorio(n)
    
    # Mide el tiempo de ejecución del Algoritmo 1
    inicio = time.perf_counter_ns()
    sumaSubMax1(vector)
    fin = time.perf_counter_ns()
    tiempo_ejecucion1 = fin - inicio

    # Mide el tiempo de ejecución del Algoritmo 2
    inicio = time.perf_counter_ns()
    sumaSubMax2(vector)
    fin = time.perf_counter_ns()
    tiempo_ejecucion2 = fin - inicio

    # Imprime los resultados
    print(f"Tamaño de n: {n}")
    print(f"Tiempo de ejecución Algoritmo 1: {tiempo_ejecucion1} nanosegundos")
    print(f"Tiempo de ejecución Algoritmo 2: {tiempo_ejecucion2} nanosegundos")
    print()