#Algoritmos a comprobar
#1. Implemente en PYTHON los algoritmos de ordenación por inserción y ordenación Shell con incrementos de Hibbard.

def ins_sort(v):    # La función ordena el vector dado según el algoritmo de inserción

    for i in range(1,len(v)): # Recorremos el arreglo desde la segunda posición
        x = v[i]              # Guardamos el valor actual en x
        j = i-1               # Inicializamos j con la posición anterior

        # El siguiente bucle sirve para mover los elementos mayores que x a la derecha
        while j>=0 and v[j]>x: # Cuando j sea superior/igual a 0 y el elemento guardado en la posición j sea mayor que el elemento x
            v[j+1] = v[j]      # Se copia el elemento de la posición j en el siguinte puesto
            j = j-1            # Mientras que la posición j se desplaza a la anterior
        v[j+1] = x             # Insertamos x en la posición correcta de j
    return v                   # Devuelve el v ector ordenado


# Función de ordenación Shell con incrementos de Hibbard (es más eficiente que ins_sort)
def shell_sort_hibbard(v):                  # Se encarga de la ordenación Shell, añadiéndole los incrementos, de vectores dados 

    increments = hibbard_increments(len(v)) # Calculamos los incrementos de Hibbard según la longitud del vector
    return shell_sort_aux(v,increments)     # Devolvemos el resultado, llamando a la función auxiliar con sus correspondientes incrementos


# Función auxiliar con los incrementos de Hibbard
def shell_sort_aux(v:list, increments): # Ordena un vector utilizando el algoritmo Shell Sort con incrementos dados

    for increment in increments:                # Recorre cada dato de la lista de incrementos
        for i in range(increment, len(v)):      # Recorremos el arreglo desde el incremento actual hasta la longitud del vector
            tmp = v[i]                          # Guardamos el valor del incremento actual en tmp
            j = i                               # La variable j guarda la posición del incremento i 
            seguir = True

            # Aplicamos la ordenación por inserción con el incremento actual
            while j-increment > 0 and seguir:   # Mientras el resultado de la resta de la posición de j menos el incremento sea superior a 0 y la variable seguir de permiso para continuar
                if tmp < v[j-increment]:        # Si el valor tmp es menor que el valor de la operación anterior
                    v[j] = v[j-increment]       # El valor de j se sobreescribe con el valor del resultado de j-incremento
                    j -= increment              # A la posición j se le resta el elemento y se guarda en j
                else:                           
                    seguir = False              # La variable seguir no da permiso para continuar
            v[j] = tmp                          # Insertamos tmp en el contenido de la posición j
    return v                                    # Devuelve el vector ordenado

# Función que calcula los incrementos de Hibbard
def hibbard_increments(n): # Calcula los incrementos siendo n == longitud del vector
    
    increments = []                             # Creamos una lista para almacenar los incrementos 
    k = 1                                       
    gap = 2**k - 1                              # Calcula el valor de la variable gap inicial como 2^k - 1

    # Generamos los incrementos de Hibbard
    while gap < n:                               # Inicia un bucle while que se ejecuta mientras gap sea menor que n 
        increments.insert(0, gap)                # Agrega el valor de gap al principio de la lista increments
        k += 1                                   # Suma 1 a k en cada iteración del bucle 
        gap = 2**k - 1                           # Calcula el nuevo valor de gap en función de la nueva k
    return increments                            # Devuelve la lista de los incrementos al rematar el bucle


