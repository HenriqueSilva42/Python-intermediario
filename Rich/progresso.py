from rich.console import Console
from rich.progress import Progress

def exibir_progresso(texto: str, isArquivo: bool = False):
    """
    Exibe um progresso de leitura do texto utilizando o rich.

    :param texto: Texto a ser exibido ou caminho para o arquivo.
    :param isArquivo: Booleano que indica se o texto é o caminho para um arquivo.
    """
    console = Console()

    if isArquivo:
        with open(texto, 'r') as f:
            texto = f.read()

    with Progress() as progress:
        task = progress.add_task("[cyan]Processando...", total=len(texto))
        for char in texto:
            progress.update(task, advance=1)
            console.print(char, end='', flush=True)
