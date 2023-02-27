dados = []
for i in range(3):
  dados.append(int(input()))
  
pos = [1, 2, 3]

aux = list(zip(pos, dados))
dicionario = dict(aux)

for i in sorted(dicionario, key = dicionario.get):
  print(i)



