qtd = int(input())
copos = 0

for i in range(qtd):
  dados = input().split()
  bandeja = list(map(int, dados))
  if bandeja[0] > bandeja[1]:
    copos += bandeja[1]

print(copos)


