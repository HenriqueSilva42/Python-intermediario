from rich.console import Console

def imprime_instrucoes():
    """
    Imprime as instruções do jogo no terminal com formatação rica.
    """
    console = Console()
    instrucoes = """
    Bem-vindo à Aventura no Labirinto!
    
    Instruções:
    - Use WASD para mover o jogador.
    - O objetivo é encontrar a saída (E) do labirinto.
    - Coletar itens ao longo do caminho para aumentar sua pontuação.
    """
    console.print(instrucoes, style="bold green")

def imprime_menu():
    """
    Imprime o menu principal do jogo.
    """
    console = Console()
    menu = """
    1. Jogar
    2. Instruções
    3. Sair
    """
    console.print(menu, style="bold blue")
