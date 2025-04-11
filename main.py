from models import Cliente, Servico

clientes = []
servicos = []

def menu():
    print("\n--- Sistema de Salão de Beleza ---")
    print("1. Cadastrar cliente")
    print("2. Cadastrar serviço")
    print("3. Listar clientes")
    print("4. Listar serviços")
    print("5. Sair")
    return input("Escolha uma opção: ")

def cadastrar_cliente():
    nome = input("Nome do cliente: ")
    telefone = input("Telefone: ")
    cliente = Cliente(nome, telefone)
    clientes.append(cliente)
    print("Cliente cadastrado com sucesso!")

def cadastrar_servico():
    nome = input("Nome do serviço: ")
    preco = float(input("Preço (R$): "))
    servico = Servico(nome, preco)
    servicos.append(servico)
    print("Serviço cadastrado com sucesso!")

def listar_clientes():
    print("\n--- Lista de Clientes ---")
    for c in clientes:
        print(c)

def listar_servicos():
    print("\n--- Lista de Serviços ---")
    for s in servicos:
        print(s)

while True:
    opcao = menu()
    if opcao == "1":
        cadastrar_cliente()
    elif opcao == "2":
        cadastrar_servico()
    elif opcao == "3":
        listar_clientes()
    elif opcao == "4":
        listar_servicos()
    elif opcao == "5":
        print("Encerrando sistema.")
        break
    else:
        print("Opção inválida.")
