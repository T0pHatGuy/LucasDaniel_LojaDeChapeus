from abc import ABC, abstractmethod

class Chapeu(ABC):
    def __init__(self, nome, cor, preco, estoque):
        self.nome = nome
        self.cor = cor
        self.__preco = preco
        self.__estoque = estoque

    @property
    def preco(self):
        return self.__preco

    @property
    def estoque(self):
        return self.__estoque

    def tirar_estoque(self, quantidade):
        if quantidade <= self.__estoque:
            self.__estoque -= quantidade
            return True
        else:
            return False

    def adicionar_estoque(self, quantidade):
        if quantidade <= 0:
            raise ValueError("A quantidade a ser adicionada deve ser maior que zero.")
        self.__estoque += quantidade

    @abstractmethod
    def calcular_preco(self):
        pass

    def __str__(self):
        return f"Chapéu: {self.nome}, Cor: {self.cor}, Preço: R${self.__preco:.2f}, Estoque: {self.__estoque}"
