import textwrap


class Banco:
    # Definindo códigos ANSI para cores
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    WHITE = '\033[0m'
    YELLOW = '\033[93m'
    MAGENTA = '\033[95m'
    CIANO = '\033[30m'

    def __init__(self):
        self.saldo = 0
        self.depositos = []
        self.AGENCIA = "0001"
        self.saques = []
        self.usuarios = []
        self.flag = True
        self.LIMITE_SAQUE = 500
        self.quantidade_saques = 3
        self.numero_saques = 0
        self.contas = []

    def menu(self):
        menu = f"""\n
        ================ MENU ================
        {self.GREEN}[d]\tDepositar{self.WHITE}
        {self.RED}[s]\tSacar{self.WHITE}
        {self.WHITE}[e]\tExtrato{self.WHITE}
        {self.YELLOW}[nc]\tNova conta{self.WHITE}
        {self.BLUE}[lc]\tListar contas{self.WHITE}
        {self.MAGENTA}[nu]\tNovo usuário{self.WHITE}
        {self.CIANO}[q]\tSair
        =>{self.WHITE} """
        return print(textwrap.dedent(menu))

    def deposito(self, valor, /):
        if valor > 0:
            self.saldo += valor
            self.depositos.append(valor)
            print(f'\nDepósito: {self.GREEN}R$ {valor:.2f}{self.WHITE} realizado com sucesso.')
        else:
            print('Valor de depósito inválido. Deve ser positivo.')

    def saque(self, *, saldo, valor, limite, numero_saques, limite_saques):
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques > limite_saques

        if(excedeu_saldo):
            print(f"\n\033[91m @@@ Operação falhou! Você não tem saldo suficiente. @@@ \033[0m")

        elif(excedeu_limite):
            print(f"\n\033[91m @@@ Operação falhou! O valor do saque excede o limite. @@@ \033[0m")

        elif(excedeu_saques):
            print(f"\n\033[91m @@@ Operação falhou! Número máximo de saques excedido. @@@ \033[0m")

        if valor > 0 and valor <= 500:
            if self.saldo >= valor:
                if self.numero_saques < 3:
                    print(f'\nSaque: {self.RED}R$ {valor:.2f}{self.WHITE} realizado com sucesso.')
                    self.saldo -= valor
                    self.saques.append(valor)
                    self.numero_saques += 1
                else:
                    print('\n\033[91m @@@ Limite máximo de 3 saques diários atingido. @@@\033[0m')
            else:
                print(f"""      {self.WHITE}Seu saldo atual é de: {self.YELLOW}R$ {self.saldo:.2f}{self.WHITE}.
                """)
        else:
            print(f'\n{self.RED}Valor de saque inválido{self.WHITE}. O valor deve ser {self.GREEN}POSITIVO{self.WHITE} e no máximo {self.YELLOW}R$ 500.00{self.WHITE}.')

    def extrato(self):
        print(f'{self.BLUE}\nExtrato:{self.WHITE}')
        for deposito in self.depositos:
            print(f'{self.GREEN}Depósito: R$ {deposito:.2f}{self.WHITE}')
        for saque in self.saques:
            print(f'{self.RED}Saque: R$ {saque:.2f}{self.WHITE}')
        print(f'{self.YELLOW}Saldo Atual: R$ {self.saldo:.2f}{self.WHITE}')

    def filtrar_usuario(self, cpf, usuarios):
        usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
        return usuarios_filtrados[0] if usuarios_filtrados else None

    def criar_usuario(self, usuarios):
        cpf = input("Informe o CPF (somente número): ")
        usuario = self.filtrar_usuario(cpf, self.usuarios)

        if(usuario):
            print(f"\n\033[91m @@@ Já existe usuário com esse CPF! @@@ \033[0m")
            return
        
        nome = input("Informe o nome completo: ")
        data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
        endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

        usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

        print("=== Usuário criado com sucesso! ===")

    def criar_conta(self, agencia, numero_conta, usuarios):
        cpf = input("Informe o CPF do usuário: ")
        usuario = self.filtrar_usuario(cpf, usuarios)

        if(usuario):
            print("\n=== Conta criada com sucesso! ===")
            return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
        
        print(f"\n\033[91m @@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@ \033[0m")

    def listar_contas(self, contas):
        for conta in contas:
            linha = f"""
                Agência:\t{conta['agencia']}
                C/C?\t\t{conta['numero_conta']}
                Titular:\t{conta['usuario']['nome']}
            """
            print("="*100)
            print(textwrap.dedent(linha))

def start_banco(obj_banco):
    while obj_banco.flag == True:
        obj_banco.menu() # Mostrando o menu inicial
        escolha = str(input("\nEscolha uma opção: ").lower())
        
        if(escolha == 'q'): # Condição que faz a saída do looping infinito caso a escolha seja igual a q
                obj_banco.flag = False
        elif(escolha == 'd'):
            try:
                obj_banco.deposito(float(input("\nEscolha um valor a ser depositado: ")))
            except ValueError:
                print(f"\n\033[91m @@@ Operação falhou! O valor informado é inválido @@@ \033[0m")
        elif(escolha == 's'):
            obj_banco.saque(
                saldo=obj_banco.saldo, 
                valor=(float(input("\nEscolha um valor a ser sacado: "))),
                limite=obj_banco.LIMITE_SAQUE,
                numero_saques=obj_banco.numero_saques,
                limite_saques=obj_banco.quantidade_saques
            )
        elif(escolha == 'e'):
            obj_banco.extrato()
        elif(escolha == 'nu'):
            obj_banco.criar_usuario(obj_banco.usuarios)
        elif(escolha == 'nc'):
            numero_conta = len(obj_banco.contas) + 1
            conta = obj_banco.criar_conta(obj_banco.AGENCIA, numero_conta, obj_banco.usuarios)

            if (conta):
                obj_banco.contas.append(conta)
        elif(escolha == 'lc'):
            obj_banco.listar_contas(obj_banco.contas)

# Exemplo de uso do sistema
obj_caixa_eletronico = Banco()
start_banco(obj_caixa_eletronico)