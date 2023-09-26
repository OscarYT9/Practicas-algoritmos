from Tests import *
from Algoritmos import *
import time

# 3. Determine los tiempos de ejecución con vectores aleatorios de tamaño n. Para el primer algoritmo
# n será igual a 500,1000,2000,4000 y 8000; para el segundo algoritmo añada también los valores
# 16000,32000,64000,128000 y 256000. Use el código de la figura 3 para obtener la hora del sistema.
# Para generar los datos de prueba utilice el código de la figura 1 que genera vectores de números
# pseudoaleatorios en el rango [−n,...,n].


tamanos_n = [500, 1000, 2000, 4000, 8000, 16000, 32000, 64000, 128000, 256000]

def test3():
    print("Algoritmo 1")
    print("Tamaño de n\tTiempo de ejecución (ns)")

    for n in tamanos_n[0:5]:
        vector = aleatorio(n)
        
        inicio = time.perf_counter_ns()
        sumaSubMax1(vector)
        fin = time.perf_counter_ns()
        tiempo_ejecucion1 = fin - inicio

        print(f"{n}\t\t\t{tiempo_ejecucion1}")
    print()  # Imprimir una línea en blanco al final



def test4():
    print("Algoritmo 2")
    print("Tamaño de n\tTiempo de ejecución (ns)")

    for n in tamanos_n:
        vector = aleatorio(n)
        
        inicio = time.perf_counter_ns()
        sumaSubMax2(vector)
        fin = time.perf_counter_ns()
        tiempo_ejecucion2 = fin - inicio

        print(f"{n}\t\t\t{tiempo_ejecucion2}")
    print()  # Imprimir una línea en blanco al final

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
def analizar_complejidad_sumaSubMax1(tamanos_n):
    print(f"{'n':<10}{'t(n) (ns)':<15}{'t(n)/n^1.8':<15}{'t(n)/n^2.0':<15}{'t(n)/n^2.2':<15}")
    for n in tamanos_n[0:5]:
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


def analizar_complejidad_sumaSubMax2(tamanos_n):
    print(f"{'n':<10}{'t(n) (ns)':<15}{'t(n)/n^1.8':<15}{'t(n)/n^2.0':<15}{'t(n)/n^2.2':<15}")
    for n in tamanos_n:
        vector = aleatorio(n)
        
        inicio = time.perf_counter_ns()
        sumaSubMax2(vector)
        fin = time.perf_counter_ns()
        tiempo_ejecucion = fin - inicio

        t_n = tiempo_ejecucion

        t_n_divided_1_8 = t_n / (n ** 0.8)
        t_n_divided_2_0 = t_n / (n)
        t_n_divided_2_2 = t_n / (n ** 1.2)

        print(f"{n:<10}{t_n:<15}{t_n_divided_1_8:<15.6f}{t_n_divided_2_0:<15.6f}{t_n_divided_2_2:<15.6f}")


# Llama a la función para analizar la complejidad
print("SumaSubMax1")
analizar_complejidad_sumaSubMax1(tamanos_n)
print("SumaSubMax2")
analizar_complejidad_sumaSubMax2(tamanos_n)