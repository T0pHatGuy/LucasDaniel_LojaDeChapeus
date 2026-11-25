from enum import Enum


class Material(str, Enum):
    FELTRO = "Feltro"
    PALHA = "Palha"
    COURO = "Couro"
    LONA = "Lona"

    def __str__(self):
        return self.value

    @property
    def acrescimo(self):
        return {
            Material.FELTRO: 30.00,
            Material.PALHA: 20.00,
            Material.COURO: 50.00,
            Material.LONA: 15.00,
        }[self]