c = []

for i in range(3):
  c.append(int(input()))
  
if (c[2] > c[0] + c[1]) or (c[2] > c[1] and c[1] > c[0]):
  print(1)
elif c[2] > c[1] or c[2] > c[0]:
  print(2)
else:
  print(3)
 
