qtd = input()

cercas = list(map(int, input().split()))

troca = 0
conserto = 0

for i in range(len(cercas)):
  if cercas[i] < 50:
    troca += 1
  elif cercas[i] >= 50 and cercas[i] < 85:
    conserto += 1
    
print('%d %d' % (troca, conserto))


