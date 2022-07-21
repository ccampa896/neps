aux = input().split()
a = float(aux[0])
b = float(aux[1])

res = (a + b) / 2

if res >= 7:
  print('Aprovado')
elif res >= 4:
  print('Recuperacao')
else:
  print('Reprovado')
