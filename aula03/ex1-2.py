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
lista_frutas_selecionados = []
lista_frutas_valores = []


cursor = 0

for linha in linhas:

    if cursor > 0:
        
        nome_fruta = linha[1]
        valor = float(linha[2])
        
        if nome_fruta not in lista_frutas_selecionados:
            
            lista_frutas_selecionados.append(nome_fruta)
            
            lista_frutas_valores.append([nome_fruta, valor])
      
    cursor += 1


print(lista_frutas_valores)
    

    
