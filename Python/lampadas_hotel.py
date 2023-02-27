lamp = list(map(int, input().split()))

if lamp[0] == lamp[2] and lamp[1] == lamp[3]:
  print(0)
elif (lamp[0] != lamp[2] and lamp[1] != lamp[3]) or (lamp[0] != lamp[2] and lamp[1] == lamp[3]):
  print(1)
else:
  print(2)

