qtd = int(input())
lista = []

for i in range(qtd):
  lista.append(int(input()))

num = int(input())

l = 0
r = qtd - 1

while l <= r:
    soma = lista[l]+lista[r]
    if soma == num:
        print(lista[l], lista[r])
        break
    elif soma < num:
        l+=1
    else:
        r-=1
