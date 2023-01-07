#
#Dado un número entero n, escribir una función que imprima los números del 1 al n en una lista, excepto aquellos que son múltiplos de 3.
#
#
#Por ejemplo, si n es 10, la función debería imprimir: [1, 2, 4, 5, 7, 8, 10].

n = int(input("Ingrese un numero: "))

def imprime_numeros(n):
  numeros = []
  for i in range(1, n+1):
    if i % 3 != 0:
     numeros.append(i)
  print(numeros)

imprime_numeros(n)
