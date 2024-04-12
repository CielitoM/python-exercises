# Dada una matriz A[M,N] y la posición [FILA, COLUMNA] de un elemento de la misma, obtener la matriz
# B que resulta al eliminar la fila y la columna de ese elemento.
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
            MATRIZ[FILA][COLUMNA] = random.randint(1,10)


def imprimirMatriz(MATRIZ):
    FILAS = len(MATRIZ)
    for FILA in range(FILAS):
        print(MATRIZ[FILA])


def eliminarFilas(MATRIZ, ELIMINARFILA):
    FILAS = len(MATRIZ)
    COLUMNAS = len(MATRIZ[0])
    bandera = 0
    for FILA in range(FILAS):
        for COLUMNA in range(COLUMNAS):
            if (FILA == ELIMINARFILA or bandera == 1) and FILA < FILAS-1:
                bandera = 1
                MATRIZ[FILA][COLUMNA] = MATRIZ[FILA+1][COLUMNA]
            elif bandera == 0:
                MATRIZ[FILA][COLUMNA] = MATRIZ[FILA][COLUMNA]

def eliminarColumnas(MATRIZ, ELIMINARCOLUMNA):
    FILAS = len(MATRIZ)
    COLUMNAS = len(MATRIZ[0])
    bandera = 0
    for FILA in range(FILAS):
        for COLUMNA in range(COLUMNAS):
            if (COLUMNA == ELIMINARCOLUMNA or bandera == 1) and COLUMNA < COLUMNAS-1:
                bandera = 1
                MATRIZ[FILA][COLUMNA] = MATRIZ[FILA][COLUMNA+1]
            elif bandera == 0:
                MATRIZ[FILA][COLUMNA] = MATRIZ[FILA][COLUMNA]

def reconstruirMatriz(MATRIZ):
    FILAS = len(MATRIZ)
    COLUMNAS = len(MATRIZ[0])
    MATRIZ2 = crearMatriz(FILAS-1, COLUMNAS-1)

    for FILA in range(FILAS-1):
        for COLUMNA in range(COLUMNAS-1):
            if MATRIZ[FILA][COLUMNA] != 0:
                MATRIZ2[FILA][COLUMNA] = MATRIZ[FILA][COLUMNA]
    imprimirMatriz(MATRIZ2)


MATRIZ1 = crearMatriz(7, 7)
leerMatriz(MATRIZ1)
print("Esta es la matriz 1:")
imprimirMatriz(MATRIZ1)
FILA = random.randint(0,6)
print("Se va a eliminar la fila:", FILA)
COLUMNA = random.randint(0,6)
print("Se va a eliminar la columna:", COLUMNA)
eliminarFilas(MATRIZ1, FILA)
eliminarColumnas(MATRIZ1, COLUMNA)
print("Esta es la matriz:")
reconstruirMatriz(MATRIZ1)

