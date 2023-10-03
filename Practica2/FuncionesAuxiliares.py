def aleatorio(n):
    """
     Parámetros
     ----------
     n: 
        valor de tipo int que reprsenta el tamaño del vector aleatorio

     Qué hace la función?
     ----------
        Genera un vector de longitud n con números pseudoaleatorios en el rango [-n, n]
     Devuelve
     -------
       El vector aleatorio generado
    """
    
    import random
    v=list(range(n))                    # Crear una lista de números en el rango [0, n-1]
    for i in v:                         # Iterar sobre la lista y asignar números enteros aleatorios entre -n y n
        v[i] = random.randint(-n, n)
    return v                            # Devolver la lista con valores aleatorios