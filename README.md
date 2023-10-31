# Comércio Eletrônico "Polinômios da Taylor"

 O arquivo comercio_eletronicoo.py implementa um sistema de comércio eletrônico da loja fictícia **Polinômios da Taylor**, sendo a relação entre os produtos e as marcas também fictícia. Ele inclui classes para produtos e inventário dos mesmos.

## Conteúdo

Incluímos as seguintes classes:

- **Produto:** Representa um produto com atributos como código de barras, nome e preço.
- **Inventario:** Gerencia o estoque de produtos, valida códigos de barras, vende produtos, repõe estoque e registra devoluções (retorno).
- **Especializações de Produtos:** Três tipos de produtos são definidos como especializações de Produto: Discos, Roupas e Posters, cada um com atributos específicos.

## Uso Básico (Requisitos do Trabalho)

Você pode criar instâncias de produtos e gerenciar seu estoque com as funcionalidades de venda, reposição e devolução. Também há uma enumeração para as marcas dos produtos.

## Exemplo de Uso

```python
# Importe o módulo e utilize as classes conforme necessário
#Cadastrar um disco
disco6 = Discos_taylorswift('006', 'Lover', 20.99, Marca.Universal_Republic_Records)
#Vender o disco
inventario.vender_produto('006')
```

## Sobre nós

  Para essa atividade, feita para a disciplina de Linguagens de Programação, fizemos uso do método de pair programming, de maneira que os commits estão apenas na conta de um integrante da dupla. Apesar disso, cada um dedicou tempo e esforço comparáveis, trabalhando presencialmente lado a lado. Curioso sobre nós? Cheque nossos perfis no github abaixo:

  * <a href="https://github.com/nataliabrandao">Natália Brandão de Souza 'Nati'</a>

    ![Picture, with CONSENT, of a team member](img/nati.jpg)
 
  * <a href="https://github.com/dyva101">Davy Albert Dutra de Andrade 'Dyva'</a>

    ![Picture, with CONSENT, of a team member](img/dyva.jpg)