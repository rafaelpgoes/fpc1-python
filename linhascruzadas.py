entrada = int(input())
numeros = [int(i) for i in input().split()]
contador = 0

for i in range(entrada):
  for j in range(i+1):
    if numeros[j] > numeros[i]:
      contador += 1
print(contador)