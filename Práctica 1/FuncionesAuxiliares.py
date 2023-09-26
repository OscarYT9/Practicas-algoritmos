
def imprimirVector (test_case,a, b):
    '''
    Imprimimos el arreglo de entrada, las sumas calculadas y hacemos una comparación (operación constante) para comprobar si los resultados son iguales
    '''
    numeros_formateados = ["{:>{}}".format(numero, 5) for numero in test_case]
    cadena_formateada = " ".join(numeros_formateados)
    print(cadena_formateada,"\t",a,"\t\t",b,"\t\t",a==b)
    
