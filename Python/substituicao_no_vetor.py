v = []

for i in range(10):
  v.append(int(input()))
  
m = min(v)

print(f'Menor: {m}')

o = []

for i in range(10):
  if v[i] == m:
    o.append(i)
    
print('Ocorrencias: ', end='')

for i in range(len(o)):
  if i == (len(o)-1):
    print(o[i])
  else:
    print(o[i], end = ' ')

for i in range(10):
  if v[i] == m:
    v[i] = -1

for i in range(10):
  if i == 9:
    print(v[i])
  else:
    print(v[i], end = ' ')

