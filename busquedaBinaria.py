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
def busquedaBinariaIterativa(lista, elemento):
    medio = int(len(lista)/2)
    if(lista[medio] < elemento):
        if (len(lista) == 1):
            return 0
        busquedaBinariaIterativa(lista[medio:], elemento)
    elif(lista[medio] > elemento):
        busquedaBinariaIterativa(lista[:medio], elemento)
        if (len(lista) == 1):
            return 0
    elif(lista[medio] == elemento):
        return medio

def bus_bin(VEC, k, INI, FIN):
    if INI > FIN:
        POSICION = 0
    else:
        MED = int((INI + FIN) / 2)
        if k == VEC[MED]:
            POSICION = MED
        else:
            if k < VEC[MED]:
                FIN = MED - 1
            else:
                INI = MED + 1
            POSICION = bus_bin(VEC, k, INI, FIN)
        return POSICION



lista = inicializacionListaRandom(30)
print("Lista sin ordenar y generada aleatoriamente: ", lista)
mergeSort(lista)
print("Lista ordenada con mergeSort", lista)
posicion = bus_bin(lista, 1, 1, 30)
if posicion:
    print("La posicion es: " , posicion)
else:
    print("No se ha encontrado el elemento")