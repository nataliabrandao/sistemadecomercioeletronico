from enum import Enum

# Classe Produto
class Produto:
    def __init__(self, codigo_barras, nome, preco, marca):
        self.codigo_barras = codigo_barras
        self.nome = nome
        self.preco = preco
        self.marca = marca

    def inventario(self, nome, qtde):
        self.estoque = []

    def vender_produto(self, codigo_barras):
        for produto in self.estoque:
            if produto.codigo_barras == codigo_barras:
                self.estoque.remove(produto)

    def repor_produto(self, nome, qtde):
        for n in range(qtde):
            self.estoque.append(nome)
    

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

class Marca(Enum):
    WorldHeart = 1
    Chanel = 2
    Zara = 3
    Virgin_EMI_Records = 4
    Big_Machine_Records = 5
    Universal_Republic_Records = 6
    Papelaria_Catete = 7
    Papelaria_JLM = 8
    Americanas = 9







