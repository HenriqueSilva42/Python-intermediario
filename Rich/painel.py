from rich.console import Console
from rich.panel import Panel

def exibir_painel(texto: str, isArquivo: bool = False):
    """
    Exibe o texto dentro de um painel usando o rich.

    :param texto: Texto a ser exibido ou caminho para o arquivo.
    :param isArquivo: Booleano que indica se o texto é o caminho para um arquivo.
    """
    console = Console()

    if isArquivo:
        with open(texto, 'r') as f:
            texto = f.read()

    painel = Panel(texto, title="Painel de Texto")
    console.print(painel)
