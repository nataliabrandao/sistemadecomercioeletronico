from enum import Enum

# Classe Produto
class Produto:
    def __init__(self, codigo_barras, nome, preco, marca):
        self.codigo_barras = codigo_barras
        self.nome = nome
        self.preco = preco
        self.marca = marca

# Especializações de produtos
class discos_taylorswift(Produto):
    def _init_(self, codigo_barras, nome, preco, marca, gravadora):
        super()._init_(codigo_barras, nome, preco, marca)
        self.gravadora = gravadora

class roupas_taylorswift(Produto):
    def _init_(self, codigo_barras, nome, preco, marca, tamanho):
        super()._init_(codigo_barras, nome, preco, marca)
        self.tamanho = tamanho

class posters_taylorswift(Produto):
    def _init_(self, codigo_barras, nome, preço, marca, cor, tamanho):
        super()._init_(codigo_barras, nome, preço, marca)
        self.cor = cor
        self.tamanho = tamanho

