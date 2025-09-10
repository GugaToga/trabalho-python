correta = ['B', 'C', 'D', 'A']

print("Escolha a sequência de 4 cartas (A, B, C ou D):")
usuario = []

for i in range(4):
    carta = input(f"Carta {i+1}: ").upper()
    usuario.append(carta)

pontos = 0

for i in range(4):
    if usuario[i] == correta[i]:
        pontos += 10

pontos += usuario.count('A') * 5

for i in range(3):
    if usuario[i] == 'C' and usuario[i+1] == 'D':
        pontos += 5
        break  


if pontos > 50:
    pontos = 50

print("Sequência correta:", correta)
print("Sua sequência:", usuario)
print("Pontuação final:", pontos)

