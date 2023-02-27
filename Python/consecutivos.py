qtd = int(input())

dados = list(map(int, input().split()))

igual = 1
maior = 1

for i in range((len(dados)-1)):
  if dados[i] == dados[i+1]:
    igual += 1
    if igual > maior:
      maior = igual
  else:
    igual = 1

print(maior)


