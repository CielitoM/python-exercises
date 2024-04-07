def factorialFunc(n):
    fac = 1
    for i in range (1, n+1):
        fac = fac * i
    return fac

def factorial(n):
    resultado = 1
    if n == 0:
        resultado = 1
    elif n > 1:
        resultado = n * factorial(n - 1)
    return resultado


print("Esta es la función factorial sin recursión:")
resultado1 = factorialFunc(10)
print(resultado1)
print("Esta es la función factorial con recursión:")
resultado2 = factorial(10)
print(resultado2)