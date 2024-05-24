#Importando as classes declaradas no arquivo classes.py
from classes import *

#A barra "/" indica que todos os argumentos antes dela são posicionais
def depositar(saldo, extrato, /):
    deposito = float(input("Digite o valor a ser depositado na conta: "))

    if deposito > 0:
        print("Operação realizada com sucesso.\n")
        saldo += deposito
        extrato += f'Depósito: R$ {deposito:.2f}\n'

        return saldo, extrato
    else:
        print("Valor inválido\n")

#O asterisco "*" indica que todos os argumentos depois dele são chamados por nome
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
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nu] Novo Usuário
    [lu] Listar Usuários
    [nc] Nova Conta
    [lc] Listar Contas
    [q] Sair do Programa
    => """

    #Lista de usuários e contas, que serão preenchidas com objetos das classes PessoaFisica e ContaCorrente
    usuarios = []
    contas = []

    #Variáveis que precisam ser tiradas de circulação:
    limite = 500
    numero_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    numeroConta = 0

    while True:
        opcao = input(menu)

        match (opcao.lower()):
            # Depositar
            case "d":
                saldo, extrato = depositar(saldo, extrato)

            # Sacar
            case "s":
                saldo, extrato = sacar(saldo = saldo, extrato = extrato, limite = limite,
                                       numero_saques = numero_saques, LIMITE_SAQUES = LIMITE_SAQUES)

            # Extrato
            case "e":
                tirarExtrato(saldo, extrato = extrato)

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
                numeroConta += 1
                conta = criarConta(usuarios, numeroConta)

                if conta:
                    contas.append(conta)

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