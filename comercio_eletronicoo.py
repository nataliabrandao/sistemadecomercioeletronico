from enum import Enum

# Classe Produto
class Produto:
    def __init__(self, codigo_barras, nome, preco, marca):
        self.codigo_barras = codigo_barras
        self.nome = nome
        self.preco = preco
        self.marca = marca

# Especializações de produtos
class Eletronico(Produto):
    def _init_(self, codigo_barras, nome, preco, marca, modelo):
        super()._init_(codigo_barras, nome, preco, marca)
        self.modelo = modelo

class Vestuario(Produto):
    def _init_(self, codigo_barras, nome, preco, marca, tamanho):
        super()._init_(codigo_barras, nome, preco, marca)
        self.tamanho = tamanho
