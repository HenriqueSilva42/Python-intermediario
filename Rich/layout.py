from rich.console import Console
from rich.layout import Layout

def exibir_layout(texto: str, isArquivo: bool = False):
    """
    Exibe o texto em um layout usando o rich.

    :param texto: Texto a ser exibido ou caminho para o arquivo.
    :param isArquivo: Booleano que indica se o texto é o caminho para um arquivo.
    """
    console = Console()
    layout = Layout()

    if isArquivo:
        with open(texto, 'r') as f:
            texto = f.read()

    layout.split_column(Layout(texto))
    console.print(layout)
