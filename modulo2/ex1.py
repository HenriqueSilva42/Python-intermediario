from datetime import datetime

class Evento:
    # Atributo de classe
    total_eventos = 0

    def __init__(self, titulo, data_hora, descricao):
        self.titulo = titulo
        self.data_hora = data_hora
        self.descricao = descricao
        self.is_concluido = False
        Evento.total_eventos += 1

    # Método de instância
    def isConcluido(self):
        if self.data_hora < datetime.now():
            self.is_concluido = True

    # Método de classe
    @classmethod
    def num_eventos(cls):
        return cls.total_eventos

    # Método estático
    @staticmethod
    def valida_evento(titulo, data_hora, descricao):
        return isinstance(titulo, str) and isinstance(data_hora, datetime) and isinstance(descricao, str)

    # Método mágico para exibição
    def __str__(self):
        return f"Evento: {self.titulo}, Data: {self.data_hora}, Descrição: {self.descricao}, Concluido: {self.is_concluido}"

    # Métodos mágicos de comparação
    def __eq__(self, other):
        return self.data_hora == other.data_hora

    def __ne__(self, other):
        return self.data_hora != other.data_hora

    def __lt__(self, other):
        return self.data_hora < other.data_hora

    def __le__(self, other):
        return self.data_hora <= other.data_hora

    def __gt__(self, other):
        return self.data_hora > other.data_hora

    def __ge__(self, other):
        return self.data_hora >= other.data_hora

# Testando a classe
if __name__ == "__main__":
    # Criando dois eventos
    evento1 = Evento("Reunião", datetime(2023, 12, 25, 14, 30), "Reunião de final de ano.")
    evento2 = Evento("Entrega de projeto", datetime(2024, 1, 15, 10, 0), "Prazo final para entrega.")

    # Testando os atributos
    print(evento1)
    print(evento2)
    
    # Testando método isConcluido
    evento1.isConcluido()
    print(f"Evento 1 concluído: {evento1.is_concluido}")

    # Testando método de classe num_eventos
    print(f"Número total de eventos: {Evento.num_eventos()}")

    # Testando método estático valida_evento
    print(Evento.valida_evento("Teste", datetime.now(), "Descrição de teste"))  # True
    print(Evento.valida_evento("Teste", "2023-12-25", "Descrição de teste"))  # False

    # Testando métodos mágicos de comparação
    print(evento1 == evento2)  # False
    print(evento1 < evento2)   # True
