saldo = 0 
limite = 500
extrato = ""
LIMITE_DE_SAQUES = 3
usuarios = list()
contas_correntes = list()
import os

def sacar(saldo, LIMITE_DE_SAQUES, extrato):

    #Quando ainda não excedeu o limite de saques diários
    if LIMITE_DE_SAQUES > 0: 

        valor_saque = float(input("\nQual valor deseja sacar?: "))
        print()

        if valor_saque <= 0:
            print("\nVocê deve sacar mais que R$0,00")
            print()

            return saldo, LIMITE_DE_SAQUES, extrato

        elif valor_saque > saldo:
            print("\nVocê não possui saldo suficiente.")
            print()

            return saldo, LIMITE_DE_SAQUES, extrato

        elif valor_saque > 500:
            print("\nVocê só pode sacar até R$500,00.")
            print()

            return saldo, LIMITE_DE_SAQUES, extrato

        else:
            saldo -= valor_saque
            LIMITE_DE_SAQUES -= 1
            extrato += f"\nVocê sacou R${valor_saque:.2f}"

            return saldo, LIMITE_DE_SAQUES, extrato

    #Quando já excedeu o limite de saques diários
    else:
        print("O limite de saques diários é 3. Você já excedeu esse limite")
        return saldo, LIMITE_DE_SAQUES, extrato

def depositar(saldo, extrato):
    valor_deposito = float(input("\nQual valor deseja depositar?: "))
    print(f"\nRS{valor_deposito:.2f} depositado")
    print()

    saldo += valor_deposito
    extrato += f"\nVocê depositou R${valor_deposito:.2f}"

    return saldo, extrato

def funcao_extrato(saldo, extrato):

    print()
    print("=" * 22)
    print("       EXTRATO        ")
    print("-" * 22)
    print(extrato)
    print()
    print(f"Seu saldo é: R${saldo:.2f}")
    print("=" * 22)
    
    return saldo, extrato

def criar_usuario(usuarios):

    while True:

        print()
        nome = input("Informe o nome completo do novo usuario: ")
        nascimento = input("Informe sua data de nascimento (DD-MM-AAAA):")

        while True:

            cpf = input("Informe seu CPF (somente números): ")
            cpf_existe = False

            for usuario in usuarios:
                if "CPF" in usuario and usuario["CPF"] == cpf:
                    cpf_existe = True
                    break

            if cpf_existe:
                print("Este CPF já está registrado em nossa base de dados.")

            else:
                break  # sai do while e continua com o cadastro

        endereco = input("Informe seu endereço completo (logradouro, número, bairro, cidade/UF): ")

        usuario = {
            "nome": nome,
            "nascimento": nascimento,
            "CPF": cpf,
            "endereco": endereco
        }

        usuarios.append(usuario)
        print("\nUsuário criado com sucesso!")
        return usuarios

def criar_conta_corrente(usuarios, contas_correntes):

    while True:

        nome = input("\nInforme o nome completo do titular da nova conta: ")
        nome_existe = False
        contador = 1

        for usuario in usuarios:
            if "nome" in usuario and usuario["nome"] == nome:
                nome_existe = True
                break

        if nome_existe:

            numero_da_conta = len(contas_correntes) + 1

            conta_corrente = {
                "agencia": "0001",
                "numero da conta": numero_da_conta,
                "usuario": nome
            }

            print()
            print("Agência: 0001")
            print(f"Número da conta: {numero_da_conta}")
            print(f"Titular: {nome}")

            contas_correntes.append(conta_corrente)
            contador += 1

            return usuarios, contas_correntes

        else:
            print("\nUsuário não encontrado. Será necessário realizar o cadastro.")
            break

            
    return usuarios, contas_correntes

while True: 

    os.system('cls')

    print("=" * 40)
    print("       SISTEMA BANCÁRIO PYTHON        ")
    print("=" * 40)

    print("""
    [d] Depositar 
    [s] Sacar
    [e] Extrato
    [c] Criar usuário
    [f] Criar conta corrente
    [q] Sair
    """)

    acao = input("👉  Escolha uma opção: ").lower()

    if acao == "d":
        saldo, extrato = depositar(saldo, extrato)
        input()

    elif acao == "s":
        saldo, LIMITE_DE_SAQUES, extrato = sacar(saldo, LIMITE_DE_SAQUES, extrato)

    elif acao == "e":
        saldo, extrato = funcao_extrato(saldo, extrato)
        input()

    elif acao == "c":
        usuarios = criar_usuario(usuarios)
        input()

    elif acao == "f":
        usuarios, contas_correntes = criar_conta_corrente(usuarios, contas_correntes)
        input()

    elif acao == "q":
        break