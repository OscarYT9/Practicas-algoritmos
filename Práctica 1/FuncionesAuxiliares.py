#Funciones que se usan dentro de otras funciones.

def formatear_lista (lista, ancho):
    """
    Formatea una lista de números para que cada elemento ocupe un ancho específico y agrega corchetes alrededor de la lista.
    (Está función es solo para imprimir de forma legible los datos, no afecta a la velocidad de los 2 algoritmos, ya que se ejecuta una vez finalizados)
    """
    # Inicializa una lista llamada 'lista_formateada' para almacenar los elementos formateados.
    # ^ Utiliza un f-string para formatear cada número de la lista con el ancho especificado.
    lista_formateada = [f"{num:{ancho}}" for num in lista]

    # Concatena todos los elementos formateados con comas y los encierra entre corchetes.
    return '[' + ', '.join(lista_formateada) + ']'


def imprimirVector(test_case, a, b):
    """
    Imprime una lista de números, dos resultados y una comparación booleana.
    """
    # Llama a la función 'formatear_lista' para formatear la 'test_case' y almacena el resultado en 'lista_formateada'.
    lista_formateada = formatear_lista(test_case, 2)

    # Imprime la 'lista_formateada', los resultados 'a' y 'b' y la comparación booleana entre 'a' y 'b'.
    print(lista_formateada, "\t", a, "\t", b, "\t-", a == b)


def aleatorio(n):
    """
    Genera un vector de longitud n con números pseudoaleatorios en el rango [-n, n]
    """
    import random
    v=list(range(n))                    # Crear una lista de números en el rango [0, n-1]
    for i in v:                         # Iterar sobre la lista y asignar números enteros aleatorios entre -n y n
        v[i] = random.randint(-n, n)
    return v                            # Devolver la lista con valores aleatorios


def calcular_tiempo_ejecucion(func, vector):
    
    import time
    inicio = time.perf_counter_ns()     # Registra el tiempo de inicio antes de ejecutar la función del algoritmo
    func(vector)                        # Ejecuta la función del algoritmo para un vector dado
    fin = time.perf_counter_ns()        # Registra el tiempo de finalización después de ejecutar la función
    return fin - inicio                 # Calcula y devuelve el tiempo transcurrido en nanosegundos


def calcular_tiempo_promedio(func, vector, repeticiones):

    tiempo_total = 0
    for _ in range(repeticiones):
        # Suma los tiempos de ejecución de la función para un número especificado de repeticiones
        tiempo_total += calcular_tiempo_ejecucion(func, vector)

     # Calcula y devuelve el tiempo promedio en nanosegundos
    return tiempo_total / repeticiones


def cotasAjustadas(n, tiempo, exp1, exp2, exp3):
     # Calcula las cotas subestimada, ajustada y sobrestimada en función de los parámetros dados
    cota_subestimada= tiempo / (n ** exp1)
    cota_ajustada = tiempo / (n ** exp2)
    cota_sobrestimada = tiempo / (n ** exp3)

    # Devuelve una cadena formateada con las cotas y el tamaño del vector
    return f"{n:>10}\t\t{tiempo:>15.4f}       {cota_subestimada:>15.6f}{cota_ajustada:>15.6f}{cota_sobrestimada:>15.6f}"