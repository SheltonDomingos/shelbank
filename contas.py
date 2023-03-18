import abc

class Contas(abc.ABC):
    def __init__(self, agencia: int, conta: int, saldo: float = 0) -> None:
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
    
    @abc.abstractmethod
    def sacar(self, valor: float) -> float: ...
    
    
    def depositar(self, valor: float) -> float:
        self.detalhes(f'(Depósito de R$ {valor})')
        self.saldo += valor
        return self.saldo

    def detalhes(self, msg=''):
        print(f'O seu saldo é R$ {self.saldo:.2f} {msg}')

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r})'
        return f'{class_name}{attrs}'

class ContaPoupanca(Contas):
    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor

        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhes(f'(Saque valor de: R$ {valor}) realizado com sucesso!')
            return self.saldo
        
        print('Não foi possível sacar o valor desejado!')
        self.detalhes(f'(Saque no valor de: R$ {valor}) Negado!')


class ContaCorrente(Contas):
    def __init__(self, agencia: int, conta: int, saldo: float = 0, limite: float =0):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor
        limite_maximo = -self.limite

        if valor_pos_saque >= limite_maximo:
            self.detalhes(f'(Saque valor de: R$ {valor}) realizado com sucesso!')
            self.saldo -= valor
            return self.saldo
        
        print('Não foi possível sacar o valor desejado!')
        print(f'Seu limite extra é: R$ {-self.limite:.2f}')
        self.detalhes(f'(Saque no valor de: R$ {valor}) Negado!')
        return self.saldo
    
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r}, '\
            f'{self.limite!r})'
        return f'{class_name}{attrs}'


if __name__ == '__main__':
    conta_ContaCorrente = ContaCorrente(111, 222, 0, 100)
    conta_ContaCorrente.depositar(2)
    conta_ContaCorrente.sacar(1)
    conta_ContaCorrente.sacar(1)
    conta_ContaCorrente.sacar(98)
    conta_ContaCorrente.sacar(2)
    conta_ContaCorrente.sacar(1)
    print()#esses prints são apenas pra separar no terminal!
    print()#esses prints são apenas pra separar no terminal!
    conta_ContaPoupança = ContaPoupanca(111, 222, 0,)
    conta_ContaPoupança.depositar(2)
    conta_ContaPoupança.sacar(1)
    conta_ContaPoupança.sacar(1)
    conta_ContaPoupança.sacar(98)
    
    