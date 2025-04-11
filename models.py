class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

    def __str__(self):
        return f"{self.nome} - {self.telefone}"


class Servico:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"{self.nome} - R$ {self.preco:.2f}"
