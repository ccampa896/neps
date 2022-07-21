risada = input()
opt = []
igual = 0
tam = len(risada)
for i in range(tam):
  if (risada[i] == 'a') or (risada[i] == 'e') or (risada[i] == 'i') or (risada[i] == 'o') or (risada[i] == 'u'):
    opt.append(risada[i])

tam2 = len(opt)
str = []

for i in range((tam2-1), -1, -1):
  str.append(opt[i])

for i in range(tam2):
  if opt[i] == str[i]:
    igual = igual + 1

if igual == tam2:
  print('S')
else:
  print('N')
