n = int(input())
f1 = list(map(int, input().split()))
f2 = list(map(int, input().split()))

Q1 = 0
Q2 = 0

if f1[0] > n/2 and f1[1] > n/2:
  Q1 = 1
if f2[0] > n/2 and f2[1] > n/2:
  Q2 = 1
  
if f1[0] <= n/2 and f1[1] > n/2:
  Q1 = 2
if f2[0] <= n/2 and f2[1] > n/2:
  Q2 = 2

if f1[0] <= n/2 and f1[1] <= n/2:
  Q1 = 3
if f2[0] <= n/2 and f2[1] <= n/2:
  Q2 = 3
  
if f1[0] > n/2 and f1[1] <= n/2:
  Q1 = 4
if f2[0] > n/2 and f2[1] <= n/2:
  Q2 = 4
  
if Q1 != Q2:
  print('S')
else:
  print('N')

