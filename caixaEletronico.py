class Banco:
    # Definindo códigos ANSI para cores
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    WHITE = '\033[0m'
    YELLOW = '\033[93m' 

    def __init__(self):
        self.saldo = 0
        self.depositos = []
        self.saques = []

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            self.depositos.append(valor)
            print(f'Depósito: {self.GREEN}R$ {valor:.2f}{self.WHITE} realizado com sucesso.')
        else:
            print('Valor de depósito inválido. Deve ser positivo.')

    def saque(self, valor):
        if valor > 0 and valor <= 500:
            if self.saldo >= valor:
                if len(self.saques) < 3:
                    self.saldo -= valor
                    self.saques.append(valor)
                    print(f'Saque: {self.RED}R$ {valor:.2f}{self.WHITE} realizado com sucesso.')
                else:
                    print('Limite máximo de 3 saques diários atingido.')
            else:
                print(f"""{self.RED}Saldo insuficiente para realizar o saque.
{self.WHITE}Seu saldo atual é de: {self.YELLOW}R$ {self.saldo:.2f}{self.WHITE}.
                """)
        else:
            print('Valor de saque inválido. Deve ser positivo e no máximo R$ 500.00.')

    def extrato(self):
        print(f'{self.BLUE}Extrato:{self.WHITE}')
        for deposito in self.depositos:
            print(f'{self.GREEN}Depósito: R$ {deposito:.2f}{self.WHITE}')
        for saque in self.saques:
            print(f'{self.RED}Saque: R$ {saque:.2f}{self.WHITE}')
        print(f'{self.YELLOW}Saldo Atual: R$ {self.saldo:.2f}{self.WHITE}')

# Exemplo de uso do sistema
banco = Banco()
print()
banco.extrato()
print()
banco.deposito(1000.00)
print()
banco.extrato()
print()
banco.saque(300.00)
print()
banco.extrato()
print()
banco.saque(200.00)
print()
banco.extrato()
print()
banco.saque(500.00)
print()
banco.extrato()
print()
banco.saque(500.00)
print()