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



def calcular_tiempo_promedio(repeticiones_umbral, n):    # Realizar repeticiones de inicialización + algoritmo K veces, es decir, repetir el cálculo del algoritmo K veces y para eso necesitas inicializar el vector K veces también, sino inicializas el vector, el algoritmo siempre iteraría las K veces sobre el vector ordenado
   import time

   # Mide el tiempo de ejecución total de Ordenacion_func ejecutado en un vector inicializado repeticiones_umbral veces

   ta = time.perf_counter_ns()                  # Tiempo antes de comenzar la ejecución
   for _ in range(repeticiones_umbral):         # Inicializa un vector y ejecuta el algoritmo de ordenación en ese vector repeticiones_umbral veces
      mi_monticulo = Monticulo()
      vector = inicializar(n)         # Ejecuta el algoritmo en esa iteración (n) un numero k de veces para cerciorarte de que el algoritmo es correcto, por eso tienes que pasarle a esta función todo lo necesario para volver a ejecutar esa misma ejecución n numero de veces, medir su tiempo y hacer la media del tiempo de las diferentes ejecuciones
      mi_monticulo.crear_Monticulo(vector)       
   tb = time.perf_counter_ns()                  # Tiempo después de finalizar todas las ejecuciones

   t1 = tb - ta                                 # Tiempo total de la ejecución = Tiempo al finalizar todas las ejecuciones - Tiempo antes de comenzar la ejecución


   # Mide el tiempo de inicialización sola del vector (sin ejecutar el algoritmo) también repetido repeticiones_umbral veces

   ta = time.perf_counter_ns()                  # Tiempo antes de comenzar la ejecución
   for _ in range(repeticiones_umbral):         # Realiza un bucle for que inicializa un vector repeticiones_umbral veces
       mi_monticulo = Monticulo()
       vector = inicializar(n)
   tb = time.perf_counter_ns()                  # Tiempo después de finalizar todas las ejecuciones
   
   t2 = tb - ta                                 # Tiempo de inicialización

   t = (t1 - t2) / repeticiones_umbral          # Resta el tiempo de inicialización para almacenar solo con el del algoritmo y después lo divides entre las K repeticiones para obtener el promedio del tiempo necesario para ejecutar el algoritmo
   return t       


def cotas_ajustadas(n, tiempo, exp1, exp2, exp3):   # Calcula las cotas  
    
   # Calcula las cotas subestimada, ajustada y sobrestimada en función de los parámetros dados
    cota_subestimada= tiempo / (n ** exp1)
    cota_ajustada = tiempo / (n ** exp2)
    cota_sobrestimada = tiempo / (n ** exp3)

    # Devuelve una cadena formateada con las cotas y el tamaño del vector
    return f"{n:>10}\t\t{tiempo:>15.4f}       {cota_subestimada:>15.6f}{cota_ajustada:>15.6f}{cota_sobrestimada:>15.6f}"

#______________________________________
def calcular_tiempo_ejecucion_ordenacionPorMonticulos(n):    # Medir el tiempo de ejecución de una función (que representa un algoritmo) cuando se le proporciona un vector como entrada
    import time
    vector = inicializar(n)  # Puedes usar el vector aleatorio como entrada

    inicio = time.perf_counter_ns()
    ordenacionPorMonticulos(vector)
    fin = time.perf_counter_ns()

    tiempo_ejecucion = fin - inicio

    return tiempo_ejecucion


def calcular_tiempo_promedio_ordenacionPorMonticulos(repeticiones_umbral, n):    # Realizar repeticiones de inicialización + algoritmo K veces, es decir, repetir el cálculo del algoritmo K veces y para eso necesitas inicializar el vector K veces también, sino inicializas el vector, el algoritmo siempre iteraría las K veces sobre el vector ordenado
   import time

   # Mide el tiempo de ejecución total de Ordenacion_func ejecutado en un vector inicializado repeticiones_umbral veces

   ta = time.perf_counter_ns()                  # Tiempo antes de comenzar la ejecución
   for _ in range(repeticiones_umbral):         # Inicializa un vector y ejecuta el algoritmo de ordenación en ese vector repeticiones_umbral veces
      vector = inicializar(n)         # Ejecuta el algoritmo en esa iteración (n) un numero k de veces para cerciorarte de que el algoritmo es correcto, por eso tienes que pasarle a esta función todo lo necesario para volver a ejecutar esa misma ejecución n numero de veces, medir su tiempo y hacer la media del tiempo de las diferentes ejecuciones
      ordenacionPorMonticulos(vector)       
   tb = time.perf_counter_ns()                  # Tiempo después de finalizar todas las ejecuciones

   t1 = tb - ta                                 # Tiempo total de la ejecución = Tiempo al finalizar todas las ejecuciones - Tiempo antes de comenzar la ejecución


   # Mide el tiempo de inicialización sola del vector (sin ejecutar el algoritmo) también repetido repeticiones_umbral veces

   ta = time.perf_counter_ns()                  # Tiempo antes de comenzar la ejecución
   for _ in range(repeticiones_umbral):         # Realiza un bucle for que inicializa un vector repeticiones_umbral veces
       vector = inicializar(n)
   tb = time.perf_counter_ns()                  # Tiempo después de finalizar todas las ejecuciones
   
   t2 = tb - ta                                 # Tiempo de inicialización

   t = (t1 - t2) / repeticiones_umbral          # Resta el tiempo de inicialización para almacenar solo con el del algoritmo y después lo divides entre las K repeticiones para obtener el promedio del tiempo necesario para ejecutar el algoritmo
   return t       

import math

def cotas_ajustadas_ordenacionPorMonticulos(n, tiempo):
    # Calcula las cotas subestimada, ajustada y sobrestimada en función de los parámetros dados
    cota_subestimada = tiempo / (n ** 1)  # Utiliza log base 2 para n log(n)
    cota_ajustada = tiempo / (n * math.log(n, 2))
    cota_sobrestimada = tiempo / (n ** 2)

    # Devuelve una cadena formateada con las cotas y el tamaño del vector
    return f"{n:>10}\t\t{tiempo:>15.4f}       {cota_subestimada:>15.6f}{cota_ajustada:>15.6f}{cota_sobrestimada:>15.6f}"
