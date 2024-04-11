# Una matriz representa la imagen de una zona del mar donde se encuentra una isla.
# Cada celda representa un cuadro de 100 por 100 metros de superficie y la isla puede
# tocar los bordes de la imagen. Los cuadros con valor 1 representan tierra de la isla y
# los cuadros con valor cero representan el mar. Escribir un programa que calcule el perímetro y
# el área de la isla.


class Coordenada:
    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna

    def __str__(self):
        return f"({self.fila}, {self.columna})"

    @staticmethod
    def esta_en_lista(lista_coordenadas, coordenada):
        # Coordenada.imprimir_lista(lista_coordenadas)
        # print(coordenada)
        """
        Verifica si una coordenada está presente en una lista de coordenadas.

        Args:
        - lista_coordenadas: La lista de coordenadas a verificar.
        - coordenada: La coordenada a buscar en la lista.

        Returns:
        - True si la coordenada está en la lista, False de lo contrario.
        """
        for c in lista_coordenadas:
            if c.fila == coordenada.fila and c.columna == coordenada.columna:
                return True
        return False

    @staticmethod
    def imprimir_lista(lista_coordenadas):
        """
        Imprime una lista de coordenadas.

        Args:
        - lista_coordenadas: La lista de coordenadas a imprimir.
        """
        # Imprime el inicio de la lista
        print("[", end="")
        # Itera sobre las coordenadas en la lista
        for i, c in enumerate(lista_coordenadas):
            # Imprime cada coordenada en el formato (fila, columna)
            print(f"({c.fila}, {c.columna})", end="")
            # Agrega una coma si no es la última coordenada
            if i < len(lista_coordenadas) - 1:
                print(", ", end="")
        # Imprime el final de la lista
        print("]")


def imprimirMatriz(MATRIZ):
    FILAS = len(MATRIZ)
    for FILA in range(FILAS):
        print(MATRIZ[FILA])


def determinarIslasAdyacentes(listasUnosyCeros, coordenadas_a_recorrer, coordenadas_recorridas):
    contador = 0  # Contador para verificar cuál de los elementos alrededor de la isla es porción de isla (1)
    # porción de agua

    # print("Coordenadas que se van a recorrer:")
    # Coordenada.imprimir_lista(coordenadas_a_recorrer)
    # print("Coordenadas que ya fueron recorridas:")
    # Coordenada.imprimir_lista(coordenadas_recorridas)

    for elemento in range(len(listasUnosyCeros)):

        coordenada = coordenadas_a_recorrer[elemento]  # Se guarda la coordenada de la porción 1 o 0
        # Si la porción es agua y además, la coordenada de la porción no se encuentra en la lista de coordenadas
        # Que ya fueron previamente recorridas
        if listasUnosyCeros[elemento] == 0 and not Coordenada.esta_en_lista(coordenadas_recorridas, coordenada):
            contador = contador + 1
            coordenadas_recorridas.append(coordenadas_a_recorrer[elemento])  # Se agrega nueva coordeanda recorrida

    if contador == 4:
        return 400, coordenadas_recorridas
    elif contador == 3:
        return 300, coordenadas_recorridas
    elif contador == 2:
        return 200, coordenadas_recorridas
    elif contador == 1:
        return 100, coordenadas_recorridas
    elif contador == 0:
        return 0, coordenadas_recorridas


# HALLAR PERIMETRO DE LA ISLA
def hallarPerimetroDeLaIsla(A):
    FILAS = len(A)
    COLUMNAS = len(A[0])
    perimetro = 0
    listasUnosyCeros = []  # Lista donde se almacenará los "1" y "0" respectivos de cada coordenada
    coordenadas_recorridas = []  # Lista donde se almacenarán las coordenadas que ya han sido recorridas
    # para evitar medir el perímetro dos veces

    for FILA in range(FILAS):
        for COLUMNA in range(COLUMNAS):

            if A[FILA][COLUMNA] == 1:  # Si se encuentra una porción de isla
                # se verifica que no se trate de un caso donde llega al final de la matriz
                if FILA - 1 > -1 and FILA + 1 < FILAS and COLUMNA - 1 > -1 and COLUMNA + 1 < COLUMNAS:

                    listasUnosyCeros.append(A[FILA - 1][COLUMNA])  # arriba
                    listasUnosyCeros.append(A[FILA + 1][COLUMNA])  # abajo
                    listasUnosyCeros.append(A[FILA][COLUMNA + 1])  # derecha
                    listasUnosyCeros.append(A[FILA][COLUMNA - 1])  # izquierda

                    # Agregar coordenadas que se van a verificar si ya fueron recorridas para evitar
                    # repetir coordenadas ya visitadas

                    coordenadas_a_recorrer = [Coordenada(FILA - 1, COLUMNA),
                                              Coordenada(FILA + 1, COLUMNA),
                                              Coordenada(FILA, COLUMNA + 1),
                                              Coordenada(FILA, COLUMNA - 1)]

                    # Se llama a la función para verificar el perímetro por cada celda. Se envia la listas de 1
                    # y 0 para contar los perímetros, las coordenadas a recorrer para evitar un contar perímetro que
                    # ya fue contado (para ello usar la lista de coordenadas), y las coordenadas que ya fueron recorridas
                    # para realizar la verificación.

                    resultadoPerimetroPorCelda, coordenadas_recorridas = determinarIslasAdyacentes(listasUnosyCeros,
                                                                                                   coordenadas_a_recorrer,
                                                                                                   coordenadas_recorridas)
                    perimetro = perimetro + resultadoPerimetroPorCelda

                    listasUnosyCeros = []

                else:
                    # Existen 10 POSIBILIDADES en donde puede haber una porción de isla en un extremo de la matriz.

                    # 1. ARRIBA e IZQUIERDA (final de la matriz)
                    if FILA - 1 == -1 and COLUMNA - 1 == -1:
                        # Se verifican si las porciones adyacentes son 1 o 0, para determinar su perimetro
                        listasUnosyCeros.append(A[FILA + 1][COLUMNA])  # abajo
                        listasUnosyCeros.append(A[FILA][COLUMNA + 1])  # derecha
                        # Se agregan sus respectivas coordenadas
                        coordenadas_a_recorrer = [Coordenada(FILA + 1, COLUMNA),  # abajo
                                                  Coordenada(FILA, COLUMNA + 1)]  # derecha
                        # Se realiza el mismo procedimiento
                        resultadoPerimetroPorCelda, coordenadas_recorridas = determinarIslasAdyacentes(listasUnosyCeros,
                                                                                                       coordenadas_a_recorrer,
                                                                                                       coordenadas_recorridas)
                        perimetro = perimetro + resultadoPerimetroPorCelda + 200 # Se suma el perímetro 200 porque choca
                        # con 2 extremos de la matriz, y se consideran como perimetros

                        listasUnosyCeros = []

                    # ARRIBA y DERECHA (final de la matriz)
                    if FILA - 1 == -1 and COLUMNA + 1 == COLUMNAS:
                        listasUnosyCeros.append(A[FILA + 1][COLUMNA])  # abajo
                        listasUnosyCeros.append(A[FILA][COLUMNA - 1])  # izquierda
                        coordenadas_a_recorrer = [Coordenada(FILA + 1, COLUMNA),
                                                  Coordenada(FILA, COLUMNA - 1)]
                        resultadoPerimetroPorCelda, coordenadas_recorridas = determinarIslasAdyacentes(listasUnosyCeros,
                                                                                                       coordenadas_a_recorrer,
                                                                                                       coordenadas_recorridas)
                        perimetro = perimetro + resultadoPerimetroPorCelda + 200
                        listasUnosyCeros = []

                    # ABAJO e IZQUIERDA (final de la matriz)
                    if FILA + 1 == FILAS and COLUMNA - 1 == -1:
                        listasUnosyCeros.append(A[FILA - 1][COLUMNA])  # arriba
                        listasUnosyCeros.append(A[FILA][COLUMNA + 1])  # derecha
                        coordenadas_a_recorrer = [Coordenada(FILA - 1, COLUMNA),
                                                  Coordenada(FILA, COLUMNA + 1)]
                        resultadoPerimetroPorCelda, coordenadas_recorridas = determinarIslasAdyacentes(listasUnosyCeros,
                                                                                                       coordenadas_a_recorrer,
                                                                                                       coordenadas_recorridas)
                        perimetro = perimetro + resultadoPerimetroPorCelda + 200
                        listasUnosyCeros = []

                    # ABAJO y DERECHA (final de la matriz)
                    if FILA + 1 == FILAS and COLUMNA + 1 == COLUMNAS:
                        listasUnosyCeros.append(A[FILA - 1][COLUMNA])  # arriba
                        listasUnosyCeros.append(A[FILA][COLUMNA - 1])  # izquierda
                        coordenadas_a_recorrer = [Coordenada(FILA - 1, COLUMNA),
                                                  Coordenada(FILA, COLUMNA - 1)]
                        resultadoPerimetroPorCelda, coordenadas_recorridas = determinarIslasAdyacentes(listasUnosyCeros,
                                                                                                       coordenadas_a_recorrer,
                                                                                                       coordenadas_recorridas)
                        perimetro = perimetro + resultadoPerimetroPorCelda + 200
                        listasUnosyCeros = []

                    # ABAJO
                    if FILA + 1 == FILAS and COLUMNA + 1 != COLUMNAS and COLUMNA - 1 != -1:
                        listasUnosyCeros.append(A[FILA - 1][COLUMNA])  # arriba
                        listasUnosyCeros.append(A[FILA][COLUMNA - 1])  # izquierda
                        listasUnosyCeros.append(A[FILA][COLUMNA + 1])  # derecha
                        coordenadas_a_recorrer = [Coordenada(FILA - 1, COLUMNA),
                                                  Coordenada(FILA, COLUMNA - 1),
                                                  Coordenada(FILA, COLUMNA + 1)]
                        resultadoPerimetroPorCelda, coordenadas_recorridas = determinarIslasAdyacentes(listasUnosyCeros,
                                                                                                       coordenadas_a_recorrer,
                                                                                                       coordenadas_recorridas)
                        perimetro = perimetro + resultadoPerimetroPorCelda + 100
                        listasUnosyCeros = []

                    # ARRIBA
                    if FILA - 1 == -1 and COLUMNA + 1 != COLUMNAS and COLUMNA - 1 != -1:
                        listasUnosyCeros.append(A[FILA + 1][COLUMNA])  # abajo
                        listasUnosyCeros.append(A[FILA][COLUMNA - 1])  # izquierda
                        listasUnosyCeros.append(A[FILA][COLUMNA + 1])  # derecha
                        coordenadas_a_recorrer = [Coordenada(FILA + 1, COLUMNA),
                                                  Coordenada(FILA, COLUMNA - 1),
                                                  Coordenada(FILA, COLUMNA + 1)]
                        resultadoPerimetroPorCelda, coordenadas_recorridas = determinarIslasAdyacentes(listasUnosyCeros,
                                                                                                       coordenadas_a_recorrer,
                                                                                                       coordenadas_recorridas)
                        perimetro = perimetro + resultadoPerimetroPorCelda + 100
                        listasUnosyCeros = []

                    # IZQUIERDA
                    if COLUMNA - 1 == -1 and FILA + 1 != FILAS and FILA - 1 != -1:
                        listasUnosyCeros.append(A[FILA + 1][COLUMNA])  # abajo
                        listasUnosyCeros.append(A[FILA - 1][COLUMNA])  # arriba
                        listasUnosyCeros.append(A[FILA][COLUMNA + 1])  # derecha
                        coordenadas_a_recorrer = [Coordenada(FILA + 1, COLUMNA),
                                                  Coordenada(FILA - 1, COLUMNA),
                                                  Coordenada(FILA, COLUMNA + 1)]
                        resultadoPerimetroPorCelda, coordenadas_recorridas = determinarIslasAdyacentes(listasUnosyCeros,
                                                                                                       coordenadas_a_recorrer,
                                                                                                       coordenadas_recorridas)
                        perimetro = perimetro + resultadoPerimetroPorCelda + 100
                        listasUnosyCeros = []

                    # DERECHA
                    if COLUMNA + 1 == COLUMNAS and FILA + 1 != FILAS and FILA - 1 != -1:
                        listasUnosyCeros.append(A[FILA + 1][COLUMNA])  # abajo
                        listasUnosyCeros.append(A[FILA - 1][COLUMNA])  # arriba
                        listasUnosyCeros.append(A[FILA][COLUMNA - 1])  # izquierda
                        coordenadas_a_recorrer = [Coordenada(FILA + 1, COLUMNA),
                                                  Coordenada(FILA - 1, COLUMNA),
                                                  Coordenada(FILA, COLUMNA - 1)]
                        resultadoPerimetroPorCelda, coordenadas_recorridas = determinarIslasAdyacentes(listasUnosyCeros,
                                                                                                       coordenadas_a_recorrer,
                                                                                                       coordenadas_recorridas)
                        perimetro = perimetro + resultadoPerimetroPorCelda + 100
                        listasUnosyCeros = []

    return perimetro


# HALLAR EL ÁREA DE LA ISLA
def hallarAreaDeLaIsla(A):
    FILAS = len(A)
    COLUMNAS = len(A[0])
    contador = 0
    for FILA in range(FILAS):
        for COLUMNA in range(COLUMNAS):
            if A[FILA][COLUMNA] == 1:
                contador = contador + 1

    area = contador * 100 * 100
    return area


print("Esta es la matriz 1:")
MATRIZ1 = [
    [1, 1, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [0, 0, 1, 1, 1, 1, 0],
    [1, 0, 0, 1, 1, 1, 0],
    [1, 1, 0, 0, 0, 0, 1]
]
imprimirMatriz(MATRIZ1)

perimetro = hallarPerimetroDeLaIsla(MATRIZ1)
print("El perimetro de la matriz es = ", perimetro, "u")
area = hallarAreaDeLaIsla(MATRIZ1)
print("El perimetro de la matriz es = ", area, "u2")


print("Esta es la matriz 2:")
MATRIZ2 = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [0, 0, 1, 1, 1, 1, 0],
    [0, 0, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0]
]
imprimirMatriz(MATRIZ2)

perimetro = hallarPerimetroDeLaIsla(MATRIZ2)
print("El perimetro de la matriz es = ", perimetro, "u")
area = hallarAreaDeLaIsla(MATRIZ2)
print("El perimetro de la matriz es = ", area, "u2")
