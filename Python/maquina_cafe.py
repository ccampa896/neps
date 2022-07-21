andar = []
for i in range(3):
  andar.append(int(input()))

t = []

t.append(int((andar[1] * 2) + (andar[2] * 4)))
t.append(int((andar[0] * 2) + (andar[2] * 2)))
t.append(int((andar[0] * 4) + (andar[1] * 2)))

print(min(t))
