from Algoritmos import *            #Importamos los algoritmos a probar
from FuncionesAuxiliares import *   #Importamos las funciones auxiliares necesarias para la ejecución de las pruebas

# Estamos definiendo estas variables como globales, ya que usamos los mismos valores para cada prueba pero podrían establecerse como parametros de entrada de la función en caso de querer probar con otras convinaciones

tamanos_n = [500, 1000, 2000, 4000, 8000, 16000, 32000, 64000, 128000, 256000, 512000, 1024000]   # Lista con los tamaños del vector aleatorio, es una progresión geométrica de razón 2, si se quisiese se podría automatizar su creación también, en este caso no lo hacemos ya que con esos valores deberia ser suficiente para comprobar la complejidad algorítmica
umbral_confianza = 1000                                          # El tiempo en us (microsegundos) en el cual no nos podemos fiar de los valores obtenidos y habrá que realizar varias iteraciones y hacer el promedio de las mismas para asegurarnos de obtener valores correctos.
repeticiones_umbral = 1000                                         # Número iteraciones una vez superado el umbral de tiempo

#-------------------------------------------------------------------------------------------------------------------------
def test_tiempo_complejidad_crearMonticulo(orden, exp1, exp2, exp3):
    '''
    Permite comprobar el tiempo de ejecución del algoritmo para cada caso del vector y además nos ayuda a demostrar su complejidad de manera empírica gracias al cálculo del tiempo de ejecución entre las cotas.
    '''

    print(f"{'Subestimada':>64}{'Ajustada':>12}{'Sobreestimada':>15}")
    print(f"{'n':>12}\t\t{'t(n) (ns)':>15}{'t(n)/n^'+str(exp1):>22}{'t(n)/n^'+str(exp2):>15}{'t(n)/n^'+str(exp3):>15}")

    
    # Iteramos sobre diferentes tamaños de entrada
    for n in tamanos_n:
        
        tiempo_ejecucion = calcular_tiempo_ejecucion(n, orden)  # Calculamos el tiempo de ejecución del algoritmo para ese vector

        if tiempo_ejecucion < umbral_confianza * 1000:                          # Comprobamos si el tiempo de ejecución está por debajo de un umbral de confianza (y pasamos el umbral de us a ns)

            tiempo_promedio = calcular_tiempo_promedio(repeticiones_umbral, n, orden)                           # Calculamos el tiempo promedio para varias repeticiones
            print("*",cotas_ajustadas(n, tiempo_promedio, exp1, exp2, exp3),f"(promedio de {repeticiones_umbral} repeticiones)")    # Imprimimos el resultado con un asterisco para indicar el promedio

        else:
            print(" ",cotas_ajustadas(n, tiempo_ejecucion, exp1, exp2, exp3))    # Imprimimos el tiempo de ejecución normal


def test_tiempo_complejidad_ordenacionPorMonticulos(orden):
    '''
    Permite comprobar el tiempo de ejecución del algoritmo para cada caso del vector y además nos ayuda a demostrar su complejidad de manera empírica gracias al cálculo del tiempo de ejecución entre las cotas.
    '''

    print(f"{'Subestimada':>64}{'Ajustada':>12}{'Sobreestimada':>15}")
    print(f"{'n':>12}\t\t{'t(n) (ns)':>15}{'t(n)/n*1'}{'t(n)/n^log(n)'}{'t(n)/n^2'}")

    
    # Iteramos sobre diferentes tamaños de entrada
    for n in tamanos_n:
        
        tiempo_ejecucion = calcular_tiempo_ejecucion_ordenacionPorMonticulos(n, orden)  # Calculamos el tiempo de ejecución del algoritmo para ese vector

        if tiempo_ejecucion < umbral_confianza * 1000:                          # Comprobamos si el tiempo de ejecución está por debajo de un umbral de confianza (y pasamos el umbral de us a ns)

            tiempo_promedio = calcular_tiempo_promedio_ordenacionPorMonticulos(repeticiones_umbral, n, orden)                           # Calculamos el tiempo promedio para varias repeticiones
            print("*",cotas_ajustadas_ordenacionPorMonticulos(n, tiempo_promedio),f"(promedio de {repeticiones_umbral} repeticiones)")    # Imprimimos el resultado con un asterisco para indicar el promedio

        else:
            print(" ",cotas_ajustadas_ordenacionPorMonticulos(n, tiempo_ejecucion))    # Imprimimos el tiempo de ejecución normal