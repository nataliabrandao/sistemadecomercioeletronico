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
    def __init__(self, codigo_barras, nome, preco, gravadora):
        super().__init__(codigo_barras, nome, preco)
        self.gravadora = gravadora

class roupas_taylorswift(Produto):
    def __init__(self, codigo_barras, nome, preco, marca, tamanho):
        super().__init__(codigo_barras, nome, preco, marca)
        self.tamanho = tamanho

class posters_taylorswift(Produto):
    def __init__(self, codigo_barras, nome, preço, marca, cor, tamanho):
        super().__init__(codigo_barras, nome, preço, marca)
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

if __init__ == "__main__":

    #Criação de estoque da Loja "Polinômios da Taylor"
    discos_taylorswift('001', 'Fearless', 15.99, MarcaProduto.Republic_Records),
    discos_taylorswift('002', 'Speak Now', 12.99, MarcaProduto.Republic_Records),
    discos_taylorswift('003', 'Red', 18.99, MarcaProduto.Big_Machine_Records),
    discos_taylorswift('004', '1989', 19.99, MarcaProduto.Big_Machine_Records),
    discos_taylorswift('005', 'Reputation', 22.99, MarcaProduto.Big_Machine_Records),
    discos_taylorswift('006', 'Lover', 20.99, MarcaProduto.Republic_Records),
    discos_taylorswift('007', 'Folklore', 21.99, MarcaProduto.Universal_Music_Group),
    discos_taylorswift('008', 'Evermore', 21.99, MarcaProduto.Universal_Music_Group)
    roupas_taylorswift('101', 'Moletom', 120.50, Marca.Zara, M)
    roupas_taylorswift('102', 'Moletom', 120.50, Marca.Zara, G)
    roupas_taylorswift('103', 'Baby Look', 599.99, Marca.Chanel, M)
    roupas_taylorswift('104', 'Baby Look', 599.99, Marca.Chanel, G)





