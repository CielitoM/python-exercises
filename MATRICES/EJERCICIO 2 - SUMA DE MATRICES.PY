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
def sumarDosMatricesZonaSombreada1(A,B):
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

        #recorrer las filas de arriba y abajo
        for FILA in range(1, FILAS-1):
            for COLUMNA in range(1, COLUMNAS-1):
                    C[FILA][COLUMNA] = A[FILA][COLUMNA] + B[FILA][COLUMNA]
        return C



MATRIZ1 = crearMatriz(5, 5)
MATRIZ2 = crearMatriz(5, 5)
leerMatriz(MATRIZ1)
leerMatriz(MATRIZ2)
print("Esta es la matriz 1:")
imprimirMatrizEspecial(MATRIZ1)
print("Esta es la matriz 2:")
imprimirMatrizEspecial(MATRIZ2)

MATRIZ3 = sumarDosMatricesZonaSombreada1(MATRIZ1, MATRIZ2)
print("Resultado = ")
imprimirMatrizEspecial(MATRIZ3)