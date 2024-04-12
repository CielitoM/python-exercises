#Calcular la suma de la zona indicada en la figura, siendo datos m, n, p, q y los elementos de la matriz:
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

def imprimirMatrizEspecial(MATRIZ):
    FILAS = len(MATRIZ)

    for FILA in range(FILAS):
        fila_formateada = ''
        for columna in MATRIZ[FILA]:
            fila_formateada += str(columna).rjust(6)  # Alinea cada elemento a la derecha con un ancho de 6 caracteres
        print(fila_formateada)

#SUMA DE MATRICES
def HallarSumaDeZonaSombreada(A, FILA_ANILLO, COLUMNA_ANILLO):
    #Verificación de cantidad de filas y columnas
    FILAS_A = len(A)
    COLUMNAS_A = len(A[0])

    #Determinar cuanto debe correr la fila de la matriz para construir el anillo
        # Parte de arriba = FILA_ANILLO
        # Parte de abajo = FILAS_A - FILA_ANILLO
    INICIO_FILA_ANILLO_ARRIBA = FILA_ANILLO
    FINAL_FILA_ANILLO_ABAJO = FILAS_A - FILA_ANILLO -1
    #Determinar cuanto debe correr la columna de la matriz para construir el anillo
        # Parte de arriba = COLUMNA_ANILLO
        # Parte de abajo = COLUMNAS_A - COLUMNA_ANILLO
    INICIO_COLUMNA_ANILLO_IZQUIERDA = COLUMNA_ANILLO
    FINAL_COLUMNA_ANILLO_DERECHA = COLUMNAS_A - COLUMNA_ANILLO -1

    #Recorrer matriz
    SUMA = 0
    for FILA in range(FILAS_A):
        for COLUMNA in range(COLUMNAS_A):
            if (INICIO_FILA_ANILLO_ARRIBA <= FILA <= FINAL_FILA_ANILLO_ABAJO) and (INICIO_COLUMNA_ANILLO_IZQUIERDA <= COLUMNA <= FINAL_COLUMNA_ANILLO_DERECHA):
                if FILA > INICIO_FILA_ANILLO_ARRIBA and FILA < FINAL_FILA_ANILLO_ABAJO and COLUMNA > INICIO_COLUMNA_ANILLO_IZQUIERDA and COLUMNA < FINAL_COLUMNA_ANILLO_DERECHA:
                    continue
                else:
                    SUMA = SUMA + A[FILA][COLUMNA]
                    A[FILA][COLUMNA] = 'HERE'

    return SUMA, A





MATRIZ1 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]
print("Esta es la matriz 1:")
imprimirMatrizEspecial(MATRIZ1)
SUMA, MATRIZ1 = HallarSumaDeZonaSombreada(MATRIZ1, 2, 2)
print("Esta es la suma de la zona sombreada", SUMA)
print("Estos son los valores que se han sumado = ")
imprimirMatrizEspecial(MATRIZ1)



MATRIZ2 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1]
]

print("Esta es la matriz 2:")
imprimirMatrizEspecial(MATRIZ2)
SUMA, MATRIZ2 = HallarSumaDeZonaSombreada(MATRIZ2, 0, 0)
print("Esta es la suma de la zona sombreada", SUMA)
print("Estos son los valores que se han sumado = ")
imprimirMatrizEspecial(MATRIZ2)

MATRIZ3 = crearMatriz(10, 10)
leerMatriz(MATRIZ3)
print("Esta es la matriz 3:")
imprimirMatrizEspecial(MATRIZ3)
FILA = random.randint(0, int(10/2)-1)
COLUMNA = random.randint(0, int(10/2)-1)
print("La fila del anillo es = ",FILA, "y la columna es = ", COLUMNA)
SUMA, MATRIZ3 = HallarSumaDeZonaSombreada(MATRIZ3, FILA, COLUMNA)
print("Esta es la suma de la zona sombreada", SUMA)
print("Estos son los valores que se han sumado = ")
imprimirMatrizEspecial(MATRIZ3)