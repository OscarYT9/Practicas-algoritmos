#Funciones para comprobar los algoritmos
from Algoritmos import *            #Importamos los algoritmos a probar
from FuncionesAuxiliares import *   #Importamos las funciones auxiliares necesarias para la ejecución de las pruebas

# 2. Valide que los algoritmos funcionan correctamente. Chequee las siguientes secuencias:
 # Definimos una lista con los vectores de prueba que consisten en arreglos de números enteros.
test_cases=[[-9,2,-5,-4,6], 
            [4,0,9,2,5],
            [-2,-1,-9,-7,-1],
            [9,-2,1,-7,-8],
            [15,-2,-5,-4,16],
            [7,-5,6,7,-7]]

# 2.1 Así mismo realice una segunda comprobación con vectores generados de forma aleatoria (función aleatorio) comprobando que ambos algoritmos devuelven el mismo resultado:
# Generamos una lista de 9 vectores aleatorios utilizando la función aleatorio(n) que nos proporciona un vector de n elementos con valores desde n hasta -n [-n,...,n], necesitamos 10 vectores así, por lo que usamos el for _ in range(9) (0.....9)
vectores_aleatorios = [aleatorio(9) for _ in range(9)]    

#-------------------------------------------------------------------------------------------------------------------------
def test1(lista):

    for vector in lista:                                      # Iteramos en la lista a través de los vectores dentro de ella.
        result_algo1 = sumaSubMax1(vector)                    # Calculamos la suma máxima usando el Algoritmo 1.
        result_algo2 = sumaSubMax2(vector)                    # Calculamos la suma máxima usando el Algoritmo 2.
        imprimirVector(vector, result_algo1, result_algo2)    # Llamamos a la función auxiliar que nos imprimirá cada vector y el resultado de la Suma de la Subsecuencia Máxima.

#Se podrían crear varias funciones para iterar las dos listas, pero es más legible si se crea una sola, ya que solo cambias la lista de entrada de la función
#...
# def test2():
#     for i in range(0, 10):
#         v = aleatorio(9)
#         x = sumaSubMax1(v)
#         y = sumaSubMax2(v)
#         print('{0:0d}{1:0d} - {2}'.format(x, y, x==y))
#     print()
#...
#_______________________________________________________________________________________________________________________________________________________________________________________________________________________________


# 3. Determine los tiempos de ejecución con vectores aleatorios de tamaño n. Para el primer algoritmo
# n será igual a 500,1000,2000,4000 y 8000; para el segundo algoritmo añada también los valores
# 16000,32000,64000,128000 y 256000. Use el código de la figura 3 para obtener la hora del sistema.
# Para generar los datos de prueba utilice el código de la figura 1 que genera vectores de números
# pseudoaleatorios en el rango [−n,...,n].

tamanos_n = [500, 1000, 2000, 4000, 8000, 16000, 32000, 64000, 128000, 256000] # Lista con los tamaños del vector aleatorio, es una progresión geométrica de razón 2, si se quisiese se podría automatizar su creación también, en este caso no lo hacemos ya que con esos valores deberia ser suficiente para comprobar la complejidad algorítmica
umbral_confianza = 1000 # El tiempo en us (microsegundos) en el cual no nos podemos fiar de los valores obtenidos y habrá que realizar varias iteraciones y hacer el promedio de las mismas para asegurarnos de obtener valores correctos.
repeticiones_umbral = 10 # Número iteraciones una vez superado el umbral de tiempo

#-------------------------------------------------------------------------------------------------------------------------
def test_tiempo_ejecucion(algoritmo):

    # Comprobamos el valor del parámetro algoritmo y configuramos las variables en consecuencia
    if algoritmo == 1:
        algoritmo_str = "***Algoritmo 1***"
        tamanos = tamanos_n[:5]       # Limitar tamaños para Algoritmo 1
        sumaSubMax_func = sumaSubMax1

    elif algoritmo == 2:
        algoritmo_str = "***Algoritmo 2***"
        tamanos = tamanos_n
        sumaSubMax_func = sumaSubMax2

    else:
        raise ValueError("El valor de algoritmo debe ser 1 o 2.")

    # Imprimimos el nombre del algoritmo actual
    print(algoritmo_str)
    print(f"{'Tamaño de n':>12}             {'Tiempo de ejecución (ns)':>15}")

    # Iteramos sobre diferentes tamaños de entrada
    for n in tamanos:
        vector = aleatorio(n)  #Creamos un vector de ese tamaño de entrada
        tiempo_ejecucion = calcular_tiempo_ejecucion (sumaSubMax_func, vector)  # Calculamos el tiempo de ejecución del algoritmo para ese vector

        if tiempo_ejecucion < umbral_confianza * 1000: # Comprobamos si el tiempo de ejecución está por debajo de un umbral de confianza (y pasamos el umbral de us a ns)

            tiempo_promedio = calcular_tiempo_promedio(sumaSubMax_func, vector, repeticiones_umbral) # Calculamos el tiempo promedio para varias repeticiones
            print(f"* {n:>10}\t\t{tiempo_promedio:>15.4f} (promedio de {repeticiones_umbral} repeticiones)") # Imprimimos el resultado con un asterisco para indicar el promedio

        else:
            print(f"  {n:>10}\t\t{tiempo_ejecucion:>15.4f}") # Imprimimos el tiempo de ejecución normal

            
#-------------------------------------------------------------------------------------------------------------------------
def analizar_complejidad(algoritmo):
        
        # Comprobamos el valor del parámetro algoritmo y configuramos las variables en consecuencia
        if algoritmo == 1:
            algoritmo_str = "***SumaSubMax1***"
            tamanos = tamanos_n[:5]  # Limitar tamaños para Algoritmo 1
            sumaSubMax_func = sumaSubMax1
            exp1=1.8
            exp2=2
            exp3=2.2

        elif algoritmo == 2:
            algoritmo_str = "***SumaSubMax2***"
            tamanos = tamanos_n
            sumaSubMax_func = sumaSubMax2
            exp1=0.8
            exp2=1
            exp3=1.2

        else:
            raise ValueError("El valor de algoritmo debe ser 1 o 2.")

        # Imprimimos el nombre del algoritmo actual y las cabeceras de las columnas
        print(algoritmo_str)
        print(f"{'n':>12}\t\t{'t(n) (ns)':>15}       {'t(n)/n^1.8':>15}{'t(n)/n^2.0':>15}{'t(n)/n^2.2':>15}")

        # Iteramos sobre diferentes tamaños de entrada
        for n in tamanos:
            vector = aleatorio(n) #Creamos un vector de ese tamaño de entrada
            tiempo_ejecucion = calcular_tiempo_ejecucion (sumaSubMax_func,vector) # Calculamos el tiempo de ejecución del algoritmo para ese vector
            
            if tiempo_ejecucion < umbral_confianza * 1000: # Comprobamos si el tiempo de ejecución está por debajo de un umbral de confianza (y pasamos el umbral de us a ns)
          
                tiempo_promedio = calcular_tiempo_promedio(sumaSubMax_func, vector, repeticiones_umbral) # Calculamos el tiempo promedio para varias repeticiones
                print("*",cotasAjustadas(n, tiempo_promedio, exp1, exp2, exp3),f"(promedio de {repeticiones_umbral} repeticiones)") # Imprimimos el resultado con un asterisco para indicar el promedio

            else:
                print(" ",cotasAjustadas(n, tiempo_ejecucion, exp1, exp2, exp3)) # Imprimimos el tiempo de ejecución normal
