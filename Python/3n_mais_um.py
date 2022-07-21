def par(n):
    return n / 2

def impar(n):
    return (3 * n) + 1

num = int(input())
cont = 0

while num != 1:
    if num % 2 == 0:
        num = par(num)
        cont += 1
    else:
        num = impar(num)
        cont += 1
        
print(cont)
