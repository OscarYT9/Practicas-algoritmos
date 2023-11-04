
#_____________________________________________________________________________________
# Función para crear un montículo de mínimos a partir de un vector.
def crearMonticulo(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

# Función para consultar el menor elemento del montículo.
def consultarMenor(arr):
    return arr[0]

# Función para quitar el menor elemento del montículo.
def quitarMenor(arr):
    n = len(arr)
    if n == 0:
        return
    arr[0] = arr[n - 1]
    arr.pop()
    heapify(arr, n - 1, 0)

# Función para mantener la propiedad de montículo en el índice dado.
def heapify(arr, n, i):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] < arr[smallest]:
        smallest = left
    if right < n and arr[right] < arr[smallest]:
        smallest = right

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify(arr, n, smallest)

# Función para ordenar un arreglo usando montículos.
def ordenacionPorMonticulos(arr):
    n = len(arr)

    # Crear un montículo a partir del arreglo dado.
    crearMonticulo(arr)

    # Extraer elementos uno por uno del montículo para ordenarlos.
    for i in range(n - 1, -1, -1):
        arr[i] = consultarMenor(arr)
        quitarMenor(arr)

# Función para validar que el montículo esté ordenado.
def validarMonticuloOrdenado(arr):
    n = len(arr)
    for i in range(1, n):
        if arr[i] < arr[(i - 1) // 2]:
            return False
    return True

# Ejemplo de uso
arr = [12, 11, 13, 5, 6, 7]
print("Arreglo original:", arr)

# Crear un montículo a partir del arreglo
crearMonticulo(arr)
print("Montículo creado:", arr)

# Consultar el menor elemento del montículo
menor = consultarMenor(arr)
print("Menor elemento del montículo:", menor)

# Quitar el menor elemento del montículo
quitarMenor(arr)
print("Montículo después de quitar el menor elemento:", arr)

# Ordenar el arreglo usando montículos
ordenacionPorMonticulos(arr)
print("Arreglo ordenado:", arr)

# Validar que el arreglo esté ordenado
print("¿El arreglo está ordenado?", validarMonticuloOrdenado(arr))


#__________________________________________________________________________________________________________________________________
