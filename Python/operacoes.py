op = input()
num = list(map(float, input().split()))
res = 0

if op == 'M':
  res = num[0] * num[1]
  print('%.2f' % res)
else:
  res = num[0] / num[1]
  print('%.2f' % res)
