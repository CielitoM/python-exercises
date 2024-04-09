#Escribir un programa para determinar cual es el cuadro de 2 x 2 elementos que posee la mayor
# suma en una matriz dada.
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

#SUMAR LOS ELEMENTOS DE LA MATRIZ 2X2
def sumarElementosDeMatrizDosPorDos(MATRIZ):
    SUMA = 0
    FILAS = 2
    COLUMNAS = 2
    for FILA in range(FILAS):
        for COLUMNA in range(COLUMNAS):
            SUMA = SUMA + MATRIZ[FILA][COLUMNA]
    return SUMA


#SUMA DE MATRICES
def hallarMayorSumaDosporDos(A):
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
        C = crearMatriz(2, 2)
        SUMA = 0
        MATRIZ = crearMatriz(2,2)
        for FILA in range(FILAS):
            for COLUMNA in range(COLUMNAS):
                if FILA+1 < FILAS and COLUMNA+1 < COLUMNAS:
                    C = [[A[FILA][COLUMNA], A[FILA][COLUMNA+1]], [A[FILA+1][COLUMNA], A[FILA+1][COLUMNA+1]]]
                    SUMATEMPORAL = sumarElementosDeMatrizDosPorDos(C)
                    if SUMATEMPORAL > SUMA:
                        SUMA = SUMATEMPORAL
                        MATRIZ = C
        return MATRIZ, SUMA


MATRIZ1 = crearMatriz(7, 7)
leerMatriz(MATRIZ1)
print("Esta es la matriz 1:")
imprimirMatriz(MATRIZ1)

MATRIZ3, SUMA = hallarMayorSumaDosporDos(MATRIZ1)
print("Resultado de la suma es = ", SUMA)
imprimirMatriz(MATRIZ3)

