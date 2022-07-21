aux = input().split()
A = int(aux[0])
B = int(aux[1])
C = int(aux[2])

if A == B and B == C:
  print('*')
elif B == C and B != A:
  print('A')
elif A == C and C != B:
  print('B')
else:
  print('C')
