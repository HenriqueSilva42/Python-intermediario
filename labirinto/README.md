# Aventura no Labirinto

## Descrição
Aventura no Labirinto é um jogo onde o jogador explora um labirinto usando as teclas WASD. O objetivo é encontrar a saída do labirinto enquanto coleta pontos ao longo do caminho.

## Como Jogar
1. Use as teclas `W`, `A`, `S`, `D` para mover o jogador pelo labirinto.
2. Encontre a saída e ganhe pontos.
3. Se desejar, ouça música durante o jogo (ou desative com a opção `--disable-sound`).

## Como Rodar
1. Crie um ambiente virtual e instale as dependências:
    ```bash
    python -m venv env
    source env/bin/activate  # macOS/Linux
    env\Scripts\activate     # Windows
    pip install -r requirements.txt
    ```
2. Execute o jogo:
    ```bash
    python main.py --name "Jogador" --dificuldade 5
    ```

## Licença
MIT
