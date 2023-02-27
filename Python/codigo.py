qtd = input()

dados = input().split()
cont = 0

for i in range(len(dados)-2):
  if dados[i] == '1':
    if dados[i+1] == '0':
      if dados[i+2] == '0':
        cont += 1

print(cont)

