def aleatorio(n):
    """
     Parámetros
     ----------
     n: 
        valor de tipo int que representa el tamaño del vector aleatorio

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


def vector_ordenado_aleatorio(n,orden):
    """
     Parámetros
     ----------
     n: 
        valor de tipo int que reprsenta el tamaño del vector ordenado

     Qué hace la función?
     ----------
        Genera un vector de longitud n con números aleatorios en el rango [-n, n], y luego lo ordena de forma ascendente.
     Devuelve
     -------
       El vector ordenado con números aleatorios generado
    """
    
    v = aleatorio(n)  # Genera un vector de números aleatorios en el rango [-n, n]
    if orden =="ascendente":
      return sorted(v)  # Ordena el vector de forma ascendente
    elif orden =="descendente":
      return sorted(v, reverse=True)  # Ordena el vector de forma descendente
    else:
       ValueError

