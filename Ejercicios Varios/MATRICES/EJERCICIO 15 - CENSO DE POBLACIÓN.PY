# Los datos del censo de población se almacenan en una matriz CENSO [ m , n ], donde cada
# elemento representa la población de una manzana [m y n son pares]. Se pide formar una nueva
# matriz RESUMEN donde cada elemento represente la población de un cuadro de 2 * 2 manzanas de la
# matriz CENSO.
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


def hacerResumen(MATRIZ, FILAS, COLUMNAS):

    #Inicializar lista SUMA donde se almacenaran la suma de la población por c/matriz 2*2
    SUMA = []
    #hallar la cantidad de elementos en resumen
    FILAS_RESUMEN = int(FILAS/2)
    COLUMNAS_RESUMEN = int(COLUMNAS/2)
    RESUMEN = crearMatriz(FILAS_RESUMEN, COLUMNAS_RESUMEN)

    for FILA in range(0, FILAS, 2):
        for COLUMNA in range(0, COLUMNAS, 2):
                        # Arriba izquierda      Arriba derecha            Abajo izquierda            Abajo derecha
            SUMA.append(MATRIZ[FILA][COLUMNA] + MATRIZ[FILA][COLUMNA+1] + MATRIZ[FILA+1][COLUMNA] + MATRIZ[FILA+1][COLUMNA+1])

    ELEMENTO = 0
    for FILA in range(FILAS_RESUMEN):
        for COLUMNA in range(COLUMNAS_RESUMEN):
            RESUMEN[FILA][COLUMNA] = SUMA[ELEMENTO]
            ELEMENTO = ELEMENTO + 1

    return RESUMEN



FILA = 10
COLUMNA = 2
CENSO = crearMatriz(FILA, COLUMNA)
leerMatriz(CENSO)

print("Esta es la matriz 1:")
imprimirMatriz(CENSO)

RESUMEN = hacerResumen(CENSO, FILA, COLUMNA)


print("Esta es la matriz resumen:")
imprimirMatriz(RESUMEN)

