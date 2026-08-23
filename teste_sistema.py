# teste_sistema.py
# Esse arquivo testa se o sistema esta funcionando direito
# ele roda varias operacoes e confere se o resultado é o esperado

from classes import Produto, Cliente, Pedido
from funcoes import (
    criar_cardapio_inicial,
    adicionar_produto,
    remover_produto,
    buscar_produto,
    cadastrar_cliente,
    buscar_cliente,
    criar_pedido,
    gerar_relatorio,
)

testes_ok = 0
testes_falhou = 0


def conferir(nome_teste, condicao):
    # essa funcao confere se a condicao é verdadeira e mostra o resultado
    global testes_ok, testes_falhou
    if condicao:
        print(f"OK   - {nome_teste}")
        testes_ok = testes_ok + 1
    else:
        print(f"ERRO - {nome_teste}")
        testes_falhou = testes_falhou + 1


print("==================================================")
print("TESTANDO O SISTEMA COFFEE SHOPS TIA ROSA")
print("==================================================\n")

# Teste 1 - cardapio inicial ja vem com produtos
cardapio = criar_cardapio_inicial()
conferir("cardapio inicial tem produtos", len(cardapio) == 5)

# Teste 2 - adicionar produto novo
adicionar_produto(cardapio, "Suco de Laranja", 6.00, "Suco natural")
conferir("produto novo foi adicionado", len(cardapio) == 6)

# Teste 3 - buscar produto que existe
produto_achado = buscar_produto(cardapio, 1)
conferir("busca de produto encontrou o certo", produto_achado.nome == "Cafe Expresso")

# Teste 4 - remover produto
remover_produto(cardapio, 6)
conferir("produto foi removido", len(cardapio) == 5)

# Teste 5 - cadastrar cliente
clientes = []
cliente1 = cadastrar_cliente(clientes, "Joao Silva", "11999990000")
conferir("cliente foi cadastrado", len(clientes) == 1)

# Teste 6 - cliente comeca com 0 pontos
conferir("cliente comeca com zero pontos", cliente1.pontos == 0)

# Teste 7 - buscar cliente
cliente_achado = buscar_cliente(clientes, 1)
conferir("busca de cliente encontrou o certo", cliente_achado.nome == "Joao Silva")

# Teste 8 - criar pedido e conferir o total
pedidos = []
produto_cafe = buscar_produto(cardapio, 1)   # Cafe Expresso R$ 5.00
produto_bolo = buscar_produto(cardapio, 5)   # Bolo de Chocolate R$ 7.50
pedido1 = criar_pedido(pedidos, cliente1, [produto_cafe, produto_bolo])
conferir("total do pedido esta certo", pedido1.total == 12.50)

# Teste 9 - pontos de fidelidade (1 ponto por real gasto)
conferir("cliente ganhou pontos certos", cliente1.pontos == 12)

# Teste 10 - historico de pedidos aumentou
conferir("pedido foi guardado no historico", len(pedidos) == 1)

# Teste 11 - fazer mais um pedido pra testar o relatorio
cliente2 = cadastrar_cliente(clientes, "Maria Souza", "11988887777")
produto_cappuccino = buscar_produto(cardapio, 3)  # R$ 8.00
pedido2 = criar_pedido(pedidos, cliente2, [produto_cappuccino])
conferir("segundo pedido foi criado", len(pedidos) == 2)

# Teste 12 - relatorio de vendas nao da erro
try:
    gerar_relatorio(pedidos)
    relatorio_funcionou = True
except Exception:
    relatorio_funcionou = False
conferir("relatorio de vendas rodou sem erro", relatorio_funcionou)


print("\n==================================================")
print("RESULTADO FINAL DOS TESTES")
print("==================================================")
print(f"Testes que passaram: {testes_ok}")
print(f"Testes que falharam: {testes_falhou}")

if testes_falhou == 0:
    print("\nTODOS OS TESTES PASSARAM! O sistema esta funcionando certinho.")
else:
    print("\nAlguns testes falharam, olha o que deu ERRO ali em cima.")
