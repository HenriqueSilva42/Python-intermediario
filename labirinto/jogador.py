from pynput import keyboard

class Jogador:
    def __init__(self, nome: str, labirinto: list):
        self.nome = nome
        self.labirinto = labirinto
        self.posicao = (0, 0)
        self.pontuacao = 0

    def mover(self, direcao: str):
        x, y = self.posicao
        if direcao == 'w' and x > 0:
            self.posicao = (x - 1, y)
        elif direcao == 's' and x < len(self.labirinto) - 1:
            self.posicao = (x + 1, y)
        elif direcao == 'a' and y > 0:
            self.posicao = (x, y - 1)
        elif direcao == 'd' and y < len(self.labirinto[0]) - 1:
            self.posicao = (x, y + 1)

        # Atualizar a pontuação
        if self.labirinto[x][y] == 'E':  # Se atingir a saída
            self.pontuacao += 10
            return True
        return False

    def escutar_comandos(self):
        """
        Escuta as teclas pressionadas e movimenta o jogador de acordo com a tecla.
        """
        def on_press(key):
            try:
                if hasattr(key, 'char') and key.char:
                    if key.char in ['w', 'a', 's', 'd']:  # Movimentos para cima, esquerda, baixo e direita
                        if self.mover(key.char):
                            print(f"Você ganhou! Pontuação: {self.pontuacao}")
                            return False  # Finaliza o jogo quando o jogador chegar na saída
            except AttributeError:
                pass

        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()
