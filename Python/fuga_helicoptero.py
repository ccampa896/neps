
"""
# Lendo os valores de entrada
helicoptero, policial, fugitivo, direcao = [int(i) for i in input().split()]

fator = "S" # Definindo a variável de impressão como positiva

# É criado um ciclo infinito, mas as condições de encerramento estão presentes
while True:
  # Caso saia do limite da roda, acerte o valor ao correspondente
  if(fugitivo == 16 and direcao == 1): fugitivo = 0
  if(fugitivo == -1 and direcao == -1): fugitivo = 15

  # Se a posição do fugitivo é igual ao do helicóptero, encerra-se o ciclo
  if(fugitivo == helicoptero): break

  # Se a posição do fugitivo é igual aao do policial, muda-se a variável e encerra-se o ciclo
  if(fugitivo == policial):
    fator = "N"
    break

  # Acrescenta ou diminui 1 a posição dependendo do sentido do fugitivo.
  if(direcao == 1): fugitivo += 1
  if(direcao == -1): fugitivo -= 1

print(fator) # Imprimindo resultado






"""







pos = list(map(int, input().split()))


"""
                P                    H                      F
[0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12] [13] [14] [15]

"""

H = pos[0]
P = pos[1]
F = pos[2]
D = pos[3]

if F < H and H < P:
  if D == 1:
    print('S')
  else:
    print('N')
elif F < P and P < H:
  if D == 1:
    print('N')
  else:
    print('S')
elif F > P and F < H:
  if D == 1:
    print('S')
  else:
    print('N')
elif F > H and F < P:
  if D == 1:
    print('N')
  else:
    print('S')
elif F > P and P > H:
  if D == 1:
    print('S')
  else:
    print('N')
elif F > H and H > P:
  if D == 1:
    print('N')
  else:
    print('S')

