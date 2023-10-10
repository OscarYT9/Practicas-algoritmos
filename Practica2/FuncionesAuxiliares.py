

def aleatorio(n):
     
    import random
    v=list(range(n))                    # Crear una lista de números en el rango [0, n-1]
    for i in v:                         # Iterar sobre la lista y asignar números enteros aleatorios entre -n y n
        v[i] = random.randint(-n, n)
    return v    


def vector_ordenado_aleatorio(n,orden):

    if orden =="ascendente":
      v = list(range(1,n+1))
      return v
    
    elif orden =="descendente":
      v = list(range(n, 0, -1))
      return v
    
    elif orden =="aleatorio":
      v= aleatorio(n)
      return v

#Funciones de inicialización
def inicializar(vector, func_type, n):
    if func_type == "alet":
        vector = vector_ordenado_aleatorio(n, "aleatorio")
    elif func_type == "desc":
        vector = vector_ordenado_aleatorio(n, "descendente")
    elif func_type == "asc":
        vector = vector_ordenado_aleatorio(n, "ascendente")
    return vector
#Prefuntar sobre inicizalizar y preguntar si lo que hay que hacer es calcular el tiempo concreto, en ves de toda la función
#-------------------------------------------
def calcular_tiempo_promedio(Ordenacion_func, vector, repeticiones_umbral, func_type,n):
    
   import time
   # Realizar repeticiones del algoritmo K veces
   ta = time.perf_counter_ns()
   for _ in range(repeticiones_umbral):
      vector = inicializar(vector, func_type,n) #Ejecutas el algoritmo en esa iteración (n) un numero k de veces para cerciorarte de que el algoritmo es correcto, por eso tienes que pasarle a esta función todo lo necesario para volver a ejecutar esa misma ejecución n numero de veces, medir su tiempo y hacer la media del tiempo de las diferentes ejecuciones
      Ordenacion_func(vector)
   tb = time.perf_counter_ns()

   t1 = tb - ta

   ta = time.perf_counter_ns()
   for _ in range(repeticiones_umbral):
      vector = inicializar(vector, func_type,n)
   tb = time.perf_counter_ns()
   
   t2 = tb - ta
   t = (t1 - t2) / repeticiones_umbral
   return t

def calcular_tiempo_ejecucion(func, vector):
    
    import time
    inicio = time.perf_counter_ns()     # Registra el tiempo de inicio antes de ejecutar la función del algoritmo
    func(vector)                        # Ejecuta la función del algoritmo para un vector dado
    fin = time.perf_counter_ns()        # Registra el tiempo de finalización después de ejecutar la función
    return fin - inicio                 # Calcula y devuelve el tiempo transcurrido en nanosegundos


def cotas_ajustadas(n, tiempo, exp1, exp2, exp3):
    
   # Calcula las cotas subestimada, ajustada y sobrestimada en función de los parámetros dados
    cota_subestimada= tiempo / (n ** exp1)
    cota_ajustada = tiempo / (n ** exp2)
    cota_sobrestimada = tiempo / (n ** exp3)

    # Devuelve una cadena formateada con las cotas y el tamaño del vector
    return f"{n:>10}\t\t{tiempo:>15.4f}       {cota_subestimada:>15.6f}{cota_ajustada:>15.6f}{cota_sobrestimada:>15.6f}"