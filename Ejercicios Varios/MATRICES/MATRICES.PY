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


#SUMA DE MATRICES
def sumarDosMatrices(A,B):
    #Verificación de cantidad de filas y columnas de A y B
    FILAS_A = len(A)
    COLUMNAS_A = len(A[0])
    FILAS_B = len(A)
    COLUMNAS_B = len(A[0])
    if FILAS_A != COLUMNAS_A or FILAS_B != COLUMNAS_B:
        print("Sólo se puede realizar esta operacioón con matrices cuadradas")
        return 0
    else:
        FILAS = FILAS_A
        COLUMNAS = COLUMNAS_A
        C = crearMatriz(FILAS, COLUMNAS)
        for FILA in range(FILAS):
            for COLUMNA in range(COLUMNAS):
                C[FILA][COLUMNA] = A[FILA][COLUMNA] + B[FILA][COLUMNA]
        return C

#MULTIPLICACION POR UN NUMERO
def multiplicacionMatrizPorUnEscalar(MATRIZ, escalar):
    FILAS = len(MATRIZ)
    COLUMNAS = len(MATRIZ[0])

    for FILA in range(FILAS):
        for COLUMNA in range(COLUMNAS):
            MATRIZ[FILA][COLUMNA] = MATRIZ[FILA][COLUMNA] * escalar


#MULTIPLICACION ENTRE DOS MATRICES
def multiplicacionEntreDosMatrices(MATRIZ_A, MATRIZ_B):
    FILAS_A = len(MATRIZ_A)
    COLUMNAS_A = len(MATRIZ_A[0])

    FILAS_B = len(MATRIZ_B)
    COLUMNAS_B = len(MATRIZ_B[0])

    #CREAR MATRIZ CANTIDAD DE FILAS de A Y CANTIDAD DE COLUMNAS de B
    MATRIZ_C = crearMatriz(FILAS_A, COLUMNAS_B)

    for FILA_A in range(FILAS_A):
        for COLUMNA_B in range(COLUMNAS_B):
            SUMA = 0
            for COLUMNA in range (COLUMNAS_A):
                SUMA = SUMA + MATRIZ_A[FILA_A][COLUMNA] * MATRIZ_B[COLUMNA][COLUMNA_B]
            MATRIZ_C[FILA_A][COLUMNA_B] = SUMA

    return (MATRIZ_C)

MATRIZ1 = crearMatriz(4, 4)
MATRIZ2 = crearMatriz(4, 4)
leerMatriz(MATRIZ1)
leerMatriz(MATRIZ2)
print("Esta es la matriz 1:")
imprimirMatriz(MATRIZ1)
print("Esta es la matriz 2:")
imprimirMatriz(MATRIZ2)

print("Esta es la matriz suma de la matriz1 y matriz2:")
SUMA = sumarDosMatrices(MATRIZ1, MATRIZ2)
imprimirMatriz(SUMA)

print("Esta es la matriz 1 multiplicada por un escalar, 2:")
multiplicacionMatrizPorUnEscalar(MATRIZ1, 2)
imprimirMatriz(MATRIZ1)

print("Esta es la matriz 1 multiplicada por la matriz 2:")
MATRIZ3 = multiplicacionEntreDosMatrices(MATRIZ1, MATRIZ2)
imprimirMatriz(MATRIZ3)