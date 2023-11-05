#Funciones que se usan dentro de otras funciones.
from Algoritmos import *            #Importamos los algoritmos a probar

def inicializar(n): # Crea un vector de una longitud dada (n) con elementos aleatorios 
    import random
    
    v=list(range(n))                    # Crear una lista de números en el rango [0, n-1]
    for i in v:                         # Iterar sobre la lista y asignar números enteros aleatorios entre -n y n
        v[i] = random.randint(-n, n)
    return v                            # Devolver la lista con valores aleatorios

#-------------------------------------------

def calcular_tiempo_ejecucion(n):    # Medir el tiempo de ejecución de una función (que representa un algoritmo) cuando se le proporciona un vector como entrada
    import time
    mi_monticulo = Monticulo()
    vector = inicializar(n)  # Puedes usar el vector aleatorio como entrada
    inicio = time.perf_counter_ns()
    mi_monticulo.crear_Monticulo(vector)
    fin = time.perf_counter_ns()
    tiempo_ejecucion = fin - inicio
    return tiempo_ejecucion

def cotas_ajustadas(n, tiempo, exp1, exp2, exp3):   # Calcula las cotas  
    
   # Calcula las cotas subestimada, ajustada y sobrestimada en función de los parámetros dados
    cota_subestimada= tiempo / (n ** exp1)
    cota_ajustada = tiempo / (n ** exp2)
    cota_sobrestimada = tiempo / (n ** exp3)

    # Devuelve una cadena formateada con las cotas y el tamaño del vector
    return f"{n:>10}\t\t{tiempo:>15.4f}       {cota_subestimada:>15.6f}{cota_ajustada:>15.6f}{cota_sobrestimada:>15.6f}"