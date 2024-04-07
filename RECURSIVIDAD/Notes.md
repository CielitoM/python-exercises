## Método `.sort()` en Python

- **Función**: Ordena la lista en su lugar, modificando la lista original y no devolviendo una nueva lista.

- **Comparaciones**: Se utilizan solo comparaciones `<` entre elementos de la lista. No se utilizan excepciones, por lo que si alguna operación de comparación falla, toda la operación de ordenación fallará.

- **Argumentos**:
  - `key`: Especifica una función de un argumento que se utiliza para extraer una clave de comparación de cada elemento de la lista. Por ejemplo, `key=str.lower`. El valor predeterminado de `None` significa que los elementos de la lista se ordenan directamente sin calcular un valor de clave separado.
  - `reverse`: Es un valor booleano. Si se establece en `True`, los elementos de la lista se ordenan como si cada comparación estuviera invertida.

- **Estabilidad**: Garantiza ser estable. Una ordenación es estable si no cambia el orden relativo de los elementos que se comparan iguales.

- **Modificación in-place**: Modifica la secuencia en su lugar para economía de espacio cuando se ordena una secuencia grande. No devuelve la secuencia ordenada.

- **Implementación de CPython**: Durante la ordenación, si intentas mutar o incluso inspeccionar la lista, el efecto es indefinido. La implementación en C de Python hace que la lista parezca vacía durante la duración de la ordenación y lanza un `ValueError` si puede detectar que la lista ha sido modificada durante la ordenación.
