#Ordenar la matriz A[m,n], conforme a la regla mostrada en el ejemplo siguiente:
#
#   24 11  71                   3   24  48
#   48 46  3                    9   37  71
#   9  75  37                   11  46  75
#   Matriz original            Matriz Ordenada

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

def mergeSort(lista):
    if len(lista) > 1:
        medio = len(lista) // 2
        izquierda = lista[:medio]
        derecha = lista[medio:]

        # Llamada recursiva para cada mitad
        mergeSort(izquierda)
        mergeSort(derecha)

        # Dos índices para recorrer las dos mitades
        I = 0
        J = 0

        # Índice para la lista principal
        K = 0

        while I < len( izquierda ) and J < len( derecha ):
            if izquierda[ I ] < derecha[ J ]:
                # Se utiliza el valor tomado de la mitad izquierda
                lista[ K ] = izquierda[ I ]
                # Aumenta el índice de la mitad izquierda
                I += 1
            else:
                # Se utiliza el valor tomado de la mitad derecha
                lista[ K ] = derecha[ J ]
                # Aumenta el índice de la mitad derecha
                J += 1
            # Aumenta el índice en la lista principal
            K += 1

        # Para todos los valores restantes
        while I < len( izquierda ):
            lista[ K ] = izquierda[ I ]
            I += 1
            K += 1

        while J < len( derecha ):
            lista[ K ] = derecha[ J ]
            J += 1
            K += 1
    return lista

def convertirMatrizALista(MATRIZ, FILAS, COLUMNAS):
    LISTA = []
    for FILA in range (FILAS):
        for COLUMNA in range(COLUMNAS):
            LISTA.append(MATRIZ[FILA][COLUMNA])
    return LISTA

#SUMA DE MATRICES
def OrdenarMatrizDeAcuerdoARegla(A):
    #Verificación de cantidad de filas y columnas
    FILAS_A = len(A)
    COLUMNAS_A = len(A[0])

    # Convertir matriz a lista
    LISTA_A = convertirMatrizALista(A, FILAS_A, COLUMNAS_A)

    #Ordenar matriz
    LISTA_A = mergeSort(LISTA_A)

    #reconstruir matriz
    elemento = 0
    for COLUMNA in range(COLUMNAS_A):
        for FILA in range(FILAS_A):
            A[FILA][COLUMNA] = LISTA_A[elemento]
            elemento = elemento + 1
    return A

MATRIZ1 = crearMatriz(3, 3)
leerMatriz(MATRIZ1)
print("Esta es la matriz 1:")
imprimirMatriz(MATRIZ1)


MATRIZ1 = OrdenarMatrizDeAcuerdoARegla(MATRIZ1)
print("Esta es la matriz ordenada")
imprimirMatriz(MATRIZ1)


