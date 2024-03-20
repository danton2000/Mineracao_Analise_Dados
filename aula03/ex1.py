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
arquivo = open("C:/Users/181810032/Desktop/Mineracao_Analise_Dados/aula02/cadastro_produtosV1.csv")

# Colocando todas as informações do arquivo na variavel
linhas = csv.reader(arquivo)

maior_preco = 0
menor_preco = 0
soma = 0
qtd = 0
nome_fruta = ""

lista_frutas = []
lista_nome_frutas = []
lista_maior_preco = []

cursor = 0

for linha in linhas:

    if cursor > 0:

       pass

        

        
           


        
    #print(linha)
    cursor += 1

print(lista_nome_frutas)


    
    

    
