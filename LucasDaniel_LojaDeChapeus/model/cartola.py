from chapeu import Chapeu

class Cartola(Chapeu):
    def __init__(self, nome, cor, preco, estoque, tamanho, material):
        super().__init__(nome, cor, preco, estoque)
        self.tamanho = tamanho
        self.material = material

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Material: {self.material}")