qtd = int(input())

dic = {}

for i in range(qtd):
  aux = input().split()
  dic[aux[0]] = aux[1]

frase = input().split()

for i in range(len(frase)):
  if i < (len(frase)-1):
    print(dic[frase[i]], end=' ')
  else:
    print(dic[frase[i]])

