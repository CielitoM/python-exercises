#HALLAR LA SUMA DE DOS MATRICES A Y B

A = [[2,4],[3,5]]
B = [[8,6],[1,2]]

def CrearMatriz:
    pass

def sumarDosMatrices(A,B, FILAS, COLUMNAS):
    C = [[]]
    for FILA in range(FILAS):
        for COLUMNA in range(COLUMNAS):
            C[FILA][COLUMNA] = A[FILA][COLUMNA] + B[FILA][COLUMNA]

    return C


print(sumarDosMatrices(A,B,2,2))



