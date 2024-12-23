import random

def criar_labirinto(dificuldade: int) -> list:
    """
    Cria um labirinto aleatório com base no nível de dificuldade.

    :param dificuldade: Nível de dificuldade que altera o tamanho do labirinto.
    :return: Lista de listas representando o labirinto.
    """
    labirinto = []
    for i in range(dificuldade):
        linha = [random.choice(['#', '.']) for _ in range(dificuldade)]
        labirinto.append(linha)
    labirinto[0][0] = 'P'  # Posição inicial do jogador
    labirinto[dificuldade-1][dificuldade-1] = 'E'  # Posição de saída
    return labirinto

def imprimir_labirinto(labirinto: list) -> None:
    """
    Imprime o labirinto na tela.

    :param labirinto: Labirinto a ser impresso.
    """
    for linha in labirinto:
        print(" ".join(linha))
