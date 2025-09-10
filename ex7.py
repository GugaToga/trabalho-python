idade = int(input("Idade: "))
renda = float(input("Renda mensal (R$): "))
dividas = float(input("Total de dívidas (R$): "))

percentual_divida = (dividas / renda) * 100 

if renda < 2000 and percentual_divida > 50:
    print("Sua classificação de risco é: ALTA")
elif 2000 <= renda <= 5000 or 30 <= percentual_divida <= 50:
    print("Sua classificação de risco é: MEDIA")
elif renda > 5000 and percentual_divida < 30:
    print("Sua classificação de risco é: BAIXA")
else:
    print("Sua classificação de risco é: MEDIA/BAIXA")

