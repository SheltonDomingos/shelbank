import contas
import pessoas


class banco:
    def __init__(
        self,
        agencias: list[int] | None = None,
        clientes: list[pessoas.pessoa] | None = None,
        contas: list[contas.Contas] | None= None,    
    ):
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []

    def _checa_agencia(self, conta):
        if conta.agencia in self.agencias:
            return True
        return False

    def _checa_cliente(self, cliente):
        if cliente in self.clientes:
            return True
        return False
    
    def _checa_conta(self, conta):
        if conta in self.contas:
            return True
        return False
   
    def _checa_se_conta_e_do_cliente(self, cliente, conta):
        if conta in self.contas:
            print('_checa_se_conta_e_do_cliente', True)
            return True
        print('_checa_se_conta_e_do_cliente', False)
        return False


    def autenticar(self, cliente: pessoas.pessoa, conta: contas.Contas):
        return self._checa_agencia(conta) and \
            self._checa_cliente(cliente) and \
            self._checa_conta(conta) and \
            self._checa_se_conta_e_do_cliente(cliente, conta)
   
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencias!r}, {self.clientes!r}, {self.contas!r})'
        return f'{class_name}{attrs}'


if __name__ == '__main__':
    cliente1 = pessoas.cliente('shelton', 25)
    ContaCorrente1 = contas.ContaCorrente(111, 222, 0, 0)
    cliente1.conta = ContaCorrente1
    Banco = banco()
    Banco.clientes.extend([cliente1])
    Banco.contas.extend([ContaCorrente1])
    Banco.agencias.extend([111, 222])
    
    if Banco.autenticar(cliente1, ContaCorrente1):
        ContaCorrente1.depositar(10)
        ContaCorrente1.depositar(10)
        print(cliente1.conta)
        
