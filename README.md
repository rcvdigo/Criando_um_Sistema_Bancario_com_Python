# Desafio!!!

- Iniciar a modelagem do sistema bancário em POO. Adicionar classes para cliente e as operações bancárias: Deposito e saque.
- Atualizar a implementação do sistema bancário, para armazenar os dados de clientes e contas bancárias em objetos ao invés de dicionários. O código deve seguir o modelo de classes UML a seguir.

```mermaid
classDiagram

Historico --* Conta : -historico 1
Conta <|-- ContaCorrente
Historico o-- "*" Transacao : -transacoes
Deposito --|> Transacao
Saque --|> Transacao
Transacao "*" -- Cliente : realiza
Conta "* -contas" *-- "1 -cliente" Cliente
Cliente <|-- PessoaFisica

class Historico {
  + adicionar_transacao(transacao: Transacao)
}

class Conta {
  - saldo: float
  - numero: int
  - agencia: str
  - cliente: Cliente
  - historico: Historico
  + saldo(): float
  + nova_conta(cliente: Cliente, numero: int): Conta
  + sacar(valor: float): bool
  + depositar(valor: float): bool
}

class ContaCorrente {
  - limite: float
  - limite_saques: int
}

class Transacao {
  <<interface>>
  + registrar(conta: Conta)
}

class Deposito {
  - valor: float
}

class Saque {
  - valor: float
}

class Cliente {
  - endereco: str
  - contas: list
  + realizar_transacao(conta: Conta, transacao: Transacao)
  + adicionar_conta(conta: Conta)
}

class PessoaFisica {
  - cpf: str
  - nome: str
  - data_nascimento: date
}
```