qtd = int(input())
gab = input()
res = input()
x = 0

for i in range(qtd):
  if gab[i] == res[i]:
    x = x + 1

print(x)
