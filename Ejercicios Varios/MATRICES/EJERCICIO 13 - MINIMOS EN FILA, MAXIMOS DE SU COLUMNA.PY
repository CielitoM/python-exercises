#MATRICES
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


def encontrarElementosMinimosFilas(MATRIZ):
    FILAS = len(MATRIZ)
    COLUMNAS = len(MATRIZ[0])
    MINIMOS = []
    for FILA in range(FILAS):
        MINIMO = MATRIZ[FILA][0]
        for COLUMNA in range(COLUMNAS):
            if MATRIZ[FILA][COLUMNA] < MINIMO:
                MINIMO = MATRIZ[FILA][COLUMNA]
        MINIMOS.append(MINIMO)
    return MINIMOS

def encontrarElementosMaximosColumnas(MATRIZ):
    FILAS = len(MATRIZ)
    COLUMNAS = len(MATRIZ[0])
    MAXIMOS = []
    for COLUMNA in range(COLUMNAS):
        MAXIMO = MATRIZ[0][COLUMNA]
        for FILA in range(FILAS):
            if MATRIZ[FILA][COLUMNA] > MAXIMO:
                MAXIMO = MATRIZ[FILA][COLUMNA]
        MAXIMOS.append(MAXIMO)
    return MAXIMOS


MATRIZ1 = crearMatriz(7, 7)
leerMatriz(MATRIZ1)
print("Esta es la matriz 1:")
imprimirMatriz(MATRIZ1)

MINIMOS = encontrarElementosMinimosFilas(MATRIZ1)
print("Los minimos por fila son = ")
print(MINIMOS)
MAXIMOS = encontrarElementosMaximosColumnas(MATRIZ1)
print("Los máximos por columna = ")
print(MAXIMOS)
