from Algoritmos import *            #Importamos los algoritmos a probar
from FuncionesAuxiliares import *   #Importamos las funciones auxiliares necesarias para la ejecución de las pruebas

#definición del primer caso de prueba
matriz_caso_1 = [
     [0, 1, 8, 4, 7],
     [1, 0, 2, 6, 5],
     [8, 2, 0, 9, 5],
     [4, 6, 9, 0, 3],
     [7, 5, 5, 3, 0]
        ]
#definición del segundo caso de prueba
matriz_caso_2 = [
     [0, 1, 4, 7],
     [1, 0, 2, 8],
     [4, 2, 0, 3],
     [7, 8, 3, 0],
        ]


def test_matrices_minimas():
     #se encarga de mostrar en la terminal los resultados del algoritmo dijkstra
     print("TEST 1")
     print("Matriz del caso 1:")
     printear_matrices(matriz_caso_1)
     print("Calculamos la matriz de adyacencia de caminos de peso mínimo para la matriz del caso 1:")
     matriz_distancias_minimas(matriz_caso_1)
     print(" ")

     print("Matriz del caso 2:")
     printear_matrices(matriz_caso_2)
     print("Calculamos la matriz de adyacencia de caminos de peso mínimo para la matriz del caso 2:")
     matriz_distancias_minimas(matriz_caso_2)

     print("Matriz aleatoria:")
     a = matrizAleatoria(10)
     printear_matrices(a)
     print("Calculamos la matriz de adyacencia de caminos de peso mínimo para una matriz aleatoria:")
     matriz_distancias_minimas(a)
    

tamanos_n = [10, 20, 40, 80, 160, 320, 640]   # Lista con los tamaños del vector aleatorio, es una progresión geométrica de razón 2, si se quisiese se podría automatizar su creación también, en este caso no lo hacemos ya que con esos valores deberia ser suficiente para comprobar la complejidad algorítmica
umbral_confianza = 1000                                          # El tiempo en us (microsegundos) en el cual no nos podemos fiar de los valores obtenidos y habrá que realizar varias iteraciones y hacer el promedio de las mismas para asegurarnos de obtener valores correctos.
repeticiones_umbral = 1000                                         # Número iteraciones una vez superado el umbral de tiempo
#Función complejidad
#________________________________________________________________________________________________________________________________________________________________________________________________________________________________
def test_tiempo_complejidad(exp1, exp2, exp3):
     '''
     Permite comprobar el tiempo de ejecución del algoritmo para cada caso del vector y además nos ayuda a demostrar su complejidad de manera empírica gracias al cálculo del tiempo de ejecución entre las cotas.
     '''
     
     # Iteramos sobre diferentes tamaños de entrada
     for n in tamanos_n:
         matriz = matrizAleatoria(n)
         tiempo_ejecucion = calcular_tiempo_ejecucion(matriz)  # Calculamos el tiempo de ejecución del algoritmo para ese vector

         if tiempo_ejecucion < umbral_confianza * 1000:                          # Comprobamos si el tiempo de ejecución está por debajo de un umbral de confianza (y pasamos el umbral de us a ns)

             tiempo_promedio = calcular_tiempo_promedio(repeticiones_umbral, n)                           # Calculamos el tiempo promedio para varias repeticiones
             print("*",cotas_ajustadas(n, tiempo_promedio, exp1, exp2, exp3),f"(promedio de {repeticiones_umbral} repeticiones)")    # Imprimimos el resultado con un asterisco para indicar el promedio

         else:
             print(" ",cotas_ajustadas(n, tiempo_ejecucion, exp1, exp2, exp3))    # Imprimimos el tiempo de ejecución normal

#______________________________________________________________
#Funciones que imprimen las tablas
def imprimir_complejidad(exp1, exp2, exp3):
    print(" ")
    print(f"{'Subestimada':>64}{'Ajustada':>12}{'Sobreestimada':>15}")
    print(f"{'n':>12}\t\t{'t(n) (ns)':>15}{'t(n)/n^'+str(exp1):>22}{'t(n)/n^'+str(exp2):>15}{'t(n)/n^'+str(exp3):>15}")
    test_tiempo_complejidad(exp1, exp2, exp3)
