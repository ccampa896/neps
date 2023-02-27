num = int(input())
divisor = []

for i in range(1, (num+1)):
  if (num % i) == 0:
    divisor.append(i)

for i in range(len(divisor)):
  if i == (len(divisor) - 1):
    print('%d ' % divisor[i])
  else:
    print('%d ' % divisor[i], end = '')
