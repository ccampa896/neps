from collections import Counter

qtd = int(input())
lista = []

for i in range(qtd):
  lista.append(int(input()))
  
cont = Counter(lista)

res = cont.most_common(1)

igual = []

for chave in cont.items():
  if res[0][1] == chave[1]:
    igual.append(chave)

igual.sort()

for i in range(len(igual)):
  if i < (len(igual)-1):
    print(igual[i][0], end=' ')
  else:
    print(igual[i][0])

