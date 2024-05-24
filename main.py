#Importando as classes declaradas no arquivo classes.py
from classes import *

def depositar(usuarios):
    # Verifica se o cliente existe
    cadastrado = False
    cpf = input('Digite o CPF do cliente que quer depositar: ')
    for usuario in usuarios:
        if usuario.cpf == cpf:
            cliente = usuario
            cadastrado = True


    if cadastrado:
        # Caso o cliente esteja cadastrado, verifica se ele possui contas abertas
        contas = cliente.contas
        if len(contas) > 0:
            existe = False
            cc = int(input(f"Informe o número da conta do(a) cliente {cliente.nome} que irá receber o depósito: "))
            for conta in contas:
                # Verifica se a conta informada está vinculada ao cliente
                if conta.numero == cc:
                    valor = float(input(f"Informe o valor a ser depositado na conta nº {conta.numero}: R$ "))
                    deposito = Deposito(valor)
                    cliente.realizar_transacao(conta, deposito)
                    return
            # Mensagem de erro caso a conta não seja encontrada
            if not existe:
                print(f"O(A) cliente {cliente.nome} não possui uma conta com o número {cc}, favor tentar novamente.")
        # Mensagem de erro caso o cliente não tenha contas abertas
        else:
            print(f"O(A) cliente {cliente.nome} não possui contas abertas! Favor criar uma e tentar novamente.")
    # Mensagem de erro caso o cliente não esteja cadastrado
    else:
        print("Usuário não encontrado! Favor cadastrar o cliente")


def sacar(usuarios):
    # Verifica se o cliente existe
    cadastrado = False
    cpf = input('Digite o CPF do cliente que quer sacar: ')
    for usuario in usuarios:
        if usuario.cpf == cpf:
            cliente = usuario
            cadastrado = True

    # Caso o cliente exista, verifica se ele possui contas abertas
    if cadastrado:
        contas = cliente.contas
        if len(contas) > 0:
            existe = False
            cc = int(input(f"Informe o número da conta do(a) cliente {cliente.nome} que irá ser sacada: "))
            for conta in contas:
                # Verifica se a conta está vinculada ao cliente
                if conta.numero == cc:
                    # Solicita o valor e tenta realizar o saque
                    valor = float(input(f"Informe o valor a ser sacado da conta nº {conta.numero}: R$ "))
                    saque = Saque(valor)
                    cliente.realizar_transacao(conta, saque)
                    return
                # Mensagem de erro caso a conta não seja encontrada
            if not existe:
                print(f"O(A) cliente {cliente.nome} não possui uma conta com o número {cc}, favor tentar novamente.")
        # Mensagem de erro caso o cliente não possua contas abertas
        else:
            print(f"O(A) cliente {cliente.nome} não possui contas abertas! Favor criar uma e tentar novamente.")
    # Mensagem de erro caso o cliente não esteja cadastrado
    else:
        print("Usuário não encontrado! Favor cadastrar o cliente")

def tirarExtrato(usuarios):
    # Verifica se o cliente existe
    cadastrado = False
    cpf = input('Digite o CPF do cliente que quer verificar o extrato: ')
    for usuario in usuarios:
        if usuario.cpf == cpf:
            cliente = usuario
            cadastrado = True

    # Verifica se o cliente está cadastrado e tem contas abertas
    if cadastrado:
        contas = cliente.contas
        if len(contas) > 0:
            existe = False
            cc = int(input(f"Informe o número da conta do(a) cliente {cliente.nome} cujo extrato será verificado: "))
            for conta in contas:
                if conta.numero == cc:
                    transacoes = conta.historico.transacoes
                    for transacao in transacoes:
                        print(f"""
                            {transacao["Tipo"]}: R$ {transacao["Valor"]:.2f}
                        """)
                    print(f"""
                            Saldo: R$ {conta.saldo:.2f}
                    """)
                    return
            #Mensagem de erro caso a conta informada não esteja vinculada ao cliente
            if not existe:
                print(f"O(A) cliente {cliente.nome} não possui uma conta com o número {cc}, favor tentar novamente.")
        # Mensagem de erro caso o cliente não tenha contas abertas
        else:
            print(f"O(A) cliente {cliente.nome} não possui contas abertas! Favor criar uma e tentar novamente.")
    # Mensagem de erro caso o cliente não esteja cadastrado
    else:
        print("Usuário não encontrado! Favor cadastrar o cliente")

    """
    print("-----------------------------\n")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f'Saldo: {saldo:.2f}')
    print("-----------------------------\n")
    """

def criarUsuario(usuarios):
    cadastrado = False
    cpf = input("Informe o CPF a ser cadastrado: ")
    # Verifica se o CPF informado já está associado a um cliente
    for usuario in usuarios:
        if usuario.cpf == cpf:
            print("O CPF informado já foi cadastrado!")
            cadastrado = True

    # Caso o CPF não pertença a nenhum cliente, cria um objeto da classe PessoaFisica
    # e retorna o objeto, que será adicionado a lista de usuários
    if not cadastrado:
        nome = input("Informe o nome completo do usuário: ")
        nascimento = input("Informe a data de nascimento (dd-mm-aa): ")
        endereco = input("Informe o endereço do usuário (Logradouro, Número - Bairro - Cidade/Sigla do Estado): ")

        print("Usuário criado com sucesso!")
        return PessoaFisica(cpf, nome, nascimento, endereco)

def listarUsuarios(usuarios):
    # Percorre a lista de usuários cadastrados
    # e executa a função __str__ delas
    for usuario in usuarios:
        print(usuario)

def criarConta(usuarios, numeroConta):
    cadastrado = False
    cpf = input("Informe o CPF do cliente a criar uma conta: ")
    # Verifica se o usuário existe dentro da lista de usuários cadastrados
    for usuario in usuarios:
        if usuario.cpf == cpf:
            # Caso o usuário esteja cadastrado, cria uma variável
            # para armazenar o objeto que irá receber uma conta nova,
            # e atualiza o valor da variável de controle
            cliente = usuario
            cadastrado = True

    # Verifica se o usuário está cadastrado,
    # Pois não existe conta sem usuário
    if cadastrado:
        # Cria uma variável para armazenar um objeto Conta utilizando
        # o número de conta auto-iterável e o cliente resgatado anteriormente
        contaNova = ContaCorrente(numeroConta, cliente)
        cliente.adicionar_conta(contaNova)

        print("Operação realizada com sucesso!")
        return contaNova.__str__()
    else:
        print("Usuário não encontrado! Favor cadastrar o cliente.")

def listarContas(contas):
    for conta in contas:
        # Aqui a função irá acessar os objetos dentro da lista
        # "contas" e irá printar a função __str__ delas
        print(conta)

def main():
    menu = """
    Operações:
    [d] Depositar               [nu] Novo usuário
    [s] Sacar                   [nc] Nova conta
    [e] Extrato                 [lu] Listar usuários
    [q] Sair do Programa        [lc] Listar contas
    => """

    #Lista de usuários e contas, que serão preenchidas com objetos das classes PessoaFisica e ContaCorrente
    usuarios = []
    contas = []
    numeroConta = 1

    # Execução do programa
    while True:
        opcao = input(menu)

        match (opcao.lower()):
            # Depositar
            case "d":
               depositar(usuarios)

            # Sacar
            case "s":
                sacar(usuarios)

            # Extrato
            case "e":
                tirarExtrato(usuarios)

            # Novo usuário
            case "nu":
                usuario = criarUsuario(usuarios)
                if usuario:
                    usuarios.append(usuario)

            # Listar usuários
            case "lu":
                listarUsuarios(usuarios)

            # Nova conta
            case "nc":
                conta = criarConta(usuarios, numeroConta)

                if conta:
                    contas.append(conta)
                    numeroConta += 1

            # Listar contas
            case "lc":
                listarContas(contas)

            # Encerrar
            case "q":
                break

            # Operação inválida
            case _:
                print("Operação inválida, selecione alguma das opções disponíveis.\n")


#Início do programa
main()