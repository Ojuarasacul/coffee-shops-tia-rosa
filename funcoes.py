# funcoes.py
# Aqui ficam as funcoes que fazem o sistema funcionar
# cada funcao cuida de uma parte: cardapio, clientes, pedidos e relatorio

from classes import Produto, Cliente, Pedido


# ---------- FUNCOES DO CARDAPIO ----------

def criar_cardapio_inicial():
    # cria alguns produtos ja cadastrados so pra o sistema nao comecar vazio
    lista = []
    lista.append(Produto(1, "Cafe Expresso", 5.00, "Cafe forte tirado na hora"))
    lista.append(Produto(2, "Cafe com Leite", 6.50, "Cafe com leite quente"))
    lista.append(Produto(3, "Cappuccino", 8.00, "Cafe com espuma de leite e canela"))
    lista.append(Produto(4, "Pao de Queijo", 4.00, "Pao de queijo mineiro quentinho"))
    lista.append(Produto(5, "Bolo de Chocolate", 7.50, "Fatia de bolo de chocolate"))
    return lista


def proximo_codigo_produto(cardapio):
    # descobre qual vai ser o codigo do proximo produto
    if len(cardapio) == 0:
        return 1
    ultimo = cardapio[-1]
    return ultimo.codigo + 1


def adicionar_produto(cardapio, nome, preco, descricao):
    codigo = proximo_codigo_produto(cardapio)
    novo_produto = Produto(codigo, nome, preco, descricao)
    cardapio.append(novo_produto)
    print(f"\nProduto '{nome}' adicionado com sucesso! Codigo: {codigo}")


def remover_produto(cardapio, codigo):
    for produto in cardapio:
        if produto.codigo == codigo:
            cardapio.remove(produto)
            print(f"\nProduto '{produto.nome}' removido do cardapio.")
            return True
    print("\nNao achei nenhum produto com esse codigo.")
    return False


def listar_cardapio(cardapio):
    print("\n--- CARDAPIO ---")
    if len(cardapio) == 0:
        print("O cardapio esta vazio.")
        return
    for produto in cardapio:
        produto.mostrar()


def buscar_produto(cardapio, codigo):
    for produto in cardapio:
        if produto.codigo == codigo:
            return produto
    return None


# ---------- FUNCOES DE CLIENTES ----------

def proximo_codigo_cliente(clientes):
    if len(clientes) == 0:
        return 1
    ultimo = clientes[-1]
    return ultimo.codigo + 1


def cadastrar_cliente(clientes, nome, telefone):
    codigo = proximo_codigo_cliente(clientes)
    novo_cliente = Cliente(codigo, nome, telefone)
    clientes.append(novo_cliente)
    print(f"\nCliente '{nome}' cadastrado com sucesso! Codigo: {codigo}")
    return novo_cliente


def listar_clientes(clientes):
    print("\n--- CLIENTES CADASTRADOS ---")
    if len(clientes) == 0:
        print("Nenhum cliente cadastrado ainda.")
        return
    for cliente in clientes:
        cliente.mostrar()


def buscar_cliente(clientes, codigo):
    for cliente in clientes:
        if cliente.codigo == codigo:
            return cliente
    return None


# ---------- FUNCOES DE PEDIDOS ----------

def proximo_numero_pedido(pedidos):
    if len(pedidos) == 0:
        return 1
    ultimo = pedidos[-1]
    return ultimo.numero + 1


def criar_pedido(pedidos, cliente, lista_de_produtos):
    numero = proximo_numero_pedido(pedidos)
    pedido = Pedido(numero, cliente)

    for produto in lista_de_produtos:
        pedido.adicionar_item(produto)

    pedidos.append(pedido)

    # a cada real gasto o cliente ganha 1 ponto de fidelidade
    pontos_ganhos = int(pedido.total)
    cliente.ganhar_pontos(pontos_ganhos)

    print(f"\nPedido numero {numero} registrado com sucesso!")
    print(f"Total do pedido: R$ {pedido.total:.2f}")
    print(f"{cliente.nome} ganhou {pontos_ganhos} pontos de fidelidade!")

    return pedido


def listar_pedidos(pedidos):
    print("\n--- HISTORICO DE PEDIDOS ---")
    if len(pedidos) == 0:
        print("Ainda nao tem nenhum pedido registrado.")
        return
    for pedido in pedidos:
        pedido.mostrar()
        print("")


# ---------- RELATORIO DE VENDAS ----------

def gerar_relatorio(pedidos):
    print("\n--- RELATORIO DE VENDAS ---")

    if len(pedidos) == 0:
        print("Nao tem vendas registradas ainda.")
        return

    total_vendido = 0
    for pedido in pedidos:
        total_vendido = total_vendido + pedido.total

    quantidade_pedidos = len(pedidos)
    ticket_medio = total_vendido / quantidade_pedidos

    print(f"Quantidade de pedidos: {quantidade_pedidos}")
    print(f"Total vendido: R$ {total_vendido:.2f}")
    print(f"Ticket medio: R$ {ticket_medio:.2f}")
