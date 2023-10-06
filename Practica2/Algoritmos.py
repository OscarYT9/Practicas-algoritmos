v=[1,3,-23,-4,2,5,7,556,45]
n=len(v)

#1. Implemente en PYTHON los algoritmos de ordenación por inserción y ordenación Shell con incrementos de Hibbard.

def ins_sort(v):
    for i in range(1,n): #Buscar traducir el pseudocodigo a python, nos dice que el algoritmo empieza en la posicion 2 del algoritmo y en python tiene que ir de la posicion 1 a la n, ya que la primera posición pyhton es el 0
        x = v[i]
        j = i-1
        while j>0 and v[j]>x:
            v[j+1] = v[j]
            j = j-1
        v[j+1] = x
    return v


def shell_sort_aux(v:list, increments): #preguntar
    for increment in increments:
        for i in range(increment+1, n):
            tmp = v[i]
            j = i
            seguir = True
            while j-increment > 0 and seguir:
                if tmp < v[j-increment]:
                    v[j] = v[j-increment]
                    j -= increment
                else:
                    seguir = False
            v[j] = tmp
    return v




#---------------------------
def hibbard_increments(n):
    increments = []
    k = 1
    gap = 2**k - 1
    while gap < n:
        increments.insert(0, gap)
        k += 1
        gap = 2**k - 1
    return increments

def shell_sort_hibbard(v):

    increments = hibbard_increments(len(v))
    return shell_sort_aux(v,increments)


print(ins_sort(v))
print(shell_sort_hibbard(v))#es más eficiente


