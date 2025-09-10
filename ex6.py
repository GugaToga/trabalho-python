idade = int(input("Idade: "))
nacionalidade = int(input("Nacionalidade-\n1- Brasileiro\n2- Estrangeiro\n>: "))

if idade > 150 or idade < 0 :
    print("Idade invalida.")
elif nacionalidade > 2 or nacionalidade < 1 :
    print("Nacionalidade invalida.")
else :
    if idade < 16 :
        print("Você não pode votar.")
    elif idade >= 18 and nacionalidade == 1 :
        print("Você pode votar!")
    elif idade >= 18 and nacionalidade == 2 :
        print("Voce pode votar! (Opcionalmente)")
    elif idade < 18 and idade > 15 :
        print("Voce pode votar! (Opcionalmente)")
    
