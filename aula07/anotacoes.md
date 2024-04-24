# Normalização
    Separar 1 tabela em varias pequenas tabelas

# Modelagem das Tabelas

## Pedido

## Cliente

## Vendedor

## Produto

## Estoque

Pedido n ---- 1 Cliente
Pedido n ---- 1 Vendedor
Pedido 1 ---- n PedProd n ---- 1 Produto
Produto 1 ---- n Estoque

### Exercicio
Cloudera(base free)

1 - Criação
    - Em .csv para cada um arquivo para um banco FREE
2 - Ranking Vendedor
        - Quantidade Produto
        - Valores
        - Quantidade Clientes
        - Quantidade Produto
        - Vendidos acima do valor médio

#### PASSOS

1 - Criar Banco
2 - Criar Tabelas com suas colunas
3 - Criar uma base de amostra que corresponde as tabelas e colunas
4 - Converter essa base de amostra para o SQL
5 - Inserir essas informações no banco