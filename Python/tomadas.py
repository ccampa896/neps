aux = input().split()
tomadas = []
for i in range(4):
  tomadas.append(int(aux[i]))

total = 0
for i in range(3):
  total += (tomadas[i] - 1)

total += tomadas[3]

print(total)
