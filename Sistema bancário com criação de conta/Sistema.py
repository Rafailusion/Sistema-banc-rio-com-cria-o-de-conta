class Usuario:
    def __init__(self, nome, cpf, endereco):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco

class Conta:
    def __init__(self, numero, usuario):
        self.numero = numero
        self.usuario = usuario
        self.saldo = 0.0
        self.extrato = []
        self.saques_realizados = 0
        self.limite_saque_diario = 3
        self.valor_limite_saque = 500.0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: R$ {valor:.2f}")
            print(f"Depósito realizado: R$ {valor:.2f}")
        else:
            print("Depósito não pode ser negativo!")

    def sacar(self, valor):
        if self.saques_realizados >= self.limite_saque_diario:
            print("Limite diário de saques atingido!")
        elif valor > self.valor_limite_saque:
            print(f"Saque não pode exceder R$ {self.valor_limite_saque:.2f} por operação!")
        elif valor > self.saldo:
            print("Saldo insuficiente!")
        else:
            self.saldo -= valor
            self.extrato.append(f"Saque: R$ {valor:.2f}")
            self.saques_realizados += 1
            print(f"Saque realizado: R$ {valor:.2f}")

    def mostrar_saldo(self):
        print(f"Saldo atual: R$ {self.saldo:.2f}")

    def mostrar_extrato(self):
        print("=== Extrato ===")
        if not self.extrato:
            print("Nenhuma movimentação realizada.")
        else:
            for movimento in self.extrato:
                print(movimento)
        print(f"Saldo atual: R$ {self.saldo:.2f}")
        print("================")

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
