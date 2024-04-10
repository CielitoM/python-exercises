#Una matriz representa la imagen de una zona del mar donde se encuentra una isla.
# Cada celda representa un cuadro de 100 por 100 metros de superficie y la isla no
# toca los bordes de la imagen. Los cuadros con valor 1 representan tierra de la isla y
# los cuadros con valor cero representan el mar. Escribir un programa que calcule el perímetro y
# el área de la isla.
#import random


def crearMatriz(M, N):
    MATRIZ = []
    for I in range(M):
        MATRIZ.append([0] * N)
    return (MATRIZ)

"""
def leerMatriz(MATRIZ):
    FILAS = len(MATRIZ)
    COLUMNAS = len(MATRIZ[0])
    for FILA in range(FILAS):
        for COLUMNA in range(COLUMNAS):
            MATRIZ[FILA][COLUMNA] = random.randint(1,100)
"""

def imprimirMatriz(MATRIZ):
    FILAS = len(MATRIZ)
    for FILA in range(FILAS):
        print(MATRIZ[FILA])

def determinarIslasAdyacentes(LISTAPERIMETRAL):
    contador = 0
    for ELEMENTO in range(len(LISTAPERIMETRAL)):
        if LISTAPERIMETRAL[ELEMENTO] == 1:
            contador = contador + 1
    if contador == 4:
        return 0
    elif contador == 3:
        return 100
    elif contador == 2:
        return 200
    elif contador == 1:
        return 300
    elif contador == 0:
        return 0

#HALLAR PERIMETRO DE LA ISLA
def hallarPerimetroDeLaIsla(A):
    FILAS = len(A)
    COLUMNAS = len(A[0])
    perimetro = 0
    LISTAPERIMETRAL = []
    for FILA in range(FILAS):
        for COLUMNA in range(COLUMNAS):
            if A[FILA][COLUMNA] == 1:
                if FILA-1 > -1 and FILA+1 < FILAS and COLUMNA-1 > -1 and COLUMNA+1 < COLUMNAS:
                    LISTAPERIMETRAL.append(A[FILA-1][COLUMNA])
                    LISTAPERIMETRAL.append(A[FILA+1][COLUMNA])
                    LISTAPERIMETRAL.append(A[FILA][COLUMNA-1])
                    LISTAPERIMETRAL.append(A[FILA][COLUMNA+1])
                    resultadoPerimetroPorCelda = determinarIslasAdyacentes(LISTAPERIMETRAL)
                    perimetro = perimetro + resultadoPerimetroPorCelda
                    LISTAPERIMETRAL = []
                else:
                    if FILA - 1 > -1:
                        perimetro = perimetro + 100
                    elif FILA+1 < FILAS:
                        perimetro = perimetro + 100
                    elif COLUMNA-1 > -1:
                        perimetro = perimetro + 100
                    elif COLUMNA+1 < COLUMNAS:
                        perimetro = perimetro + 100
    return perimetro


#HALLAR EL ÁREA DE LA ISLA
def hallarAreaDeLaIsla(A):
    FILAS = len(A)
    COLUMNAS = len(A[0])
    for FILA in range(FILAS):
        for COLUMNA in range(COLUMNAS):
            pass
    pass


"""
MATRIZ1 = crearMatriz(7, 7)
leerMatriz(MATRIZ1)
"""
print("Esta es la matriz 1:")
MATRIZ1 = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [0, 0, 1, 1, 1, 1, 0],
    [0, 0, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 1, 0, 0]
]

imprimirMatriz(MATRIZ1)

perimetro = hallarPerimetroDeLaIsla(MATRIZ1)
print("El perimetro de la matriz es = ", perimetro)


