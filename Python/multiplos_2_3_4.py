qtd = int(input())
lista = []
m_2 = 0
m_3 = 0
m_4 = 0

for i in range(qtd):
  lista.append(int(input()))
  if lista[i] % 2 == 0:
    m_2 = m_2 + 1
  if lista[i] % 3 == 0:
    m_3 = m_3 + 1
  if lista[i] % 4 == 0:
    m_4 = m_4 + 1

print(m_2)
print(m_3)
print(m_4)
