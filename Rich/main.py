import argparse
from layout import exibir_layout
from painel import exibir_painel
from progresso import exibir_progresso
from estilo import exibir_com_estilo

def main():
    parser = argparse.ArgumentParser(description="Imprimir texto formatado usando a biblioteca Rich.")
    parser.add_argument("texto", help="Texto ou caminho para um arquivo de texto")
    parser.add_argument("-a", "--arquivo", action="store_true", help="Indica que o argumento 'texto' é um arquivo")
    parser.add_argument("-m", "--modulo", choices=["layout", "painel", "progresso", "estilo"], required=True, help="Escolha o módulo a ser usado")
    parser.add_argument("-f", "--funcao", choices=["exibir_layout", "exibir_painel", "exibir_progresso", "exibir_com_estilo"], required=True, help="Escolha a função a ser utilizada")

    args = parser.parse_args()

    if args.modulo == "layout" and args.funcao == "exibir_layout":
        exibir_layout(args.texto, args.arquivo)
    elif args.modulo == "painel" and args.funcao == "exibir_painel":
        exibir_painel(args.texto, args.arquivo)
    elif args.modulo == "progresso" and args.funcao == "exibir_progresso":
        exibir_progresso(args.texto, args.arquivo)
    elif args.modulo == "estilo" and args.funcao == "exibir_com_estilo":
        exibir_com_estilo(args.texto, args.arquivo)

if __name__ == "__main__":
    main()
