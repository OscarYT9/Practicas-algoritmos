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

def test1(lista):

    for vector in lista:                                      # Iteramos en la lista a través de los vectores.
        result_algo1 = sumaSubMax1(vector)                    # Calculamos la suma máxima usando el Algoritmo 1.
        result_algo2 = sumaSubMax2(vector)                    # Calculamos la suma máxima usando el Algoritmo 2.
        imprimirVector(vector, result_algo1, result_algo2)    # Llamamos a la función auxiliar que nos imprimirá cada vector.

    
#_______________________________________________________________________________________________________________________________________________________________________________________________________________________________
print("")
test1(test_cases)
print("")
test1(vectores_aleatorios)
#_______________________________________________________________________________________________________________________________________________________________________________________________________________________________
#Hacer funcion axiliar para imprimir bien el vector
#Hacer que en la misma ejecución saque varias veces las mismas tablas(para comprobar que están bien las mediciones)


# Imprimimos el vector aleatorio, las sumas calculadas y hacemos una comparación (operación constante) para comprobar si los resultados son iguales

#a mitad del desarrollo nos dimos cuenta que era mucho más eficiente crear una sola función para comprobar los vecores aleatorios y los definidos