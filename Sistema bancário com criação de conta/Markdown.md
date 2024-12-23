# Sistema Bancário em Python

Este projeto implementa um sistema bancário simples em Python com as seguintes funcionalidades:

## Funcionalidades

### 1. **Cadastrar Usuário**
Permite cadastrar um novo usuário com as seguintes informações:
- Nome
- CPF
- Endereço

### 2. **Criar Conta**
Permite criar uma conta associada a um usuário existente (identificado pelo CPF).

### 3. **Operações Bancárias**
As contas possuem as funcionalidades:
- **Depositar:** Permite realizar depósitos na conta.
- **Sacar:** Permite realizar saques respeitando os limites diários e por operação.
- **Mostrar Saldo:** Exibe o saldo atual da conta.
- **Mostrar Extrato:** Exibe todas as movimentações financeiras da conta.

## Estrutura do Código

### **Classe `Usuario`**
Representa os dados de um usuário.
```python
class Usuario:
    def __init__(self, nome, cpf, endereco):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
```

### **Classe `Conta`**
Gerencia as operações bancárias de cada conta.
```python
class Conta:
    def __init__(self, numero, usuario):
        self.numero = numero
        self.usuario = usuario
        self.saldo = 0.0
        self.extrato = []
        self.saques_realizados = 0
        self.limite_saque_diario = 3
        self.valor_limite_saque = 500.0
```

#### Métodos da Classe `Conta`
- **`depositar(valor)`**: Realiza um depósito na conta.
- **`sacar(valor)`**: Realiza um saque considerando os limites estabelecidos.
- **`mostrar_saldo()`**: Exibe o saldo atual da conta.
- **`mostrar_extrato()`**: Mostra o histórico de transações da conta.

### **Menu Interativo**

O menu interativo permite ao usuário navegar pelas funcionalidades:
```python
def menu():
    usuarios = []
    contas = []
    numero_conta = 1

    while True:
        print("\n=== Sistema Bancário ===")
        print("1. Cadastrar Usuário")
        print("2. Criar Conta")
        print("3. Depositar")
        print("4. Sacar")
        print("5. Mostrar Saldo")
        print("6. Mostrar Extrato")
        print("7. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Informe o nome: ")
            cpf = input("Informe o CPF: ")
            endereco = input("Informe o endereço: ")
            usuarios.append(Usuario(nome, cpf, endereco))
            print("Usuário cadastrado com sucesso!")

        elif opcao == "2":
            cpf = input("Informe o CPF do usuário: ")
            usuario = next((u for u in usuarios if u.cpf == cpf), None)
            if usuario:
                contas.append(Conta(numero_conta, usuario))
                print(f"Conta criada com sucesso! Número da conta: {numero_conta}")
                numero_conta += 1
            else:
                print("Usuário não encontrado! Cadastre o usuário antes de criar uma conta.")

        elif opcao == "3":
            numero = int(input("Informe o número da conta: "))
            conta = next((c for c in contas if c.numero == numero), None)
            if conta:
                valor = float(input("Informe o valor do depósito: R$ "))
                conta.depositar(valor)
            else:
                print("Conta não encontrada!")

        elif opcao == "4":
            numero = int(input("Informe o número da conta: "))
            conta = next((c for c in contas if c.numero == numero), None)
            if conta:
                valor = float(input("Informe o valor do saque: R$ "))
                conta.sacar(valor)
            else:
                print("Conta não encontrada!")

        elif opcao == "5":
            numero = int(input("Informe o número da conta: "))
            conta = next((c for c in contas if c.numero == numero), None)
            if conta:
                conta.mostrar_saldo()
            else:
                print("Conta não encontrada!")

        elif opcao == "6":
            numero = int(input("Informe o número da conta: "))
            conta = next((c for c in contas if c.numero == numero), None)
            if conta:
                conta.mostrar_extrato()
            else:
                print("Conta não encontrada!")

        elif opcao == "7":
            print("Saindo do sistema. Obrigado!")
            break

        else:
            print("Opção inválida! Tente novamente.")

menu()
```

## Como Executar

1. Certifique-se de que você tenha o Python instalado em sua máquina.
2. Salve o código em um arquivo `.py`.
3. Execute o script no terminal ou em um ambiente Python:
   ```
   python nome_do_arquivo.py
   ```

## Melhorias Futuras
- Implementar autenticação de usuários.
- Permitir transferência entre contas.
- Criar uma interface gráfica para o sistema.
