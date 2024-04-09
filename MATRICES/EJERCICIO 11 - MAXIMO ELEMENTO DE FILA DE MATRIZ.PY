#Encontrar el máximo elemento de cada fila de una matriz T[m, n]
import random


def crearMatriz(M, N):
    MATRIZ = []
    for I in range(M):
        MATRIZ.append([0] * N)
    return (MATRIZ)


def leerMatriz(MATRIZ):
    FILAS = len(MATRIZ)
    COLUMNAS = len(MATRIZ[0])
    for FILA in range(FILAS):
        for COLUMNA in range(COLUMNAS):
            MATRIZ[FILA][COLUMNA] = random.randint(1,100)


def imprimirMatriz(MATRIZ):
    FILAS = len(MATRIZ)
    for FILA in range(FILAS):
        print(MATRIZ[FILA])

#SUMA DE MATRICES
def hallarMaximoElementoDeCadaFila(A):
    FILAS = len(A)
    COLUMNAS = len(A[0])
    MAXIMOS = []
    MAXIMOTEMP = 0
    for FILA in range(FILAS):
        for COLUMNA in range(COLUMNAS):
            if A[FILA][COLUMNA] > MAXIMOTEMP:
                MAXIMOTEMP = A[FILA][COLUMNA]

        MAXIMOS.append(MAXIMOTEMP)
        MAXIMOTEMP = 0
    return MAXIMOS


MATRIZ1 = crearMatriz(7, 7)
leerMatriz(MATRIZ1)
print("Esta es la matriz 1:")
imprimirMatriz(MATRIZ1)

MAXIMOS = hallarMaximoElementoDeCadaFila(MATRIZ1)
print("Los máximos de cada fila de la matriz es = ", MAXIMOS)


