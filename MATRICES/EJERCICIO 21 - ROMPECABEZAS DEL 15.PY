import random


def crearMatriz(M, N):
    MATRIZ = []
    for I in range(M):
        MATRIZ.append([0] * N)
    return (MATRIZ)


def leerMatriz(MATRIZ):
    FILAS = len(MATRIZ)
    COLUMNAS = len(MATRIZ[0])
    RANGO = range(1,16)
    LISTA_ALEATORIA = random.sample(RANGO,15)
    ELEMENTO = 0
    for FILA in range(FILAS):
        for COLUMNA in range(COLUMNAS):
            if FILA == 3 and COLUMNA == 3:
                MATRIZ[FILA][COLUMNA] = 0
            else:
                MATRIZ[FILA][COLUMNA] = LISTA_ALEATORIA[ELEMENTO]
                ELEMENTO = ELEMENTO + 1


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



MATRIZ = crearMatriz(4, 4)
leerMatriz(MATRIZ)
print("Esta es la matriz inicial:")
imprimirMatrizEspecial(MATRIZ)
FINALIZADO = False
print("Juega con ASDW")
while not FINALIZADO:
    MOVIMIENTO = input("Ingrese su movimiento: ")

    #REALIZACION DEL MOVIMIENTO
    if (MOVIMIENTO == 'W' or MOVIMIENTO == 'w'):
    #print("Su movimiento ha sido : ", MOVIMIENTO)
        MATRIZ = realizarMovimientoArriba(MATRIZ, MOVIMIENTO)
    elif (MOVIMIENTO == 'S' or MOVIMIENTO == 's'):
        MATRIZ = realizarMovimientoAbajo(MATRIZ, MOVIMIENTO)

    elif (MOVIMIENTO == 'D' or MOVIMIENTO == 'd'):

    elif (MOVIMIENTO == 'A' or MOVIMIENTO == 'a'):


    FINALIZADO = True
