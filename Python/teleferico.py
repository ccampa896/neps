cap = int(input())
tel = int(input())

if cap > tel:
    print(1)
else:
    aux1 = cap - 1
    if (tel % aux1) == 0:
        aux2 = tel / aux1
        print(int(aux2))
    else:
        aux2 = (tel // aux1) + 1
        print(int(aux2))
