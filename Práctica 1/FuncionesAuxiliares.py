import time

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
    print(lista_formateada, "\t", a, "\t", b, "\t", a == b)


def aleatorio(n):
    """
    Genera un vector de longitud n con números pseudoaleatorios en el rango [-n, n]
    """
    import random
    v=list(range(n))
    for i in v:
        v[i] = random.randint(-n, n)
    return v


def calcular_tiempo_promedio(algoritmo_func, vector, repeticiones):

    tiempos = []

    for _ in range(repeticiones):
        
        inicio = time.perf_counter_ns()
        algoritmo_func(vector)
        fin = time.perf_counter_ns()
        tiempos.append(fin - inicio)

    return sum(tiempos) / repeticiones