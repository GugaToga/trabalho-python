nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))

if nota1 or nota2 or nota3 == 0:
    print("Reprovado automaticamente. (Zerado)")
else:
    media = (nota1 + nota2 + nota3) / 3
    print(f"Media: {media:.2f}")

    if media >= 7:
        print("Aprovado")
    elif media >= 5:
        print("Recuperação")
    else:
        print("Reprovado")