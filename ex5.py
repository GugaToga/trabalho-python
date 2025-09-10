dia = int(input("Dia: "))
mes = int(input("Mes: "))
ano = int(input("Ano: "))

if ano < 0 or ano > 2025:
    print("Data invalida (Ano fora do permitido).")
elif mes < 1 or mes > 12:
    print("Data invalida (Mes inexistente).")
else:
    dias_por_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        dias_por_mes[2] = 29

    if dia < 1 or dia > dias_por_mes[mes]:
        print("Data invalida (Dia inexistente).")
    else:
        print("Data valida!")








