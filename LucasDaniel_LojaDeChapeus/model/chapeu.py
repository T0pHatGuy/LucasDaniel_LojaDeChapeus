from abc import ABC, abstractmethod

class Chapeu(ABC):
    def __init__(self, nome, cor, preco):
        self.nome = nome
        self.cor = cor
        self.__preco = preco

    @property
    def preco(self):
        return self.__preco

    @abstractmethod
    def calcular_preco(self):
        pass

    def __str__(self):
        return f"Chapéu: {self.nome}, Cor: {self.cor}, Preço: R${self.__preco:.2f}"
