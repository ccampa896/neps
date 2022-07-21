A = False
B = False

qtd = int(input())
aux = input().split()
for i in range(qtd):
  if aux[i] == '1':
    A = not A
  if aux[i] == '2':
    A = not A
    B = not B

if A == True:
  print(1)
else:
  print(0)

if B == True:
  print(1)
else:
  print(0)
