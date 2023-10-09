def aleatorio(n):
    
    import random
    v=list(range(n))                    # Crear una lista de números en el rango [0, n-1]
    for i in v:                         # Iterar sobre la lista y asignar números enteros aleatorios entre -n y n
        v[i] = random.randint(-n, n)
    return v                            # Devolver la lista con valores aleatorios

def vector_ordenado_aleatorio(n,orden):

    v = aleatorio(n)  # Genera un vector de números aleatorios en el rango [-n, n]
    if orden =="ascendente":
      return sorted(v)  # Ordena el vector de forma ascendente
    elif orden =="descendente":
      return sorted(v, reverse=True)  # Ordena el vector de forma descendente
    else:
       ValueError
#-------------------------------------------
def calcular_tiempo_promedio(func, inicializar_func, vector, repeticiones_umbral):
    
   import time
   inicio = time.perf_counter_ns()     # Registra el tiempo de inicio antes de ejecutar la función del algoritmo
   func(vector)                        # Ejecuta la función del algoritmo para un vector dado
   fin = time.perf_counter_ns()        # Registra el tiempo de finalización después de ejecutar la función
   t= fin - inicio                     # Calcula y devuelve el tiempo transcurrido en nanosegundos

   if t < 1000:
        # Realizar repeticiones del algoritmo K veces
        ta = time.perf_counter_ns()
        for _ in range(repeticiones_umbral):
            inicializar_func(vector)
            func(vector)
        tb = time.perf_counter_ns()
        t1 = tb - ta
        
        ta = time.perf_counter_ns()
        for _ in range(repeticiones_umbral):
            inicializar_func(vector)
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