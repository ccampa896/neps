idades = []

for i in range(3):
  idades.append(int(input()))
  
dona = idades[0]

filho = dona - (idades[1] + idades[2])

filhos = [filho, idades[1], idades[2]]

print(max(filhos))
