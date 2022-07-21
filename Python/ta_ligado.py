pontes = set()
aux = input().split()
qtd = int(aux[1])

for i in range(qtd):
    x, y, z = map(int, input().split())
    aux = []
    aux.append(y)
    aux.append(z)
    if x == 0:
        if frozenset(sorted(aux)) in pontes:
            print(1)
        else:
            print(0)
    else:
        pontes.add(frozenset(sorted(aux)))
