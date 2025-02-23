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

def eliminarFila(MATRIZ, FILAX):
    banderafilas = 0

    FILAS = len(MATRIZ)
    COLUMNAS = len(MATRIZ[0])

    MATRIZ2 = crearMatriz(FILAS - 1, COLUMNAS)
    FILA = 0

    while FILA < FILAS:
        for COLUMNA in range(COLUMNAS):
            if (FILA == FILAX or banderafilas == 1) and FILA < FILAS - 1 and FILA != FILAS-1:
                MATRIZ2[FILA][COLUMNA] = MATRIZ[FILA + 1][COLUMNA]
                banderafilas = 1
            elif FILA < FILAS-1 and banderafilas == 0:
                MATRIZ2[FILA][COLUMNA] = MATRIZ[FILA][COLUMNA]
                banderafilas = 0
        FILA = FILA+1


    return MATRIZ2

def eliminarColumna(MATRIZ, COLUMNAX):
    banderacolumna = 0

    FILAS = len(MATRIZ)
    COLUMNAS = len(MATRIZ[0])

    MATRIZ2 = crearMatriz(FILAS, COLUMNAS-1)
    COLUMNA = 0

    while COLUMNA < COLUMNAS:
        for FILA in range(FILAS):
            if (COLUMNA == COLUMNAX or banderacolumna == 1) and COLUMNA < COLUMNAS - 1 and COLUMNA != COLUMNAS-1:
                MATRIZ2[FILA][COLUMNA] = MATRIZ[FILA][COLUMNA + 1]
                banderacolumna = 1
            elif COLUMNA < COLUMNAS-1 and banderacolumna == 0:
                MATRIZ2[FILA][COLUMNA] = MATRIZ[FILA][COLUMNA]
                banderacolumna= 0
        COLUMNA = COLUMNA+1
    return (MATRIZ2)


MATRIZ1 = crearMatriz(7, 7)
leerMatriz(MATRIZ1)
"""
MATRIZ1 = ([
    [10, 3, 1, 5, 9, 3, 5],
    [4, 3, 7, 8, 4, 4, 5],
    [8, 2, 9, 9, 9, 4, 3],
    [10, 7, 3, 8, 3, 10, 5],
    [4, 2, 9, 5, 2, 6, 5],
    [7, 5, 5, 10, 2, 1, 6],
    [3, 8, 4, 6, 2, 4, 9]
])
"""
print("Esta es la matriz 1:")
imprimirMatriz(MATRIZ1)
FILA =  random.randint(0,6)
print("Se va a eliminar la fila:", FILA)
COLUMNA = random.randint(0,6)
print("Se va a eliminar la columna:", COLUMNA)

print("Esta es la matriz:")
MATRIZ2 = eliminarFila(MATRIZ1, FILA)
MATRIZ2 = eliminarColumna(MATRIZ2, COLUMNA)
imprimirMatriz(MATRIZ2)
