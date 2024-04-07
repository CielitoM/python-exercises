#Hallar un valor en una lista ordenada
#utilizando búsqueda binaria
import random

#Inicialización de la lista con valores aleatorios
def inicializacionListaRandom(longitud):
    lista = []
    for i in range(longitud):
        lista.append(random.randint(1,100))
    return lista

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


#Busqueda binaria iterativa
def busquedaBinaria(VECTOR, k, INICIO, FIN):
    if INICIO > FIN:
        POSICION = "not found"
    else:
        MEDIO = int((INICIO + FIN) / 2)
        if k == VECTOR[MEDIO]:
            POSICION = MEDIO
        else:
            if k < VECTOR[MEDIO]:
                FIN = MEDIO - 1
            else:
                INICIO = MEDIO + 1
            POSICION = busquedaBinaria(VECTOR, k, INICIO, FIN)
    return POSICION



lista = inicializacionListaRandom(30)
print("Lista sin ordenar y generada aleatoriamente: ", lista)
mergeSort(lista)
print("Lista ordenada con mergeSort", lista)
posicion = busquedaBinaria(lista, 1, 0, 30)
if posicion != "not found":
    print("La posicion es: " , posicion)
else:
    print("No se ha encontrado el elemento")