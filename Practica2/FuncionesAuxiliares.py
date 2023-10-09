
def vector_ordenado_aleatorio(n,orden):

    if orden =="ascendente":
      v=list(range(n))
      return sorted(v)  # Ordena el vector de forma ascendente
    
    elif orden =="descendente":
      v=list(range(n))
      return sorted(v, reverse=True)  # Ordena el vector de forma descendente
    
    elif orden =="aleatorio":
         import random
         v=list(range(n))                    # Crear una lista de números en el rango [0, n-1]
         for i in v:                         # Iterar sobre la lista y asignar números enteros aleatorios entre -n y n
            v[i] = random.randint(-n, n)
         return v

#Funciones de inicialización
def inicializar(v, func_type):
   import random
   if func_type == "alet":
     random.shuffle(v)
   elif func_type == "desc":
     sorted(v)
   elif func_type == "asc":
     sorted(v, reverse=True)

#-------------------------------------------
def calcular_tiempo_promedio(Ordenacion_func, vector, repeticiones_umbral, func_type):
    
   import time
   # Realizar repeticiones del algoritmo K veces
   ta = time.perf_counter_ns()
   for _ in range(repeticiones_umbral):
      inicializar(vector, func_type)
      Ordenacion_func(vector)
   tb = time.perf_counter_ns()

   t1 = tb - ta

   ta = time.perf_counter_ns()
   for _ in range(repeticiones_umbral):
      inicializar(vector, func_type)
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