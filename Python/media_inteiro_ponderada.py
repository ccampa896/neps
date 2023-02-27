import math

notas = []
for i in range(2):
  notas.append(int(input()))
  
media = ((notas[0] * 4) + (notas[1] * 6)) / 10

print(math.ceil(media))

