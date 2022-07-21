aux = input().split()
t1 = int(aux[0])
t2 = int(aux[1])
t3 = int(aux[2])

if (t1 == t2) or (t1 == t3) or (t2 == t3):
  print('S')
elif (t1 + t2 == t3) or (t1 + t3 == t2) or (t2 + t3 == t1):
  print('S')
else:
  print('N')
