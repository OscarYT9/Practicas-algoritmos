import sys

def dijkstra(M):
    n = len(M)  # Obtener el tamaño de la matriz, asumiendo que es cuadrada

    # Inicializar matriz de distancias con valores infinitos
    Distancias = [[sys.maxsize] * n for _ in range(n)] #sys.maxsize se guarda como infinito

    for m in range(n):
        noVisitados = set(range(n))  # Conjunto de nodos no visitados
        noVisitados.remove(m)  # Remover el nodo actual de noVisitados

        # Inicializar la distancia desde el nodo m a todos los demás nodos
        for i in range(n):
            Distancias[m][i] = M[m][i]

        # Repetir n-2 veces para encontrar las distancias más cortas
        for _ in range(n - 2):
            # Encontrar el nodo en noVisitados con la distancia mínima
            v = min(noVisitados, key=lambda x: Distancias[m][x])

            # Remover el nodo v de noVisitados
            noVisitados.remove(v)

            # Actualizar las distancias hacia los nodos no visitados a través de v
            for w in noVisitados:
                if Distancias[m][w] > Distancias[m][v] + M[v][w]:
                    Distancias[m][w] = Distancias[m][v] + M[v][w]

    return Distancias





# Ejemplo de matriz de adyacencia
# M = [
#     [0, 1, 8, 4, 7],
#     [1, 0, 2, 6, 5],
#     [8, 2, 0, 9, 5],
#     [4, 6, 9, 0, 3],
#     [7, 5, 5, 3, 0]
# ]

# matriz_distancias_minimas(M)
