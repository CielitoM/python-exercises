#Teniendo las matrices A[m,n] y B[p,q], almacenar en la lista V todos los elementos no comunes de ambas matrices.
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
            MATRIZ[FILA][COLUMNA] = random.randint(0,10)


def imprimirMatriz(MATRIZ):
    FILAS = len(MATRIZ)
    for FILA in range(FILAS):
        print(MATRIZ[FILA])


#SUMA DE MATRICES
def elementosComunesDeDosMatrices(A,B):
    #Verificación de cantidad de filas y columnas de A y B
    FILAS_A = len(A)
    COLUMNAS_A = len(A[0])
    FILAS_B = len(A)
    COLUMNAS_B = len(A[0])

    V = []

    for FILA_A in range(FILAS_A):
        for COLUMNA_A in range(COLUMNAS_A):
            for FILA_B in range(FILAS_B):
                for COLUMNA_B in range(COLUMNAS_B):
                    if (A[FILA_A ][COLUMNA_A] == B[FILA_B ][COLUMNA_B]):
                        V.append(A[FILA_A][COLUMNA_A])

    V = list(set(V))
    return V


MATRIZ1 = crearMatriz(3, 3)
MATRIZ2 = crearMatriz(3, 3)
leerMatriz(MATRIZ1)
leerMatriz(MATRIZ2)
print("Esta es la matriz 1:")
imprimirMatriz(MATRIZ1)
print("Esta es la matriz 2:")
imprimirMatriz(MATRIZ2)

V = elementosComunesDeDosMatrices(MATRIZ1,MATRIZ2)
print("Resultado = ", V)
