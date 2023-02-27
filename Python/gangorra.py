dados = input().split()

gangorra = list(map(int, dados))

lado1 = gangorra[0] * gangorra[1]
lado2 = gangorra[2] * gangorra[3]

if lado1 == lado2:
  print(0)
elif lado1 > lado2:
  print(-1)
else:
  print(1)


