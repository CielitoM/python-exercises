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


def imprimirMatrizEspecial(MATRIZ):
    FILAS = len(MATRIZ)

    for FILA in range(FILAS):
        fila_formateada = ''
        for columna in MATRIZ[FILA]:
            fila_formateada += str(columna).rjust(6)  # Alinea cada elemento a la derecha con un ancho de 6 caracteres
        print(fila_formateada)


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
        contadorFilasInicial = 0
        for COLUMNA in range(COLUMNAS-1, -1, -1):
            for FILA in range(contadorFilasInicial, FILAS):
                C[FILA][COLUMNA] = A[FILA][COLUMNA] + B[FILA][COLUMNA]
            contadorFilasInicial = contadorFilasInicial + 1
        return C



MATRIZ1 = crearMatriz(7, 7)
MATRIZ2 = crearMatriz(7, 7)
leerMatriz(MATRIZ1)
leerMatriz(MATRIZ2)
print("Esta es la matriz 1:")
imprimirMatrizEspecial(MATRIZ1)
print("Esta es la matriz 2:")
imprimirMatrizEspecial(MATRIZ2)

MATRIZ3 = sumarDosMatricesZonaSombreada6(MATRIZ1, MATRIZ2)
print("Resultado: ")
imprimirMatrizEspecial(MATRIZ3)