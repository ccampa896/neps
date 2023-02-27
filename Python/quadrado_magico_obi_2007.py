"""
--> exemplo

matriz = [
  [2 7 6],
  [9 5 1],
  [4 3 8]
         ]
"""

tam = int(input())
mat = []
linha = []

for i in range(tam):
  linha = list(map(int, input().split()))
  mat.append(linha)
  linha = []

magico = 0
quad = False
soma = []

while not quad:
  for i in range(tam):
    soma.append(sum(mat[i]))

  conjunto = set(soma)
  if len(conjunto) == 1:
    conj = list(conjunto)
    magico = conj[0]
    quad = True

  soma = []
  coluna = 0

  for i in range(tam):
    for j in range(tam):
      coluna += mat[j][i]
    soma.append(coluna)
    coluna = 0

  conjunto = set(soma)
  if len(conjunto) == 1:
    conj = list(conjunto)
    if conj[0] == magico:
      quad = True
    else:
      quad = False
      break
  else:
    quad = False
    break
      
  soma = []
  diagonal = 0

  for i in range(tam):
    diagonal += mat[i][i]
  soma.append(diagonal)

  diagonal = 0
  i = tam - 1
  j = 0

  while (j < tam) and (i >= 0):
    diagonal += mat[j][i]
    j += 1
    i -= 1
  soma.append(diagonal)

  conjunto = set(soma)
  if len(conjunto) == 1:
    conj = list(conjunto)
    if conj[0] == magico:
      quad = True
    else: 
      quad = False
      break
  else:
    quad = False
    break
    
if quad:
  print(magico)
else:
  print(-1)

