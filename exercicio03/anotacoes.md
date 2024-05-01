# Normalização
    Separar 1 tabela em varias pequenas tabelas

# Modelagem das Tabelas

## Pedido
    - Id_pedido #Identificador unico do pedido
    - Data_pedido #Data do pedido
    - Status_pedido #Status do pedido
    - Id_cliente #Identificador unico do cliente(FK)
    - Id_vendedor #Identificador unico do vendedor(FK)

## Itens
    - Id_pedido #Identificador unico do pedido
    - Id_produto #Identificador unico do produto

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
    - Id_estoque #Identificador unico do estoque
    - quantidade_estoque #Quantidade disponivel do produto no estoque
    - Id_produto #Identificador unico do produto(FK) 

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
        - Vendidos acima do valor médio

#### PASSOS

1 - Criar Banco - ok
2 - Criar Tabelas com suas colunas - ok
3 - Criar uma base de amostra que corresponde as tabelas e colunas - ok
4 - Converter essa base de amostra para o SQL - ok 
5 - Inserir essas informações no banco - ok
6 - Rankeamneto(Select) - ok

##### Perguntas feitas pelo CHAT GPT
Olá, mapeie a seguinte tabela em SQL:
CREATE TABLE IF NOT EXISTS CLIENTE (
	id_cliente INTEGER PRIMARY KEY,
	nome_cliente VARCHAR(100) NOT NULL,
	email_cliente VARCHAR(100) NOT NULL
)

Preciso de 5 registros no formatado .csv, ponto e virgula que corresponde a tabela CLIENTES

Certo, agora mapeie essa outra tabela em SQL:
CREATE TABLE IF NOT EXISTS VENDEDOR (
	id_vendedor INTEGER PRIMARY KEY,
	nome_vendedor VARCHAR(100) NOT NULL,
	setor_vendedor VARCHAR(100) NOT NULL,
	data_admissao_vendedor VARCHAR(100) NOT NULL
)
Preciso novamente de 5 registros no formatado .csv, ponto e virgula que corresponde a tabela VENDEDOR

Certo, agora mapeie essa outra tabela em SQL:
CREATE TABLE IF NOT EXISTS PRODUTO (
	id_produto INTEGER PRIMARY KEY,
	nome_produto VARCHAR(100) NOT NULL,
	valor_produto DECIMAL(5,2) NOT NULL,
	observacao_produto VARCHAR(100) NOT NULL
)
Preciso novamente de 5 registros no formatado .csv, ponto e virgula que corresponde a tabela PRODUTO

Certo, agora mapeie essa outra tabela em SQL:
CREATE TABLE IF NOT EXISTS ESTOQUE (
	id_estoque INTEGER PRIMARY KEY,
	quantidade_estoque INTEGER NOT NULL,
	id_produto integer REFERENCES PRODUTO (id_produto)
)
Preciso novamente de 5 registros no formatado .csv, ponto e virgula que corresponde a tabela ESTOQUE que faça ligação com a base de produtos

Certo, agora mapeie essa outra tabela em SQL:
CREATE TABLE IF NOT EXISTS PEDIDO (
	id_pedido INTEGER PRIMARY KEY,
	data_pedido DATE NOT NULL,
	status_pedido VARCHAR(100) NOT NULL,
	id_cliente integer REFERENCES Cliente (id_cliente),
	id_vendedor integer REFERENCES Vendedor (id_vendedor)
)
Preciso novamente de 5 registros no formatado .csv, ponto e virgula que corresponde a tabela PEDIDO que faça ligação com a base de cliente e que também faça ligação com a base de vendedor

Certo, agora mapeie essa outra tabela em SQL:
CREATE TABLE IF NOT EXISTS ITENS (
	id_produto integer REFERENCES Produto (id_produto),
	id_pedido integer REFERENCES Pedido (id_pedido),
	quantidade_item INTEGER NOT NULL
)
Preciso novamente de 5 registros no formatado .csv, ponto e virgula que corresponde a tabela ITENS que faça ligação com a base de produto e que também faça ligação com a base de pedido