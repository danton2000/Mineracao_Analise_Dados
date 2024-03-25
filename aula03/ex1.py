# Deadline 26/03
# Entrega: planilha de estudo de tempos + código-fonte comentado 
# Descrição:
# Com base em nossa base de testes, criar um código que devolva o nome do produto e:
# O menor valor deste produto;
# O Maior valor deste produto;
# O valor médio deste produto;
# A quantidade deste produto que apresenta valor acima da média.

# maior = 0
# menor = 0
# qtd = 0
# soma = 0
# produto = ""

# tem a fruta? não, coloca na nova lista, se tiver validar os valores

# Importa a lib para utilizar e manipular arquivos .CSV
import csv

# Pegando o arquivo utilizando o caminho absuluto
arquivo = open("./aula03/cadastro_produtosV1.csv")

# Colocando todas as informações do arquivo na variavel
linhas = csv.reader(arquivo)

maior_preco = 0
menor_preco = 0
soma = 0
qtd_produto_acima_media = 0
lista_valores = []
nome_fruta = ""


cursor = 0

for linha in linhas:

    if cursor > 0:

        preco = float(linha[2])
      
        # Pegando o maior preço
        if preco > maior_preco:
            
            maior_preco = preco
            
            menor_preco = preco
        
        # Pegando o menor preço
        elif menor_preco > preco:
        
            menor_preco = preco
        
        soma = preco + soma
    
        nome_fruta = linha[1]
      
    cursor += 1

soma = soma / cursor

lista_valores.append([maior_preco, menor_preco, qtd_produto_acima_media])

print(lista_valores) 
    

    
