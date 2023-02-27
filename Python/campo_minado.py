qtd = int(input())
campo = []
minas = []
mina = 0

for i in range(qtd):
  campo.append(int(input()))

for i in range(qtd):
  if qtd == 1:
    if campo[0] == 1:
      mina += 1
    minas.append(mina)
    mina = 0
  else:
    if i == 0:
      if campo[i] == 1:
        mina += 1
      if campo[i+1] == 1:
        mina += 1
      minas.append(mina)
      mina = 0
    elif i == (qtd-1):
      if campo[i-1] == 1:
        mina += 1
      if campo[i] == 1:
        mina += 1
      minas.append(mina)
      mina = 0
    else:
      if campo[i-1] == 1:
        mina += 1
      if campo[i] == 1:
        mina += 1
      if campo[i+1] == 1:
        mina += 1
      minas.append(mina)
      mina = 0

for i in range(qtd):
  print(minas[i])
