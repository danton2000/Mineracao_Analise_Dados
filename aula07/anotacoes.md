# Normalização
    Separar 1 tabela em varias pequenas tabelas

# Modelagem das Tabelas

## Pedido
    - Id_pedido #Identificador unico do pedido
    - Data_pedido #Data do pedido
    - Status_pedido #Status do pedido

## Cliente
    - Id_cliente #Identificador unico do cliente
    - Nome_cliente #Nome do cliente
    - Email_cliente #Email do cliente

## Vendedor
    - Id_vendedor #Identificador unico do vendedor
    - Nome_vendedor #Nome do vendedor
    - Setor_vendedor #Setor do vendedor
    - Data_admissao_vendedor #Data de admissao do vendedor

## Produto
    - Id_produto #Identificador unico do produto
    - Nome_produto #Nome do produto
    - Valor_produto #Valor do produto
    - Observacao_produto #Observacao do produto

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

1 - Criar Banco - ok
2 - Criar Tabelas com suas colunas
3 - Criar uma base de amostra que corresponde as tabelas e colunas
    - Chat GPT
4 - Converter essa base de amostra para o SQL
5 - Inserir essas informações no banco
6 - Rankeamneto(Select)