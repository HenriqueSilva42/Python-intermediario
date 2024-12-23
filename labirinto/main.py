import argparse
from aventura_pkg.labirinto import criar_labirinto, imprimir_labirinto
from aventura_pkg.jogador import Jogador
from aventura_pkg.utils import imprime_instrucoes, imprime_menu

def main():
    parser = argparse.ArgumentParser(description="Jogo Aventura no Labirinto")
    parser.add_argument("--name", required=True, help="Nome do jogador")
    parser.add_argument("--dificuldade", type=int, default=5, help="Dificuldade do labirinto (tamanho)")
    parser.add_argument("--disable-sound", action="store_true", help="Desativa o som")
    args = parser.parse_args()

    imprime_menu()

    escolha = input("Escolha uma opção: ")

    if escolha == '1':  # Jogar
        labirinto = criar_labirinto(args.dificuldade)
        imprimir_labirinto(labirinto)
        jogador = Jogador(args.name, labirinto)
        jogador.escutar_comandos()

    elif escolha == '2':  # Instruções
        imprime_instrucoes()

    elif escolha == '3':  # Sair
        print("Saindo do jogo...")
        return

if __name__ == "__main__":
    main()

