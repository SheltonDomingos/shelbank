import contas

class pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome: str):
        self._nome = nome   


    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, idade: int):
        self._idade = idade  

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.nome!r}, {self.idade!r})'
        return f'{class_name}{attrs}'


class cliente(pessoa):
    def __init__(self, nome: str, idade: int) -> None:
        super().__init__(nome, idade)
        self.conta: contas.Contas | None = None

if __name__ == '__main__':
    cliente1 = cliente('shelton', 25)
    cliente1.conta = contas.ContaCorrente(111, 222, 0, 0)
    print(cliente1)
    print(cliente1.conta)
    
    print()#esses prints são apenas pra separar no terminal!
    print()#esses prints são apenas pra separar no terminal!
    
    cliente2 = cliente('gabriel', 18)
    cliente2.conta = contas.ContaPoupanca(321, 123, 100)
    print(cliente2)
    print(cliente2.conta)