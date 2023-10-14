#Algoritmos a comprobar
#1. Implemente en PYTHON los algoritmos de ordenación por inserción y ordenación Shell con incrementos de Hibbard.

def ins_sort(v):

    for i in range(1,len(v)): # Recorremos el arreglo desde la segunda posición
        x = v[i]              # Guardamos el valor actual en x
        j = i-1               # Inicializamos j con la posición anterior

        # Movemos los elementos mayores que x a la derecha
        while j>=0 and v[j]>x:
            v[j+1] = v[j]
            j = j-1
        v[j+1] = x # Insertamos x en la posición correcta
    return v


# Función de ordenación Shell con incrementos de Hibbard (es más eficiente que ins_sort)
def shell_sort_hibbard(v):

    increments = hibbard_increments(len(v)) # Calculamos los incrementos de Hibbard
    return shell_sort_aux(v,increments)     # Llamamos a la función auxiliar con los incremento


# Función auxiliar con los incrementos de Hibbard
def shell_sort_aux(v:list, increments): #PREGUNTAR

    for increment in increments:
        for i in range(increment, len(v)): # Recorremos el arreglo desde el incremento actual #n=len(v)
            tmp = v[i]                     # Guardamos el valor actual en tmp
            j = i
            seguir = True

            # Aplicamos la ordenación por inserción con el incremento actual
            while j-increment > 0 and seguir:
                if tmp < v[j-increment]:
                    v[j] = v[j-increment]
                    j -= increment
                else:
                    seguir = False
            v[j] = tmp                      # Insertamos tmp en la posición correcta
    return v

# Función que calcula los incrementos de Hibbard
def hibbard_increments(n):
    
    increments = []
    k = 1
    gap = 2**k - 1

    # Generamos los incrementos de Hibbard
    while gap < n:
        increments.insert(0, gap)
        k += 1
        gap = 2**k - 1
    return increments


