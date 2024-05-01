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
	id_pedido integer REFERENCES Pedido (id_pedido),
	quantidade_item INTEGER NOT NULL
)

-- SELECTS(RANKEAMENTO)

--1

SELECT 
vendedor.nome_vendedor, SUM(itens.quantidade_item) as "total_quantidade_itens"
FROM pedido 
JOIN vendedor ON pedido.id_vendedor = vendedor.id_vendedor
JOIN itens ON pedido.id_pedido = itens.id_pedido
JOIN produto ON itens.id_produto = produto.id_produto
GROUP BY vendedor.nome_vendedor
ORDER BY total_quantidade_itens DESC 

--2

SELECT 
vendedor.nome_vendedor, produto.nome_produto, produto.valor_produto, produto.valor_produto * itens.quantidade_item AS "valor_total"
FROM pedido 
JOIN vendedor ON pedido.id_vendedor = vendedor.id_vendedor
JOIN itens ON pedido.id_pedido = itens.id_pedido
JOIN produto ON itens.id_produto = produto.id_produto
ORDER BY valor_total DESC 

--3

SELECT
vendedor.nome_vendedor, COUNT(pedido.id_cliente) AS "total_clientes"
FROM pedido
JOIN vendedor ON pedido.id_vendedor = vendedor.id_vendedor
GROUP BY vendedor.nome_vendedor
ORDER BY total_clientes DESC

--4

SELECT 
vendedor.nome_vendedor,
produto.nome_produto, 
itens.quantidade_item,
produto.valor_produto,
produto.valor_produto * itens.quantidade_item AS "valor_total",
(produto.valor_produto * itens.quantidade_item) / itens.quantidade_item AS "valor_medio"
FROM pedido 
JOIN vendedor ON pedido.id_vendedor = vendedor.id_vendedor
JOIN itens ON pedido.id_pedido = itens.id_pedido
JOIN produto ON itens.id_produto = produto.id_produto
ORDER BY valor_medio DESC











