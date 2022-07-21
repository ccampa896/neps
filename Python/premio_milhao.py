dias = int(input())
acc = []
res = 0
deu = True
for i in range(dias):
  acc.append(int(input()))
  if (sum(acc) >= 1000000) and deu == True:
    res = i + 1
    deu = False
print(res)
