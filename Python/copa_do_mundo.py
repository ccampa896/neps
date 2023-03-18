"""
vencedores = [[], [], [], [], []];

vencedores[0] = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
				'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']

for fase in range(1, 5):
	for i in range(0, len(vencedores[fase - 1]), 2):

		equipe1 = vencedores[fase - 1][i]
		equipe2 = vencedores[fase - 1][i + 1]

		gols1, gols2 = map(int, input().split())

		if gols1 > gols2:
			vencedores[fase].append(equipe1)
		else:
			vencedores[fase].append(equipe2)

print(vencedores[4][0])

"""


char = 'A'
copa = []

for i in range(0, 16, 2):
    aux = []
    aux.append(chr(ord(char)+i))
    aux.append(chr(ord(char)+i+1))
    copa.append(aux)
    aux = []


for i in range(8):
    res = list(map(int, input().split()))
    if res[0] > res[1]:
        copa[i].pop(1)
    else:
        copa[i].pop(0)


quartas = []
for i in range(0, 8, 2):
    aux = []
    aux.append(copa[i][0])
    aux.append(copa[i+1][0])
    quartas.append(aux)
    aux = []

for i in range(4):
    res = list(map(int, input().split()))
    if res[0] > res[1]:
        quartas[i].pop(1)
    else:
        quartas[i].pop(0)


semi = []
for i in range(0, 4, 2):
    aux = []
    aux.append(quartas[i][0])
    aux.append(quartas[i+1][0])
    semi.append(aux)
    aux = []


for i in range(2):
    res = list(map(int, input().split()))
    if res[0] > res[1]:
        semi[i].pop(1)
    else:
        semi[i].pop(0)

final = []

for i in range(2):
    final.append(semi[i][0])


res = list(map(int, input().split()))
if res[0] > res[1]:
    final.pop(1)
else:
    final.pop(0)

print(final[0])

