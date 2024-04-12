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
            MATRIZ[FILA][COLUMNA] = random.randint(0,1)


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

def convertirMatrizALista(MATRIZ, FILAS, COLUMNAS):
    LISTA = []
    for FILA in range (FILAS):
        for COLUMNA in range(COLUMNAS):
            LISTA.append(MATRIZ[FILA][COLUMNA])
    return LISTA

#SUMA DE MATRICES
def HallarSumaDeZonaSombreada(A):
    #Verificación de cantidad de filas y columnas
    FILAS_A = len(A)
    COLUMNAS_A = len(A[0])

    FILA_FINAL_ANILLO = 0
    COLUMNA_FINAL_ANILLO = 0

    FILAS_ANILLO = int((FILAS_A/2) - 1)
    COLUMNAS_ANILLO = int((COLUMNAS_A/2) - 1)
    SUMA = 0
    for FILA_ANILLO in range (FILAS_ANILLO):
        for COLUMNA_ANILLO in range(COLUMNAS_ANILLO):
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
            SUMATEMP = 0
            for FILA in range(FILAS_A):
                for COLUMNA in range(COLUMNAS_A):
                    if (INICIO_FILA_ANILLO_ARRIBA <= FILA <= FINAL_FILA_ANILLO_ABAJO) and (INICIO_COLUMNA_ANILLO_IZQUIERDA <= COLUMNA <= FINAL_COLUMNA_ANILLO_DERECHA):
                        if FILA > INICIO_FILA_ANILLO_ARRIBA and FILA < FINAL_FILA_ANILLO_ABAJO and COLUMNA > INICIO_COLUMNA_ANILLO_IZQUIERDA and COLUMNA < FINAL_COLUMNA_ANILLO_DERECHA:
                            continue
                        else:
                            SUMATEMP = SUMATEMP + A[FILA][COLUMNA]
                            #A[FILA][COLUMNA] = 'HERE'
            if SUMATEMP > SUMA:
                SUMA = SUMATEMP
                FILA_FINAL_ANILLO = FILA_ANILLO
                COLUMNA_FINAL_ANILLO = COLUMNA_ANILLO

    return SUMA, FILA_FINAL_ANILLO, COLUMNA_FINAL_ANILLO

def imprimirMatrizAnillada(A, FILA_ANILLO, COLUMNA_ANILLO):
    # Verificación de cantidad de filas y columnas
    FILAS_A = len(A)
    COLUMNAS_A = len(A[0])

    # Determinar cuanto debe correr la fila de la matriz para construir el anillo
    # Parte de arriba = FILA_ANILLO
    # Parte de abajo = FILAS_A - FILA_ANILLO
    INICIO_FILA_ANILLO_ARRIBA = FILA_ANILLO
    FINAL_FILA_ANILLO_ABAJO = FILAS_A - FILA_ANILLO - 1
    # Determinar cuanto debe correr la columna de la matriz para construir el anillo
    # Parte de arriba = COLUMNA_ANILLO
    # Parte de abajo = COLUMNAS_A - COLUMNA_ANILLO
    INICIO_COLUMNA_ANILLO_IZQUIERDA = COLUMNA_ANILLO
    FINAL_COLUMNA_ANILLO_DERECHA = COLUMNAS_A - COLUMNA_ANILLO - 1
    for FILA in range(FILAS_A):
        for COLUMNA in range(COLUMNAS_A):
            if (INICIO_FILA_ANILLO_ARRIBA <= FILA <= FINAL_FILA_ANILLO_ABAJO) and (
                    INICIO_COLUMNA_ANILLO_IZQUIERDA <= COLUMNA <= FINAL_COLUMNA_ANILLO_DERECHA):
                if FILA > INICIO_FILA_ANILLO_ARRIBA and FILA < FINAL_FILA_ANILLO_ABAJO and COLUMNA > INICIO_COLUMNA_ANILLO_IZQUIERDA and COLUMNA < FINAL_COLUMNA_ANILLO_DERECHA:
                    continue
                else:
                    A[FILA][COLUMNA] = 'HERE'
    return A


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
SUMA, FILA1, COLUMNA1 = HallarSumaDeZonaSombreada(MATRIZ1)
print("Esta es la suma de la zona sombreada", SUMA)
print("Estos son los valores que se han sumado = ")
MATRIZ1 = imprimirMatrizAnillada(MATRIZ1, FILA1, COLUMNA1)
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
SUMA, FILA2, COLUMNA2 = HallarSumaDeZonaSombreada(MATRIZ2)
print("Esta es la suma de la zona sombreada", SUMA)
print("Estos son los valores que se han sumado = ")
MATRIZ2 = imprimirMatrizAnillada(MATRIZ2, FILA2, COLUMNA2)
imprimirMatrizEspecial(MATRIZ2)

MATRIZ3 = crearMatriz(6, 6)
leerMatriz(MATRIZ3)
print("Esta es la matriz 3:")
imprimirMatrizEspecial(MATRIZ3)
SUMA, FILA3, COLUMNA3 = HallarSumaDeZonaSombreada(MATRIZ3)
print("Esta es la suma de la zona sombreada", SUMA)
print("Estos son los valores que se han sumado = ")
MATRIZ3 = imprimirMatrizAnillada(MATRIZ3, FILA3, COLUMNA3)
imprimirMatrizEspecial(MATRIZ3)


MATRIZ4 = crearMatriz(8, 8)
leerMatriz(MATRIZ4)
print("Esta es la matriz 3:")
imprimirMatrizEspecial(MATRIZ4)
SUMA, FILA4, COLUMNA4 = HallarSumaDeZonaSombreada(MATRIZ4)
print("Esta es la suma de la zona sombreada", SUMA)
print("Estos son los valores que se han sumado = ")
MATRIZ4 = imprimirMatrizAnillada(MATRIZ4, FILA4, COLUMNA4)
imprimirMatrizEspecial(MATRIZ4)