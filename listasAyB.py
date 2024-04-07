# Se cuenta con dos listas A y B, ambas ordenadas ascendentemente. Se requiere
# escribir un programa en Python que reciba estas listas y las integre en una lista única C
# ordenada ascendentemente.

A = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
B = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

#Sin recursion
def concatenarDosListas(Lista1, Lista2):
    Lista3 = []
    for elemento in Lista1:
        Lista3.append(elemento)
    for elemento in Lista2:
        Lista3.append(elemento)

    return(Lista3)

#Con recursión usando MERGESORT
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


print("Lista A: ", A)
print("Lista B: ", B)


C = concatenarDosListas(A, B)
print("Sin usar recursión, ordenar la lista C: ", C)
C.sort()
print("Lista ordenada: ", C)

C = concatenarDosListas(A, B)
print("Usando mergeSort, ordenar la lista C: ", C)
mergeSort(C)
print("Lista ordenada: ", C)

