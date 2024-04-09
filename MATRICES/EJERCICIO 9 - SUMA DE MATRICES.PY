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
def sumarDiagonalesDeDosMatrices(A,B, diagonal):
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

        if diagonal == 0:
            for FILA in range(FILAS):
                for COLUMNA in range(COLUMNAS):
                    if FILA == COLUMNA:
                        C[FILA][COLUMNA] = A[FILA][COLUMNA] + B[FILA][COLUMNA]
        else:
            contadorColumna = COLUMNAS
            for FILA in range(FILAS):
                    contadorColumna = contadorColumna - 1
                    C[FILA][contadorColumna] = A[FILA][contadorColumna] + B[FILA][contadorColumna]
        return C


MATRIZ1 = crearMatriz(7, 7)
MATRIZ2 = crearMatriz(7, 7)
leerMatriz(MATRIZ1)
leerMatriz(MATRIZ2)
print("Esta es la matriz 1:")
imprimirMatriz(MATRIZ1)
print("Esta es la matriz 2:")
imprimirMatriz(MATRIZ2)

MATRIZ3 = sumarDiagonalesDeDosMatrices(MATRIZ1, MATRIZ2, 0)
print("Resultado (Diagonal Principal) = ")
imprimirMatriz(MATRIZ3)

MATRIZ3 = sumarDiagonalesDeDosMatrices(MATRIZ1, MATRIZ2, 1)
print("Resultado (Diagonal Secundaria) = ")
imprimirMatriz(MATRIZ3)