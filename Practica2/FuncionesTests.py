#Funciones para comprobar los algoritmos
from Algoritmos import *            #Importamos los algoritmos a probar
from FuncionesAuxiliares import *   #Importamos las funciones auxiliares necesarias para la ejecución de las pruebas

# 2. Valide el correcto funcionamiento de la implementación.

def ordenado(v):
    '''
    Comprueba que si el vector esta ordenado
    '''
    for i in range(len(v) - 1):
        if v[i] > v[i + 1]:
            return False
    return True


def probar_algoritmos(n):
    '''
    True, la lista está ordenada ascendentemente
    '''
    #Creamos los vectores para comprobar los algoritmos en los 6 casos
    vector_asc = vector_ordenado_aleatorio(n, "ascendente")
    vector_desc = vector_ordenado_aleatorio(n, "descendente")
    vector_alet = vector_ordenado_aleatorio(n, "aleatorio")

    print("Inicialización ascendente")
    print(vector_asc)
    print("Ordenado inicialmente?", ordenado(vector_asc))
    vector_asc=ins_sort(vector_asc)
    print("Ordenado con el algoritmo de inserción?", ordenado(vector_asc))
    vector_asc=shell_sort_hibbard(vector_asc)
    print("Ordenado con el algoritmo de Shell?", ordenado(vector_asc))
    # Llamar al algoritmo de ordenación aquí

    print("\nInicialización descendente")
    print(vector_desc)
    print("Ordenado inicialmente?", ordenado(vector_desc))
    vector_desc=ins_sort(vector_desc)
    print("Ordenado con el algoritmo de inserción?", ordenado(vector_desc))
    vector_desc=shell_sort_hibbard(vector_desc)
    print("Ordenado con el algoritmo de Shell?", ordenado(vector_desc))
    # Llamar al algoritmo de ordenación aquí

    print("\nInicialización aleatoria")
    print(vector_alet)
    print("Ordenado inicialmente?", ordenado(vector_alet))
    vector_alet=ins_sort(vector_alet)
    print("Ordenado con el algoritmo de inserción?", ordenado(vector_alet))
    vector_alet=shell_sort_hibbard(vector_alet)
    print("Ordenado con el algoritmo de Shell?", ordenado(vector_alet))
    # Llamar al algoritmo de ordenación aquí

#_______________________________________________________________________________________________________________________________________________________________________________________________________________________________


# 3. Determine los tiempos de ejecución para distintos tamaños del vector y para tres diferentes situaciones iniciales: (a) el vector ya está ordenado en orden ascendente, (b) el vector ya está ordenado pero
# en orden descendente, y (c) el vector está inicialmente desordenado (inicialización aleatoria). Para las
# inicializaciones (a) y (b), se recomienda consultar el funcionamiento de la función numpy.arange.

# Estamos definiendo estas variables como globales, ya que usamos los mismos valores para cada prueba pero podrían establecerse como parametros de entrada de la función en caso de querer probar con otras convinaciones

tamanos_n = [128, 256, 512, 1024, 2048, 4096, 8192, 16384]       # Lista con los tamaños del vector aleatorio, es una progresión geométrica de razón 2, si se quisiese se podría automatizar su creación también, en este caso no lo hacemos ya que con esos valores deberia ser suficiente para comprobar la complejidad algorítmica
umbral_confianza = 1000                                          # El tiempo en us (microsegundos) en el cual no nos podemos fiar de los valores obtenidos y habrá que realizar varias iteraciones y hacer el promedio de las mismas para asegurarnos de obtener valores correctos.
repeticiones_umbral = 10                                         # Número iteraciones una vez superado el umbral de tiempo

#-------------------------------------------------------------------------------------------------------------------------
def test_tiempo_complejidad(algoritmo, func_type, exp1, exp2, exp3):
    
    # Comprobamos el valor del parámetro algoritmo y configuramos las variables en consecuencia
    if algoritmo == 1:
        algoritmo_str = "***ins_sort***"
        tamanos = tamanos_n
        Ordenacion_func = ins_sort

    elif algoritmo == 2:
        algoritmo_str = "***shell_sort_hibbard***"
        tamanos = tamanos_n
        Ordenacion_func = shell_sort_hibbard
        
    else:
        raise ValueError("El valor de algoritmo debe ser 1 o 2.")


    # Imprimimos el nombre del algoritmo actual y las cabeceras de las columnas
    print(algoritmo_str)

    print(f"{'Subestimada':>64}{'Ajustada':>12}{'Sobreestimada':>15}")
    print(f"{'n':>12}\t\t{'t(n) (ns)':>15}{'t(n)/n^'+str(exp1):>22}{'t(n)/n^'+str(exp2):>15}{'t(n)/n^'+str(exp3):>15}")

    
    # Iteramos sobre diferentes tamaños de entrada
    for n in tamanos:
        
        #Iniciamos los vectores
        vector = inicializar(func_type,n)                                       #Creamos un vector de ese tamaño de entrada (asc, desc o alet)
        
        tiempo_ejecucion = calcular_tiempo_ejecucion (Ordenacion_func, vector)  # Calculamos el tiempo de ejecución del algoritmo para ese vector

        if tiempo_ejecucion < umbral_confianza * 1000:                          # Comprobamos si el tiempo de ejecución está por debajo de un umbral de confianza (y pasamos el umbral de us a ns)

            tiempo_promedio = calcular_tiempo_promedio(Ordenacion_func, repeticiones_umbral, func_type,n)                           # Calculamos el tiempo promedio para varias repeticiones
            print("*",cotas_ajustadas(n, tiempo_promedio, exp1, exp2, exp3),f"(promedio de {repeticiones_umbral} repeticiones)")    # Imprimimos el resultado con un asterisco para indicar el promedio

        else:
            print(" ",cotas_ajustadas(n, tiempo_ejecucion, exp1, exp2, exp3))    # Imprimimos el tiempo de ejecución normal