def menu(lista):
    c = 1
    for item in lista:
        c += 1
    opc = (input('Sua opção'))
    return opc


def depositar(saldo,valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Deposito:\tR$ {valor:.2f}\n"
    else:
        print("\n @@@ Operação falhou! O valor informado é invalido @@@")
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite,numero_de_saques,limite_saques):

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_de_saques > limite_saques

    if excedeu_saldo:
        print("\n @@@ Operação falhou, Você não tem saldo suficiente. @@@")

    elif excedeu_limite:
        print("\n @@@ Operação falhou, O valor do saque excede o limite. @@@")

    elif excedeu_saques:
        print("\n @@@ Operação falhou, Número Máximo de saques excedido. @@@")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_de_saques += 1
        print("\n=== Saque realizado com Sucesso! ===")
    else:
        print("\n @@@ Operação falhou! O valor informado é invalido @@@")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n=============== EXTRATO ===============")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: \t\tR$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(usuarios):
    cpf = input("\nInforme o CPF (somente número): ")
    usuario = filtrar_usuario(cpf,usuarios)

    if usuario:
        print("\n Usuario criado com sucesso!")
        return
    nome = input("\nDigite o nome completo: ")
    data_nascimento = input("\nInforme a data de nascimento (dd-mm-aaaa): ")
    endereco = input("informe o endereço (logadouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereço": endereco})
    print("=== Usuário criado com sucesso! ===")

def filtrar_usuario(cpf,usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("\n Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("\n @@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
        Agência: \t{conta["agencia"]}
        C/C:\t\t{conta["numero_conta"]}
        Titular:\t{conta["usuario"]["nome"]}
        """
        print("="*100)
        print(linha)


def main():
    LIMITE_SAQUES =3
    AGENCIA = "0001"
    saldo = 0
    limite = 500
    extrato = ""
    numero_de_saques = 0
    usuarios = []
    contas = []


    while True:
        escolha = menu([
        "[d]\tDepositar"
        "[s]\tSacar",
        "[e]\tExtrato",
        "[nc]\tNova conta",
        "[lc]\tListar contas",
        "[nu]\tNovo usuário",
        "[q]\tSair"
        ])

        if escolha == "d":
            valor = float(input("Digite o valor do saque: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif escolha == "s":
            valor = float(input("Digite o valor do saque: "))
            saldo, extrato = sacar(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numero_de_saques = numero_de_saques,
                limite_saques = LIMITE_SAQUES,
            )

        elif escolha == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif escolha == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta,usuarios)

            if conta:
                contas.append(conta)
        elif escolha == "lc":
            listar_contas(contas)

        elif escolha == "nu":
            criar_usuario(usuarios)
        elif escolha == "q":
            break
        else:
            print("Operação invalida, por favor selecione novamente a operação desejada.")




if __name__ == '__main__':
    main()