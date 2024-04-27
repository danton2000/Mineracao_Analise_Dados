CREATE TABLE IF NOT EXISTS CLIENTE (
	id_cliente INTEGER PRIMARY KEY,
	nome_cliente VARCHAR(100) NOT NULL,
	email_cliente VARCHAR(100) NOT NULL
)

CREATE TABLE IF NOT EXISTS VENDEDOR (
	id_vendedor INTEGER PRIMARY KEY,
	nome_vendedor VARCHAR(100) NOT NULL,
	setor_vendedor VARCHAR(100) NOT NULL,
	data_admissao_vendedor VARCHAR(100) NOT NULL
)

CREATE TABLE IF NOT EXISTS PRODUTO (
	id_produto INTEGER PRIMARY KEY,
	nome_produto VARCHAR(100) NOT NULL,
	valor_produto DECIMAL(5,2) NOT NULL,
	observacao_produto VARCHAR(100) NOT NULL
)

CREATE TABLE IF NOT EXISTS ESTOQUE (
	id_estoque INTEGER PRIMARY KEY,
	quantidade_estoque INTEGER NOT NULL,
	id_produto integer REFERENCES PRODUTO (id_produto)
)

CREATE TABLE IF NOT EXISTS PEDIDO (
	id_pedido INTEGER PRIMARY KEY,
	data_pedido DATE NOT NULL,
	status_pedido VARCHAR(100) NOT NULL,
	id_cliente integer REFERENCES Cliente (id_cliente),
	id_vendedor integer REFERENCES Vendedor (id_vendedor)
)

CREATE TABLE IF NOT EXISTS ITENS (
	id_produto integer REFERENCES Produto (id_produto),
	id_pedido integer REFERENCES Pedido (id_pedido)
)






