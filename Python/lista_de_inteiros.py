lista_de_inteiros = map(int, input().split())

resultado = [numero * 2 if numero % 2 == 0 else numero * 3 for numero in lista_de_inteiros]

print(resultado)

