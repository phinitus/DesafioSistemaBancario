menu = """
[d] DEPOSITAR
[s] SACAR
[e] EXTRATO
[q] SAIR

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3

while True:

    opcao =input(menu)

    if opcao == "d":
        print("Depósito\n")
        deposito = float(input("Qual o valor deseja depositar? \n"))
        if deposito > 0:
            saldo = deposito
            extrato += f"Depósito: R${saldo:.2f}\n"
        else:
            print("Valor inválido!!!")
    elif opcao == "s":
        print("Saque\n")
        if numero_saques <= limite_saques:
            saque = float(input("Qual o valor deseja sacar? "))
            if saque > 0:
                if saque <= saldo:
                    if saque <= limite:
                     saldo -= saque
                     extrato += f"Saque: R${saldo:.2f}\n"
                    else:
                        print("Valor excede o limite Diário!!!")
                else:
                    print("Saldo Insuficiente!!!")
            else:
                print("Valor informado não é válido!!!")
        else:
            print("Número de saques excedido!!!")
        numero_saques += 1
    elif opcao == "e":
        print("Extrato\n")
        print(extrato)
        print("Seu saldo é: R$", saldo)
    elif opcao == "q":
        break
    else:
        print("Opção Inválida!!!")
