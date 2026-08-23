# demo_automatico.py
# Esse script roda o main.py sozinho, digitando as opcoes do menu
# automaticamente. Serve so pra gerar uma demonstracao na tela e
# facilitar tirar print do sistema funcionando. Nao faz parte do
# sistema, é so uma ferramenta de apoio.

import pty
import os
import select
import time
import sys

# opcoes que vao ser "digitadas" no menu, uma de cada vez
opcoes = [
    "1",                 # ver cardapio
    "4",                 # cadastrar cliente
    "Maria Oliveira",    # nome do cliente novo
    "11999998888",       # telefone do cliente novo
    "6",                 # fazer pedido
    "1",                 # escolhe o cliente numero 1
    "1",                 # escolhe o produto Cafe Expresso
    "s",                 # quer adicionar mais um produto
    "5",                 # escolhe o produto Bolo de Chocolate
    "n",                 # nao quer mais produtos
    "7",                 # ver historico de pedidos
    "8",                 # ver relatorio de vendas
    "0",                 # sair do sistema
]

tempo_entre_opcoes = 1.3


def escutar(fd, segundos):
    # fica lendo o que o programa vai escrevendo na tela por um tempo
    fim = time.time() + segundos
    while time.time() < fim:
        prontos, _, _ = select.select([fd], [], [], 0.2)
        if fd in prontos:
            try:
                dados = os.read(fd, 4096)
            except OSError:
                return
            if not dados:
                return
            sys.stdout.buffer.write(dados)
            sys.stdout.flush()


def main():
    pid, fd = pty.fork()

    if pid == 0:
        # esse eh o processo filho, ele vira o main.py de verdade
        os.execvp("python3", ["python3", "main.py"])
    else:
        # esse eh o processo pai, ele vai "digitando" as opcoes
        escutar(fd, 1.5)
        for opcao in opcoes:
            os.write(fd, (opcao + "\n").encode())
            escutar(fd, tempo_entre_opcoes)
        escutar(fd, 2)
        print("\n\n[demonstracao automatica terminou]")


if __name__ == "__main__":
    main()
