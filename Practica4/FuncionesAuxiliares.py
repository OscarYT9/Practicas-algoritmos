#Funciones que se usan dentro de otras funciones.
from Algoritmos import *            #Importamos los algoritmos a probar
import random



def aleatorio(n):
    l=list(range(n)) 
    for i in l:     
        l[i] = random.randint(1, 1000) 
    return l                        # Devolver la lista con valores aleatorios


def matrizAleatoria(n):
    m = []
    for i in range(n):
        m.append(aleatorio(n))
    for i in range(n):
        for j in range(i+1):
            if (i==j):
                m[i][j]=0
            else:
                m[i][j]=m[j][i]
    return m


def formatear_lista(lista, ancho):
    """
     Parámetros
     ----------
     lista: 
        vector con los elementos a aplicar los algoritmos

     ancho:
        valor de tipo entero para definir el formato de la impresión por pantalla

     Qué hace la función?
     ----------
        Formatea una lista de números para que cada elemento ocupe un ancho específico y agrega corchetes alrededor de la lista.
        (Está función es solo para imprimir de forma legible los datos, no afecta a la velocidad de los 2 algoritmos, ya que se ejecuta una vez finalizados)
     Devuelve
     -------
       El vector concatenado con todos los elementos
    """

    # Inicializa una lista llamada 'lista_formateada' para almacenar los elementos formateados.
    # ^ Utiliza un f-string para formatear cada número de la lista con el ancho especificado.
    lista_formateada = [f"{num:{ancho}}" for num in lista]

    # Concatena todos los elementos formateados con comas y los encierra entre corchetes.
    return '[' + ', '.join(lista_formateada) + ']'

def matriz_distancias_minimas(M):
    # Llamar a la función Dijkstra con la matriz de adyacencia
    resultados = dijkstra(M)

    # Imprimir los resultados
    for fila in resultados:
        print (fila)


def printear_matrices(M):
    n = len(M)
    for i in range(n):
        print(M[i])
    print(" ")





def calcular_tiempo_promedio(Ordenacion_func, repeticiones_umbral, func_type,n):    # Realizar repeticiones de inicialización + algoritmo K veces, es decir, repetir el cálculo del algoritmo K veces y para eso necesitas inicializar el vector K veces también, sino inicializas el vector, el algoritmo siempre iteraría las K veces sobre el vector ordenado
   import time

   # Mide el tiempo de ejecución total de Ordenacion_func ejecutado en un vector inicializado repeticiones_umbral veces

   ta = time.perf_counter_ns()                  # Tiempo antes de comenzar la ejecución
   for _ in range(repeticiones_umbral):         # Inicializa un vector y ejecuta el algoritmo de ordenación en ese vector repeticiones_umbral veces
      matriz = matrizAleatoria(n)         # Ejecuta el algoritmo en esa iteración (n) un numero k de veces para cerciorarte de que el algoritmo es correcto, por eso tienes que pasarle a esta función todo lo necesario para volver a ejecutar esa misma ejecución n numero de veces, medir su tiempo y hacer la media del tiempo de las diferentes ejecuciones
      dijkstra(matriz)       
   tb = time.perf_counter_ns()                  # Tiempo después de finalizar todas las ejecuciones

   t1 = tb - ta                                 # Tiempo total de la ejecución = Tiempo al finalizar todas las ejecuciones - Tiempo antes de comenzar la ejecución


   # Mide el tiempo de inicialización sola del vector (sin ejecutar el algoritmo) también repetido repeticiones_umbral veces

   ta = time.perf_counter_ns()                  # Tiempo antes de comenzar la ejecución
   for _ in range(repeticiones_umbral):         # Realiza un bucle for que inicializa un vector repeticiones_umbral veces
      matriz = matrizAleatoria(n)
   tb = time.perf_counter_ns()                  # Tiempo después de finalizar todas las ejecuciones
   
   t2 = tb - ta                                 # Tiempo de inicialización

   t = (t1 - t2) / repeticiones_umbral          # Resta el tiempo de inicialización para almacenar solo con el del algoritmo y después lo divides entre las K repeticiones para obtener el promedio del tiempo necesario para ejecutar el algoritmo
   return t                                     # Devuelve el tiempo promedio

def calcular_tiempo_ejecucion(func, matriz):    # Medir el tiempo de ejecución de una función (que representa un algoritmo) cuando se le proporciona un vector como entrada
    import time

    inicio = time.perf_counter_ns()     # Registra el tiempo de inicio antes de ejecutar la función del algoritmo
    func(matriz)                        # Ejecuta la función del algoritmo para un vector dado
    fin = time.perf_counter_ns()        # Registra el tiempo de finalización después de ejecutar la función
    return fin - inicio                 # Calcula y devuelve el tiempo transcurrido en nanosegundos

def cotas_ajustadas(alg, n, tiempo, exp1, exp2, exp3):   # Calcula las cotas  
    if alg==1:
    # Calcula las cotas subestimada, ajustada y sobrestimada en función de los parámetros dados
        cota_subestimada= tiempo / (n ** exp1)
        cota_ajustada = tiempo / (n ** exp2)
        cota_sobrestimada = tiempo / (n ** exp3)
    
    if alg==2:
        import math
        # Calcula las cotas subestimada, ajustada y sobrestimada en función de los parámetros dados
        cota_subestimada = tiempo / (n ** 1)  # Utiliza log base 2 para n log(n)
        cota_ajustada = tiempo / (n * math.log(n, 2))
        cota_sobrestimada = tiempo / (n ** 1.3) # Otra cota posible sería 1.3, se eligió 1.5 para ver más claramente los valores

    # Devuelve una cadena formateada con las cotas y el tamaño del vector
    return f"{n:>10}\t\t{tiempo:>15.4f}       {cota_subestimada:>15.6f}{cota_ajustada:>15.6f}{cota_sobrestimada:>15.6f}"

#______________________________________
