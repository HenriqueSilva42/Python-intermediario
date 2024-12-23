# Inicializa o pacote aventura_pkg

# Importa as funções e classes dos módulos dentro do pacote
from .labirinto import criar_labirinto, imprimir_labirinto
from .jogador import Jogador, mover, escutar_comandos
from .utils import imprime_instrucoes, imprime_menu

# Agora você pode acessar as funções e classes diretamente a partir do pacote aventura_pkg
# Exemplo:
# from aventura_pkg import criar_labirinto
