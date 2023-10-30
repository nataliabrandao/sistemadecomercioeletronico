from enum import Enum

# Classe Produto
class Produto:
    def __init__(self, codigo_barras, nome, preco):
        self.codigo_barras = codigo_barras
        self.nome = nome
        self.preco = preco 

# Classe Inventario
class Inventario:
    def __init__(self):
        self.estoque = []
        self.codigo_de_barras_validos = []

    #identifica o codigo de barras de um produto como valido
    def validar_codigo(self, produto):
        self.codigo_de_barras_validos.append(produto.codigo_barras)

    #retira o produto do inventario, caso seja vendido
    def vender_produto(self, codigo_barras):
        isproduto = False
        try:

            for n in self.codigo_de_barras_validos:
                if n == codigo_barras:
                    isproduto = True
                    
            if isproduto == False:
                raise KeyError()

            for produto in self.estoque:
                isinstock = (produto.codigo_barras == codigo_barras)

                if isinstock ==  True:
                    self.estoque.remove(produto)
                    return produto
                else:
                    raise NameError()
            
        except NameError:
            print("O produto está fora de estoque no momento :( Sorry, Swifter")
        except KeyError:
            print("O código de barras é inválido!")
            
    #atualiza o inventario repondo produtos de acordo com a qtde dada
    def repor_produto(self, nome, qtde):
        for n in range(qtde):
            self.estoque.append(nome)

    #adiciona o produto de volta ao estoque, em caso de devolução
    def retorno_produto(self, nome):
        self.estoque.append(nome)
    
# Especializações de produtos
class Discos_taylorswift(Produto):
    def __init__(self, codigo_barras, nome, preco, gravadora):
        super().__init__(codigo_barras, nome, preco)
        self.gravadora = gravadora

class Roupas_taylorswift(Produto):
    def __init__(self, codigo_barras, nome, preco, marca, tamanho):
        super().__init__(codigo_barras, nome, preco)
        self.marca = marca
        self.tamanho = tamanho

class Posters_taylorswift(Produto):
    def __init__(self, codigo_barras, nome, preço, marca, cor, tamanho):
        super().__init__(codigo_barras, nome, preço)
        self.marca = marca
        self.cor = cor
        self.tamanho = tamanho

class Marca(Enum):
    WorldHeart = 1
    Chanel = 2
    Zara = 3
    Universal_Music_Group = 4
    Big_Machine_Records = 5
    Universal_Republic_Records = 6
    Papelaria_Catete = 7
    Papelaria_JLM = 8
    Americanas = 9


if __name__ == "__main__":

    #Produtos Cadastrados da Loja "Polinômios da Taylor"
    disco1 = Discos_taylorswift('001', 'Fearless', 15.99, Marca.Universal_Republic_Records)
    disco2 = Discos_taylorswift('002', 'Speak Now', 12.99, Marca.Universal_Republic_Records)
    disco3 = Discos_taylorswift('003', 'Red', 18.99, Marca.Big_Machine_Records)
    disco4 = Discos_taylorswift('004', '1989', 19.99, Marca.Big_Machine_Records)
    disco5 = Discos_taylorswift('005', 'Reputation', 22.99, Marca.Big_Machine_Records)
    disco6 = Discos_taylorswift('006', 'Lover', 20.99, Marca.Universal_Republic_Records)
    disco7 = Discos_taylorswift('007', 'Folklore', 21.99, Marca.Universal_Music_Group)
    disco8 = Discos_taylorswift('008', 'Evermore', 21.99, Marca.Universal_Music_Group)
    roupa1 = Roupas_taylorswift('101', 'Moletom', 120.50, Marca.Zara, 'M')
    roupa2 = Roupas_taylorswift('102', 'Moletom', 120.50, Marca.Zara, 'G')
    roupa3 = Roupas_taylorswift('103', 'Baby Look', 599.99, Marca.Chanel, 'M')
    roupa4 = Roupas_taylorswift('104', 'Baby Look', 599.99, Marca.Chanel, 'G')
    poster1 = Posters_taylorswift('201', 'Taylor Swift The Eras Tour', 8.00, Marca.Papelaria_Catete, 'branco', '30x30')
    poster2 = Posters_taylorswift('202', 'A Lot Going On At The Momento', 5.00, Marca.WorldHeart, 'branco', '30x30')