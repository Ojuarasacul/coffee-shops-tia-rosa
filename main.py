# main.py
# Programa principal do sistema do Coffee Shops Tia Rosa
# Esse programa mostra um menu no terminal e chama as funcoes do funcoes.py

from funcoes import (
    criar_cardapio_inicial,
    adicionar_produto,
    remover_produto,
    listar_cardapio,
    buscar_produto,
    cadastrar_cliente,
    listar_clientes,
    buscar_cliente,
    criar_pedido,
    listar_pedidos,
    gerar_relatorio,
)


def mostrar_menu():
    print("\n===================================")
    print("   COFFEE SHOPS TIA ROSA - SISTEMA")
    print("===================================")
    print("1 - Ver cardapio")
    print("2 - Adicionar produto no cardapio")
    print("3 - Remover produto do cardapio")
    print("4 - Cadastrar cliente")
    print("5 - Ver clientes e pontos")
    print("6 - Fazer pedido")
    print("7 - Ver historico de pedidos")
    print("8 - Ver relatorio de vendas")
    print("0 - Sair")
    print("===================================")


def opcao_adicionar_produto(cardapio):
    print("\n--- ADICIONAR PRODUTO ---")
    nome = input("Nome do produto: ")
    preco = float(input("Preco do produto: "))
    descricao = input("Descricao (ingredientes): ")
    adicionar_produto(cardapio, nome, preco, descricao)


def opcao_remover_produto(cardapio):
    listar_cardapio(cardapio)
    codigo = int(input("\nDigite o codigo do produto que quer remover: "))
    remover_produto(cardapio, codigo)


def opcao_cadastrar_cliente(clientes):
    print("\n--- CADASTRAR CLIENTE ---")
    nome = input("Nome do cliente: ")
    telefone = input("Telefone: ")
    cadastrar_cliente(clientes, nome, telefone)


def opcao_fazer_pedido(cardapio, clientes, pedidos):
    if len(clientes) == 0:
        print("\nAinda nao tem cliente cadastrado. Cadastre um cliente primeiro.")
        return

    if len(cardapio) == 0:
        print("\nO cardapio esta vazio. Adicione produtos primeiro.")
        return

    listar_clientes(clientes)
    codigo_cliente = int(input("\nDigite o codigo do cliente: "))
    cliente = buscar_cliente(clientes, codigo_cliente)

    if cliente is None:
        print("\nCliente nao encontrado.")
        return

    listar_cardapio(cardapio)

    produtos_escolhidos = []
    continuar = "s"

    while continuar == "s":
        codigo_produto = int(input("\nDigite o codigo do produto: "))
        produto = buscar_produto(cardapio, codigo_produto)

        if produto is None:
            print("Produto nao encontrado, tenta de novo.")
        else:
            produtos_escolhidos.append(produto)
            print(f"'{produto.nome}' adicionado ao pedido.")

        continuar = input("Quer adicionar mais um produto? (s/n): ")

    if len(produtos_escolhidos) == 0:
        print("\nNenhum produto foi escolhido, pedido cancelado.")
        return

    criar_pedido(pedidos, cliente, produtos_escolhidos)


def main():
    # aqui ficam guardados os dados enquanto o programa esta rodando
    cardapio = criar_cardapio_inicial()
    clientes = []
    pedidos = []

    print("Bem vindo ao sistema da Coffee Shops Tia Rosa!")

    rodando = True
    while rodando:
        mostrar_menu()
        opcao = input("Escolha uma opcao: ")

        if opcao == "1":
            listar_cardapio(cardapio)

        elif opcao == "2":
            opcao_adicionar_produto(cardapio)

        elif opcao == "3":
            opcao_remover_produto(cardapio)

        elif opcao == "4":
            opcao_cadastrar_cliente(clientes)

        elif opcao == "5":
            listar_clientes(clientes)

        elif opcao == "6":
            opcao_fazer_pedido(cardapio, clientes, pedidos)

        elif opcao == "7":
            listar_pedidos(pedidos)

        elif opcao == "8":
            gerar_relatorio(pedidos)

        elif opcao == "0":
            print("\nSaindo do sistema... ate mais!")
            rodando = False

        else:
            print("\nOpcao invalida, tenta de novo.")


# isso faz o programa comecar quando a gente roda o arquivo
if __name__ == "__main__":
    main()
