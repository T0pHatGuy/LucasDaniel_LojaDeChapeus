from model.cartola import Cartola
from model.chapeu import Chapeu
from model.fedora import Fedora


class FabricaChapeu:
    @staticmethod
    def criar(tipo, nome, cor, preco, tamanho, material) -> Chapeu:
        if tipo.lower() == "cartola":
            return Cartola(nome, cor, preco, tamanho, material)
        if tipo.lower() == "fedora":
            return Fedora(nome, cor, preco, tamanho, material)
        raise ValueError(f"Tipo de chapéu não suportado: {tipo}")