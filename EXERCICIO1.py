salario = float(input("Digite o salário do funcionário: R$ "))
tempo = int(input("Digite o tempo de empresa (em anos): "))

if salario < 2000 and tempo >= 5:
    bonus = salario * 0.20
elif salario < 2000 and tempo < 5:
    bonus = salario * 0.10
elif salario >= 2000 and tempo >= 5:
    bonus = salario * 0.05
else:
    bonus = 0

print(f"\nSalário: R$ {salario:.2f}")
print(f"Tempo de empresa: {tempo} anos")
print(f"Bônus: R$ {bonus:.2f}")
print(f"Total a receber: R$ {salario + bonus:.2f}")
