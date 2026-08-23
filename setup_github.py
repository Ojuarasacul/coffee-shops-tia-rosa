# setup_github.py
# Esse script ajuda a colocar o projeto no Git e no GitHub sem precisar
# decorar os comandos. É só rodar ele e responder as perguntas.

import os
import subprocess


def rodar_comando(comando):
    # roda um comando no terminal e mostra o que aconteceu
    print(f"\n> {comando}")
    resultado = subprocess.run(comando, shell=True)
    return resultado.returncode == 0


def main():
    print("==================================================")
    print("CONFIGURAR GIT E GITHUB - COFFEE SHOPS TIA ROSA")
    print("==================================================")
    print("\nEsse script vai preparar o projeto pra subir no GitHub.")
    print("Antes de continuar, crie um repositorio vazio no site")
    print("github.com (sem README, sem licenca).\n")

    nome = input("Digite seu nome (pra configurar o git): ")
    email = input("Digite seu email (o mesmo do GitHub): ")

    print("\nConfigurando o nome e email do git...")
    rodar_comando(f'git config user.name "{nome}"')
    rodar_comando(f'git config user.email "{email}"')

    # inicia o repositorio git, se ainda nao tiver um
    if not os.path.isdir(".git"):
        print("\nIniciando o repositorio git...")
        rodar_comando("git init")
    else:
        print("\nEsse projeto ja tem um repositorio git.")

    print("\nAdicionando os arquivos...")
    rodar_comando("git add .")

    print("\nFazendo o commit...")
    rodar_comando('git commit -m "Sistema Coffee Shops Tia Rosa"')

    link = input("\nCole aqui o link do repositorio do GitHub (https://...): ")

    print("\nConectando com o repositorio do GitHub...")
    rodar_comando(f"git remote add origin {link}")

    print("\nRenomeando a branch principal para main...")
    rodar_comando("git branch -M main")

    print("\nEnviando os arquivos pro GitHub...")
    sucesso = rodar_comando("git push -u origin main")

    print("\n==================================================")
    if sucesso:
        print("PRONTO! O projeto foi enviado para o GitHub.")
        print(f"Confere no link: {link}")
    else:
        print("Deu algum problema no envio.")
        print("Confere se o link do repositorio esta certo e se voce")
        print("tem permissao de acesso a ele. Depois tenta rodar de novo.")
    print("==================================================")


if __name__ == "__main__":
    main()
