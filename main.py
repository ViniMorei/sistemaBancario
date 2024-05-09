menu = """
Operações:
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    match(opcao.lower()):
        case "d":
            deposito = float(input("Digite o valor a ser depositado na conta: "))

            if deposito > 0:
                print("Operação realizada com sucesso.\n")
                saldo += deposito
                extrato += f'Depósito: R$ {deposito:.2f}\n'
            else:
                print("Valor inválido\n")

        case "s":
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

        case "e": #Extrato
            print("-----------------------------\n")
            print("Não foram realizadas movimentações." if not extrato else extrato)
            print(f'Saldo: {saldo:.2f}')
            print("-----------------------------\n")

        case "q": #Encerrar
            break

        case _: #Operação inválida
            print("Operação inválida, selecione alguma das opções disponíveis.\n")