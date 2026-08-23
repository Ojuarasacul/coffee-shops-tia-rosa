# classes.py
# Aqui ficam as 3 classes do sistema: Produto, Cliente e Pedido
# Cada classe representa uma "coisa" do nosso sistema da cafeteria


class Produto:
    # Um produto é um item do cardapio, tipo um cafe ou um bolo

    def __init__(self, codigo, nome, preco, descricao):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco
        self.descricao = descricao

    def mostrar(self):
        # mostra os dados do produto de um jeito facil de ler
        print(f"[{self.codigo}] {self.nome} - R$ {self.preco:.2f}")
        print(f"    {self.descricao}")


class Cliente:
    # Um cliente eh a pessoa que compra na cafeteria
    # ele tem pontos de fidelidade que vao aumentando com as compras

    def __init__(self, codigo, nome, telefone):
        self.codigo = codigo
        self.nome = nome
        self.telefone = telefone
        self.pontos = 0

    def ganhar_pontos(self, quantidade):
        # a cada real gasto o cliente ganha 1 ponto
        self.pontos = self.pontos + quantidade

    def mostrar(self):
        print(f"[{self.codigo}] {self.nome} - Tel: {self.telefone} - Pontos: {self.pontos}")


class Pedido:
    # Um pedido eh a compra que o cliente faz
    # ele guarda quais produtos foram pedidos e o total

    def __init__(self, numero, cliente):
        self.numero = numero
        self.cliente = cliente
        self.itens = []  # lista com os produtos do pedido
        self.total = 0

    def adicionar_item(self, produto):
        self.itens.append(produto)
        self.total = self.total + produto.preco

    def mostrar(self):
        print(f"Pedido numero {self.numero} - Cliente: {self.cliente.nome}")
        for item in self.itens:
            print(f"    - {item.nome} (R$ {item.preco:.2f})")
        print(f"    Total: R$ {self.total:.2f}")
