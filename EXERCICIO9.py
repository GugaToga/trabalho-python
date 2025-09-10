preco = float(input("Digite o preço do produto: "))

vip = input("O cliente é VIP? (s/n): ").lower()

if preco >= 100:
    desconto = 20
elif preco >= 50:
    desconto = 10
else:
    desconto = 0
if vip == "s":
    desconto += 5
preco_final = preco - (preco * desconto / 100)

print(f"Desconto aplicado: {desconto}%")
print(f"Preço final: R$ {preco_final:.2f}")
