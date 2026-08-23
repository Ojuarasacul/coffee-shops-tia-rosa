# Sistema Coffee Shops Tia Rosa

Esse é um sistema simples feito em Python para ajudar a cafeteria Coffee
Shops Tia Rosa a organizar o cardápio, os clientes e os pedidos. O sistema
foi feito para essa atividade da disciplina de Lógica, Algoritmos e
Programação de Computadores.

## Sobre o projeto

A cafeteria Tia Rosa fazia tudo no papel: os pedidos, os preços, os
clientes. Isso causava confusão e demorava. Esse sistema resolve isso
mostrando um menu simples no terminal, onde dá pra:

- ver e organizar o cardápio
- cadastrar clientes
- fazer pedidos
- ver o histórico de pedidos
- ver quanto a cafeteria já vendeu
- dar pontos de fidelidade pros clientes

## Arquivos do projeto

- `main.py` - é o arquivo que a gente roda, tem o menu do sistema
- `classes.py` - tem as classes Produto, Cliente e Pedido
- `funcoes.py` - tem as funções que fazem o sistema funcionar
- `teste_sistema.py` - testa se tudo está funcionando certo

## Como rodar o sistema

Você precisa ter o Python instalado no computador (versão 3).

1. Abra o terminal na pasta do projeto
2. Digite o comando abaixo e aperte Enter:

```
python3 main.py
```

3. Vai aparecer um menu com números, é só digitar o número da opção que
   você quer usar.

## Como rodar os testes

Pra ver se o sistema está funcionando direito, roda esse comando:

```
python3 teste_sistema.py
```

Vai aparecer uma lista de testes com "OK" na frente de cada um, e no final
mostra quantos passaram.

## O que dá pra fazer no menu

1. **Ver cardápio** - mostra todos os produtos com preço e descrição
2. **Adicionar produto** - cadastra um produto novo no cardápio
3. **Remover produto** - tira um produto do cardápio
4. **Cadastrar cliente** - cadastra um cliente novo
5. **Ver clientes e pontos** - mostra os clientes e quantos pontos cada
   um tem
6. **Fazer pedido** - escolhe um cliente e os produtos que ele comprou
7. **Ver histórico de pedidos** - mostra todos os pedidos feitos
8. **Ver relatório de vendas** - mostra o total vendido e o ticket médio

## Como funciona o programa de pontos

Pra cada 1 real gasto, o cliente ganha 1 ponto de fidelidade. Por exemplo,
se o cliente gastar R$ 15,00, ele ganha 15 pontos.

## Observação

Os dados (cardápio, clientes e pedidos) ficam guardados só enquanto o
programa está rodando. Quando você fecha o programa, os dados são
perdidos, porque esse é um sistema simples feito pra estudar os conceitos
de Python (classes, funções, listas, laços e condicionais).
