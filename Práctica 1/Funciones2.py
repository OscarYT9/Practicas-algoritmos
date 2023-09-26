from Tests import *

# 3. Determine los tiempos de ejecución con vectores aleatorios de tamaño n. Para el primer algoritmo
# n será igual a 500,1000,2000,4000 y 8000; para el segundo algoritmo añada también los valores
# 16000,32000,64000,128000 y 256000. Use el código de la figura 3 para obtener la hora del sistema.
# Para generar los datos de prueba utilice el código de la figura 1 que genera vectores de números
# pseudoaleatorios en el rango [−n,...,n].

import time

def test1():
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

def test2():
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

# Llama a las funciones de prueba
def ejecutar_pruebas(veces):
    tiempo_total_ejecucion1 = 0  # Inicializamos el tiempo total del Algoritmo 1 en 0
    tiempo_total_ejecucion2 = 0  # Inicializamos el tiempo total del Algoritmo 2 en 0

    for _ in range(veces):
        print("Ejecución ", _ + 1)
        print("------------")

        # Pruebas Algoritmo 1
        inicio1 = time.perf_counter_ns()
        test1()
        fin1 = time.perf_counter_ns()
        tiempo_ejecucion1 = fin1 - inicio1
        tiempo_total_ejecucion1 += tiempo_ejecucion1

        # Pruebas Algoritmo 2
        inicio2 = time.perf_counter_ns()
        test2()
        fin2 = time.perf_counter_ns()
        tiempo_ejecucion2 = fin2 - inicio2
        tiempo_total_ejecucion2 += tiempo_ejecucion2
        
        print("-" * 20)

    # Calcular la media de los tiempos de ejecución
    media_ejecucion1 = tiempo_total_ejecucion1 / veces
    media_ejecucion2 = tiempo_total_ejecucion2 / veces

    # Imprimir la media de los tiempos
    print("Media de Tiempos:")
    print("Algoritmo 1:", media_ejecucion1, "nanosegundos")
    print("Algoritmo 2:", media_ejecucion2, "nanosegundos")

# Uso: ejecuta ambas pruebas 3 veces y calcula la media
ejecutar_pruebas(3)


# def ejecutar_pruebas(veces):
#     for _ in range(veces):
#         print("Ejecución ", _ + 1)
#         print("------------")
#         print("Pruebas Algoritmo 1:")
#         test1()
#         print("Pruebas Algoritmo 2:")
#         test2()
#         print("-" * 20)




def analizar_complejidad():
    tamanos_n = [500, 1000, 2000, 4000, 8000, 16000, 32000, 64000, 128000, 256000]

    print("{:<10} {:<10} {:<10} {:<10} {:<10}".format("n", "t(n)", "t(n)/n**1.8", "t(n)/n**2.0", "t(n)/n**2.2"))
    for n in tamanos_n:
        tiempo = test1(sumaSubMax1, n)
        t_div_1_8 = tiempo / (n ** 1.8)
        t_div_2 = tiempo / (n ** 2.0)
        t_div_2_2 = tiempo / (n ** 2.2)
        print("{:<10} {:<10.3f} {:<10.3f} {:<10.3f} {:<10.3f}".format(n, tiempo, t_div_1_8, t_div_2, t_div_2_2))

    print("\n{:<10} {:<10} {:<10} {:<10} {:<10}".format("n", "t(n)", "t(n)/n**0.8", "t(n)/n", "t(n)/n**1.2"))
    for n in tamanos_n:
        tiempo = test2(sumaSubMax2, n)
        t_div_0_8 = tiempo / (n ** 0.8)
        t_div_1 = tiempo / n
        t_div_1_2 = tiempo / (n ** 1.2)
        print("{:<10} {:<10.3f} {:<10.3f} {:<10.3f} {:<10.3f}".format(n, tiempo, t_div_0_8, t_div_1, t_div_1_2))

analizar_complejidad()