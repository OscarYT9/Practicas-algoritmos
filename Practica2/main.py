# Importa las funciones desde los otros archivos
from FuncionesTests import *


def test(iteraciones):
    for i in range(iteraciones):
        print(f"\nTest 4 (Análisis de Complejidad): (Iteración nº {i+1})")
        test_tiempo_complejidad(1 ,"alet")
# Llama a las funciones que deseas ejecutar
if __name__ == "__main__":
    #Puedes elegir el número de iteraciones que deseas.
    test(5)
