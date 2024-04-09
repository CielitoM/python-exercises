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
        contadorColumnaRangoInicial = 1
        salto = 2
        contadorParoImpar = 0
        for FILA in range(0, FILAS):
            for COLUMNA in range(contadorColumnaRangoInicial, COLUMNAS, salto):
                C[FILA][COLUMNA] = A[FILA][COLUMNA] + B[FILA][COLUMNA]
            if (contadorParoImpar == 0):
                contadorColumnaRangoInicial = 0
                salto = 1
                contadorParoImpar = 1
            else:
                contadorColumnaRangoInicial = 1
                salto = 2
                contadorParoImpar = 0
        return C


MATRIZ1 = crearMatriz(7, 7)
MATRIZ2 = crearMatriz(7, 7)
leerMatriz(MATRIZ1)
leerMatriz(MATRIZ2)
print("Esta es la matriz 1:")
imprimirMatriz(MATRIZ1)
print("Esta es la matriz 2:")
imprimirMatriz(MATRIZ2)

MATRIZ3 = sumarDosMatricesZonaSombreada6(MATRIZ1, MATRIZ2)
print("Resultado = ")
imprimirMatriz(MATRIZ3)