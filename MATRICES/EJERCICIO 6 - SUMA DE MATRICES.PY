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
def sumarDosMatricesZonaSombreada6(A,B):
    #Verificación de cantidad de filas y columnas de A y B
    FILAS_A = len(A)
    COLUMNAS_A = len(A[0])
    FILAS_B = len(A)
    COLUMNAS_B = len(A[0])
    if FILAS_A != COLUMNAS_A or FILAS_B != COLUMNAS_B:
        print("Sólo se puede realizar esta operación con matrices cuadradas")
        return 0
    else:
        FILAS = FILAS_A
        COLUMNAS = COLUMNAS_A
        C = crearMatriz(FILAS, COLUMNAS)
        COLUMNAFINAL = int(COLUMNAS/2)
        contadorFilasInicial = 0
        contadorFilasFinal = FILAS
        for COLUMNA in range(COLUMNAS - 1, COLUMNAFINAL, -1):
            contadorFilasInicial = contadorFilasInicial + 1
            contadorFilasFinal = contadorFilasFinal - 1
            for FILA in range(contadorFilasInicial, contadorFilasFinal):
                C[FILA][COLUMNA] = A[FILA][COLUMNA] + B[FILA][COLUMNA]
        return C



MATRIZ1 = crearMatriz(6, 6)
MATRIZ2 = crearMatriz(6, 6)
leerMatriz(MATRIZ1)
leerMatriz(MATRIZ2)
print("Esta es la matriz 1:")
imprimirMatriz(MATRIZ1)
print("Esta es la matriz 2:")
imprimirMatriz(MATRIZ2)

MATRIZ3 = sumarDosMatricesZonaSombreada6(MATRIZ1, MATRIZ2)
print("Resultado = ")
imprimirMatriz(MATRIZ3)