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
            MATRIZ[FILA][COLUMNA] = random.randint(0,1000)


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
def elementosComunesDeDosMatrices(A,B):
    #Verificación de cantidad de filas y columnas de A y B
    FILAS_A = len(A)
    COLUMNAS_A = len(A[0])
    FILAS_B = len(A)
    COLUMNAS_B = len(A[0])

    # Convertir ambas matrices a listas
    LISTA_A = convertirMatrizALista(A, FILAS_A, COLUMNAS_A)
    LISTA_B = convertirMatrizALista(B, FILAS_B, COLUMNAS_B)

    #Ordenar ambas matrices
    LISTA_A = mergeSort(LISTA_A)
    LISTA_B = mergeSort(LISTA_B)

    #Quitar elementos repetidos de las listas
    LISTA_A = list(set(LISTA_A))
    LISTA_B = list(set(LISTA_B))

    #Tomar los elementos no comunes de ambas listas.
    No_Comunes = set(LISTA_A) ^ set(LISTA_B)

    return  No_Comunes

MATRIZ1 = crearMatriz(8, 8)
MATRIZ2 = crearMatriz(8, 8)
leerMatriz(MATRIZ1)
leerMatriz(MATRIZ2)
print("Esta es la matriz 1:")
imprimirMatriz(MATRIZ1)
print("Esta es la matriz 2:")
imprimirMatriz(MATRIZ2)

V = elementosComunesDeDosMatrices(MATRIZ1,MATRIZ2)
if V != set():
    print("Resultado = ", V)
else:
    print("No se ha encontrado resultado")

