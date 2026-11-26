from model.cliente import Cliente
from model.enums import Material
from model.fabrica_chapeu import FabricaChapeu


def ler_inteiro(mensagem, minimo=0):
    while True:
        try:
            valor = int(input(mensagem))
        except ValueError:
            print("Digite um número inteiro válido.")
            continue

        if valor >= minimo:
            return valor
        print(f"Digite um número maior ou igual a {minimo}.")


def ler_preco(tipo):
    precos = {"cartola": 100.00, "fedora": 150.00,}
    try:
        return precos[tipo.strip().lower()]
    except (AttributeError, KeyError):
        raise ValueError("Tipo de chapéu inválido. Escolha cartola ou fedora.")


def ler_tipo_chapeu():
    while True:
        tipo = input("Tipo (cartola/fedora): ").strip().lower()
        if tipo in ("cartola", "fedora"):
            return tipo
        print("Tipo inválido. Escolha cartola ou fedora.")


def ler_material():
    opcoes = ", ".join(material.name for material in Material)
    while True:
        nome_material = input(f"Material ({opcoes}): ").strip().upper()
        try:
            return Material[nome_material]
        except KeyError:
            print("Material inválido. Escolha uma das opções exibidas.")


cliente = Cliente(input("Nome do cliente: ").strip(), input("CPF do cliente: ").strip(),)

quantidade_chapeus = ler_inteiro("Quantos chapéus deseja cadastrar? ", minimo=1)
chapeus = []

for indice in range(quantidade_chapeus):
    print(f"\nCadastro do chapéu {indice + 1}")
    tipo = ler_tipo_chapeu()
    nome = input("Nome do modelo: ").strip()
    cor = input("Cor: ").strip()
    preco = ler_preco(tipo)
    tamanho = input("Tamanho: ").strip()
    material = ler_material()
    chapeus.append(FabricaChapeu.criar(tipo, nome, cor, preco, tamanho, material))

print(cliente)
print()

for chapeu in chapeus:
    chapeu.exibir_informacoes()
    print(f"Preço final: R${chapeu.calcular_preco():.2f}")
    print()