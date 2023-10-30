from enum import Enum

# Classe Produto
class Produto:
    def __init__(self, codigo_barras, nome, preco, marca):
        self.codigo_barras = codigo_barras
        self.nome = nome
        self.preco = preco
        self.marca = marca

class Inventario(self, nome, qtde):
    def __init__(self):
        self.estoque = []

    #retira o produto do inventario, caso seja vendido
    def vender_produto(self, codigo_barras):

        try:
            for produto in self.estoque:
                isProduto = (produto.codigo_barras == codigo_barras)

                if produto.codigo_barras == codigo_barras:
                    self.estoque.remove(produto)
            
            if isProduto == False:
                raise KeyError()
            
        except NameError:
            print("O produto está fora de estoque no momento :( Sorry, Swifter")
        except KeyError:
            print("O código de barras não é válido!")
            
    #atualiza o inventario repondo produtos de acordo com a qtde dada
    def repor_produto(self, nome, qtde):
        for n in range(qtde):
            self.estoque.append(nome)

    #adiciona o produto de volta ao estoque, em caso de devolução
    def retorno_produto(self, nome):
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







