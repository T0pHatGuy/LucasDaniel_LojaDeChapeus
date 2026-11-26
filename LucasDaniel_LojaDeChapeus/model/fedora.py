from model.chapeu import Chapeu
from model.enums import Material

class Fedora(Chapeu):
    def __init__(self, nome, cor, preco, tamanho, material):
        super().__init__(nome, cor, preco)
        self.__tamanho = tamanho
        self.__material = material if isinstance(material, Material) else Material(material)

    @property
    def tamanho(self):
        return self.__tamanho

    @property
    def material(self):
        return self.__material

    def calcular_preco(self):
        return self.preco + self.material.acrescimo

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Tamanho: {self.tamanho}")
        print(f"Material: {self.material}")
