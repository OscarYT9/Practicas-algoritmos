from Tests import *
from Algoritmos import *

# 3. Determine los tiempos de ejecución con vectores aleatorios de tamaño n. Para el primer algoritmo
# n será igual a 500,1000,2000,4000 y 8000; para el segundo algoritmo añada también los valores
# 16000,32000,64000,128000 y 256000. Use el código de la figura 3 para obtener la hora del sistema.
# Para generar los datos de prueba utilice el código de la figura 1 que genera vectores de números
# pseudoaleatorios en el rango [−n,...,n].

import time

def test3():
    tamanos_n = [500, 1000, 2000, 4000, 8000]

    for n in tamanos_n:
        vector = aleatorio(n)
        
        inicio = time.perf_counter_ns()
        sumaSubMax1(vector)
        fin = time.perf_counter_ns()
        tiempo_ejecucion1 = fin - inicio

        print(f"Tamaño de n: {n}")
        print(f"Tiempo de ejecución Algoritmo 1: {tiempo_ejecucion1} nanosegundos")
        print()

def test4():
    tamanos_n = [500, 1000, 2000, 4000, 8000, 16000, 32000, 64000, 128000, 256000]

    for n in tamanos_n:
        vector = aleatorio(n)
        
        inicio = time.perf_counter_ns()
        sumaSubMax2(vector)
        fin = time.perf_counter_ns()
        tiempo_ejecucion2 = fin - inicio

        print(f"Tamaño de n: {n}")
        print(f"Tiempo de ejecución Algoritmo 2: {tiempo_ejecucion2} nanosegundos")
        print()

# def ejecutar_pruebas(veces):
#     for _ in range(veces):
#         print("Ejecución ", _ + 1)
#         print("------------")
#         print("Pruebas Algoritmo 1:")
#         test1()
#         print("Pruebas Algoritmo 2:")
#         test2()
#         print("-" * 20)
test3()
test4()


#-------------------------------------------------------------------------------------------------------------------------
def analizar_complejidad(n_valores):
    print(f"{'n':<10}{'t(n) (ns)':<15}{'t(n)/n^1.8':<15}{'t(n)/n^2.0':<15}{'t(n)/n^2.2':<15}")
    for n in n_valores:
        vector = aleatorio(n)
        
        inicio = time.perf_counter_ns()
        sumaSubMax1(vector)
        fin = time.perf_counter_ns()
        tiempo_ejecucion = fin - inicio

        t_n = tiempo_ejecucion

        t_n_divided_1_8 = t_n / (n ** 1.8)
        t_n_divided_2_0 = t_n / (n ** 2.0)
        t_n_divided_2_2 = t_n / (n ** 2.2)

        print(f"{n:<10}{t_n:<15}{t_n_divided_1_8:<15.6f}{t_n_divided_2_0:<15.6f}{t_n_divided_2_2:<15.6f}")

# Tamaños de n a probar
n_valores = [500, 1000, 2000, 4000, 8000]

# Llama a la función para analizar la complejidad
analizar_complejidad(n_valores)









