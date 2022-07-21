qtd = int(input())
lista = [0, 1]
def fib(qtd):
  for i in range(2, qtd):
      aux = lista[(i-1)] + lista[(i-2)]
      lista.append(aux)

fib(qtd)

for i in range(qtd):
  print(f'{lista[i]} ', end='')
