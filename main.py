def depositar(saldo, extrato, /):
    deposito = float(input("Digite o valor a ser depositado na conta: "))

    if deposito > 0:
        print("Operação realizada com sucesso.\n")
        saldo += deposito
        extrato += f'Depósito: R$ {deposito:.2f}\n'

        return saldo, extrato
    else:
        print("Valor inválido\n")

def sacar(*, saldo, extrato, limite, numero_saques, LIMITE_SAQUES):
    if numero_saques >= LIMITE_SAQUES:
        print("Quantidade diária de saques excedida!")
    else:
        saque = float(input(f'Saldo disponível: R$ {saldo:.2f}\nInforme o valor a ser sacado: '))

        if saque > saldo:
            print("Saldo insuficiente!\n")
        elif saque > limite:
            print("Valor excede o limite do saque!\n")
        else:
            print("Operação realizada com sucesso.\n")
            saldo -= saque
            numero_saques += 1
            extrato += f'Saldo: R$ {saldo:.2f}\n'

            return saldo, extrato

def tirarExtrato(saldo, /, *, extrato):
    print("-----------------------------\n")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f'Saldo: {saldo:.2f}')
    print("-----------------------------\n")

def criarUsuario(usuarios):
    cadastrado = False
    cpf = input("Informe o CPF a ser cadastrado: ")
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            print("O CPF informado já foi cadastrado!")
            cadastrado = True
    if not cadastrado:
        nome = input("Informe o nome completo do usuário: ")
        nascimento = input("Informe a data de nascimento (dd-mm-aa): ")
        endereco = input("Informe o endereço do usuário (Logradouro, Número - Bairro - Cidade/Sigla do Estado: ")

        print("Operação realizada com sucesso!\n")
        return {"cpf": cpf, "nome": nome, "nascimento": nascimento, "endereco": endereco}

def criarConta(usuarios, AGENCIA, numeroConta):
    cadastrado = False
    cpf = input("Informe o CPF do cliente a criar uma conta: ")
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            cadastrado = True

    if cadastrado:
        print("Operação realizada com sucesso!\n")
        return {"usuario" : cpf, "agencia" : AGENCIA, "numeroConta" : numeroConta}
    else:
        print("Usuário não encontrado! Favor cadastrar o cliente.\n")

def listarContas(contas):
    for conta in contas:
        linha = f"""
            Conta: {conta["numeroConta"]}
            Usuário: {conta["usuario"]}
            Agência: {conta["agencia"]}
            
        """
        print(linha)

def main():
    menu = """
    Operações:
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nu] Novo Usuário
    [nc] Nova Conta
    [lc] Listar Contas
    [q] Sair do Programa
    => """

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    usuarios = []
    contas = []
    numeroConta = 0
    while True:
        opcao = input(menu)

        match (opcao.lower()):
            case "d":  # Depositar
                saldo, extrato = depositar(saldo, extrato)
            case "s":  # Sacar
                saldo, extrato = sacar(saldo = saldo, extrato = extrato, limite = limite,
                                       numero_saques = numero_saques, LIMITE_SAQUES = LIMITE_SAQUES)
            case "e":  # Extrato
                tirarExtrato(saldo, extrato = extrato)
            case "nu": #Novo usuário
                usuario = criarUsuario(usuarios)
                if usuario:
                    usuarios.append(usuario)
            case "nc": #Nova conta
                numeroConta += 1
                conta = criarConta(usuarios, AGENCIA, numeroConta)
                if conta:
                    contas.append(conta)
            case "lc": #Listar contas
                listarContas(contas)
            case "q":  # Encerrar
                break

            case _:  # Operação inválida
                print("Operação inválida, selecione alguma das opções disponíveis.\n")


#Início do programa
main()