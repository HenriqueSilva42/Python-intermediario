from rich.console import Console
from rich.text import Text

def exibir_com_estilo(texto: str, isArquivo: bool = False):
    """
    Exibe o texto com formatação de estilo usando o rich.

    :param texto: Texto a ser exibido ou caminho para o arquivo.
    :param isArquivo: Booleano que indica se o texto é o caminho para um arquivo.
    """
    console = Console()

    if isArquivo:
        with open(texto, 'r') as f:
            texto = f.read()

    text = Text(texto, style="bold magenta")
    console.print(text)
