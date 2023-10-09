#Funciones para comprobar los algoritmos
from Algoritmos import *            #Importamos los algoritmos a probar
from FuncionesAuxiliares import *   #Importamos las funciones auxiliares necesarias para la ejecución de las pruebas

# 2. Valide el correcto funcionamiento de la implementación. La salida debería ser como sigue:

def ordenado(v):
    for i in range(len(v) - 1):
        if v[i] > v[i + 1]:
            return False
    return True

#v = [1, 2]
#print(ordenado(v))  # True, la lista está ordenada ascendentemente
#print(aleatorio(17))
#_______________________________________________________________________________________________________________________________________________________________________________________________________________________________


# 3. Determine los tiempos de ejecución para distintos tamaños del vector y para tres diferentes situaciones iniciales: (a) el vector ya está ordenado en orden ascendente, (b) el vector ya está ordenado pero
# en orden descendente, y (c) el vector está inicialmente desordenado (inicialización aleatoria). Para las
# inicializaciones (a) y (b), se recomienda consultar el funcionamiento de la función numpy.arange.

tamanos_n=[128, 256, 512, 1024, 2048, 4096, 8192, 16384] # Lista con los tamaños del vector aleatorio, es una progresión geométrica de razón 2, si se quisiese se podría automatizar su creación también, en este caso no lo hacemos ya que con esos valores deberia ser suficiente para comprobar la complejidad algorítmica
umbral_confianza = 1000                                                       
repeticiones_umbral = 10 

#a =[1,2,3,4]
#b= [4,2,3,1]
n = 10  # Cambia este valor según tus necesidades
vector_asc = vector_ordenado_aleatorio(n,"ascendente")
vector_desc = vector_ordenado_aleatorio(n,"descendente")
vector_alet = aleatorio(n)
#print(vector_asc, vector_desc, vector_alet)



tamanos_n = [128, 256, 512, 1024, 2048, 4096, 8192, 16384]       # Lista con los tamaños del vector aleatorio, es una progresión geométrica de razón 2, si se quisiese se podría automatizar su creación también, en este caso no lo hacemos ya que con esos valores deberia ser suficiente para comprobar la complejidad algorítmica
umbral_confianza = 1000                                          # El tiempo en us (microsegundos) en el cual no nos podemos fiar de los valores obtenidos y habrá que realizar varias iteraciones y hacer el promedio de las mismas para asegurarnos de obtener valores correctos.
repeticiones_umbral = 10                                         # Número iteraciones una vez superado el umbral de tiempo

#-------------------------------------------------------------------------------------------------------------------------
def test_tiempo_complejidad(algoritmo, inicializar_func, vector):
    """
     Parámetros
     ----------
     algoritmo: 
        valor de tipo entero que define si estamos trabajando con la función sumaSubMax1 o sumaSubMax2

     imprimir_solo_tiempo:
        valor de tipo entero que se usa en los tiempos de ejecución

     Qué hace la función?
     ----------
        comprueba los algoritmos 1 y 2 e imprime por pantalla los valores de los tiempos de ejecución o los 
        tiempos de ejecución aplicando las cotas sobreestimada, ajustada y subestimada
        Utiliza las funciones auxiliares calcular_tiempo_ejecucion(), aleatorio(n), calcular_tiempo_promedio() y cotas_ajustadas()
     Devuelve
     -------
        los valores de los tiempos de ejecución en nanosegundos para cada n
    """
    
    # Comprobamos el valor del parámetro algoritmo y configuramos las variables en consecuencia
    if algoritmo == 1:
        algoritmo_str = "***ins_sort***"
        tamanos = tamanos_n  # Limitar tamaños para Algoritmo 1
        Ordenacion_func = ins_sort
        exp1=1.8
        exp2=2
        exp3=2.2

    elif algoritmo == 2:
        algoritmo_str = "***shell_sort_hibbard***"
        tamanos = tamanos_n
        Ordenacion_func = shell_sort_hibbard
        exp1=0.8
        exp2=1
        exp3=1.2
        
    else:
        raise ValueError("El valor de algoritmo debe ser 1 o 2.")

    # Imprimimos el nombre del algoritmo actual y las cabeceras de las columnas
    print(algoritmo_str)

    print(f"{'Subestimada':>64}{'Ajustada':>12}{'Sobreestimada':>15}")
    print(f"{'n':>12}\t\t{'t(n) (ns)':>15}{'t(n)/n^'+str(exp1):>22}{'t(n)/n^'+str(exp2):>15}{'t(n)/n^'+str(exp3):>15}")

    # Iteramos sobre diferentes tamaños de entrada
    for n in tamanos:                                                                                       #Creamos un vector de ese tamaño de entrada
        tiempo_ejecucion = calcular_tiempo_ejecucion (Ordenacion_func,vector)                               # Calculamos el tiempo de ejecución del algoritmo para ese vector
        
        if tiempo_ejecucion < umbral_confianza * 1000:                                                      # Comprobamos si el tiempo de ejecución está por debajo de un umbral de confianza (y pasamos el umbral de us a ns)

            tiempo_promedio = calcular_tiempo_promedio(Ordenacion_func, inicializar_func, vector, repeticiones_umbral)        # Calculamos el tiempo promedio para varias repeticiones
            print("*",cotas_ajustadas(n, tiempo_promedio, exp1, exp2, exp3),f"(promedio de {repeticiones_umbral} repeticiones)")    # Imprimimos el resultado con un asterisco para indicar el promedio

        else:
            print(" ",cotas_ajustadas(n, tiempo_ejecucion, exp1, exp2, exp3))               # Imprimimos el tiempo de ejecución normal

# Realmente esta última función podría simplificarse si se imprimiese el tiempo + cotas, pero como en el apartado 3. de la práctica pide exclusivamente el tiempo de ejecución hemos decidido incluir la opción de poder elegir si se quiere imprimir solo el tiempo, o el tiempo + las cotas para mayor comodidad