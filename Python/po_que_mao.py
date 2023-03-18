dados = []
for i in range(4):
    dados.append(int(input()))

doce = dados.pop(0)

cont = 0
dados.sort()

while doce > 0 and len(dados) > 0:
    doce -= dados.pop(0)
    if doce >= 0:
        cont += 1

print(cont)

