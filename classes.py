from abc import ABC, abstractmethod, abstractproperty


class Cliente:
    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self._contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, dataNasc, endereco):
        super().__init__(endereco)
        self._nome = nome
        self._cpf = cpf
        self._dataNasc = dataNasc

    @property
    def cpf(self):
        return self._cpf

    @property
    def nome(self):
        return self._nome

    @property
    def contas(self):
        return self._contas

    def __str__(self):
        return f"""
            Cliente: {self._nome}
            CPF: {self._cpf}
            Data Nascimento: {self._dataNasc}
            Número de contas: {len(self._contas)}
            
            -------------------------------------------
        """

class Conta:
    def __init__(self, numero, cliente, agencia="0001", saldo = 0):
        self._saldo = saldo
        self._numero = numero
        self._agencia = agencia
        self._cliente = cliente
        self._historico = Historico()

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    def sacar(self, valor):
        saldo = self._saldo

        if valor > saldo:
            print("Saldo insuficiente")
        elif valor > 0:
            self._saldo -= valor
            print("Operação realizada com sucesso!")

            return True
        else:
            print("Operação falhou! Valor inválido")

        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("Operação realizada com sucesso!")

            return True
        else:
            print("Operação falhou! Valor inválido")

            return False


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes
             if transacao["Tipo"] == "Saque"]
        )

        excedeuLimite = valor > self._limite
        excedeuSaques = numero_saques >= self._limite_saques

        if excedeuLimite:
            print("Operação falhou! Valor inválido para saque")
        elif excedeuSaques:
            print("Operação falhou! Número máximo de saques excedido")
        else:
            return super().sacar(valor)

        return False

    def __str__(self):
        return f"""
            Agência: {self._agencia}
            Conta-corrente: {self._numero}
            Cliente: {self._cliente.nome}
            
            -------------------------------------------
        """


class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "Tipo": transacao.__class__.__name__,
                "Valor": transacao.valor,
            }
        )


class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        depositou = conta.depositar(self._valor)

        if depositou:
            conta.historico.adicionar_transacao(self)


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sacou = conta.sacar(self._valor)

        if sacou:
            conta.historico.adicionar_transacao(self)
