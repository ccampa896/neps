cartas = []
igual = 0
for i in range(3):
  cartas.append(int(input()))

cartas.sort()

for i in range(3):
  if i > 0:
    if cartas[i] == cartas[i-1]:
      igual = cartas[i]
      cartas.remove(igual)
      cartas.remove(igual)
      break
    
print(cartas[0])

