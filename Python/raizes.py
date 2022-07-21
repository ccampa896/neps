from math import sqrt

qtd = int(input())
num = input().split()
aux = []

for i in range(qtd):
  aux.append(float(num[i]))

for i in range(qtd):
  print(f'{sqrt(aux[i]):.4f}')
