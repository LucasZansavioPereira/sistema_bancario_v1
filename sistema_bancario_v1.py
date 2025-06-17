saldo = 0
limite = 500
extrato = ""
LIMITE_DE_SAQUES = 3

while True:

    print('''
      
    [d] Depositar 
    [s] Sacar
    [e] Extrato
    [q] Sair
      
''')

    acao = input("Olá, o que você precisa fazer hoje?: ").lower()

    if acao == "d":
        valor_deposito = float(input("\nQual valor deseja depositar?: "))

        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"\nVocê depositou R${valor_deposito:.2f}"

        else:
            print("\nO valor deve ser maior que R$0")

    elif acao == "s":

        if LIMITE_DE_SAQUES > 0:
            valor_saque = valor_saque = float(input("\nQual valor deseja sacar?: "))

            if valor_saque <= 0:
                print("\nVocê deve sacar mais que R$0,00")

            if valor_saque > saldo:
                print("\nVocê não possui saldo suficiente.")

            elif valor_saque > 500:
                print("\nVocê só pode sacar até R$500,00.")

            else:
                saldo -= valor_saque
                LIMITE_DE_SAQUES -= 1
                extrato += f"\nVocê sacou R${valor_saque:.2f}"

        else:
            print("\nVocê excedeu seu limite de saques diários")

    elif acao == "e":
        print(extrato)
        print(f"\nSeu saldo é: R${saldo:.2f}")

    elif acao == "q":
        print('''
              
    Até mais!
              
''')
        break

    else:
        print("Opção Inválida")