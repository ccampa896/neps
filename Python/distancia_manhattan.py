dados = input().split()

dist = list(map(int, dados))

res = abs((dist[2] - dist[0])) + abs((dist[3] - dist[1]))

print(res)
