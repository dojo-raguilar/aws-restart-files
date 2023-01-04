n = int(input("Ingrese un numero: "))

def imprime_numeros(n):
  numeros = []
  for i in range(1, n+1):
    if i % 3 != 0:
     numeros.append(i)
  print(numeros)

imprime_numeros(n)
