import math
aux = input().split()
num = []

for i in range(4):
    num.append(int(aux[i]))

dist = math.sqrt((num[0] - num[2])**2 + (num[1] - num[3])**2)

print('%.2f' % dist)
