par = []
impar = []

for i in range(10):
    num = int(input())
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

qtd_p = len(par)
qtd_i = len(impar)

for i in range(qtd_p):
    if i == qtd_p - 1:
        print(f'{par[i]}')
    else:
        print(f'{par[i]} ', end = '')
for i in range(qtd_i):
    print(f'{impar[i]} ', end = '')
