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

# lista para valores, maior e menor

# tem a fruta? não, coloca na nova lista, se tiver validar os valores

# Importa a lib para utilizar e manipular arquivos .CSV
import csv

# Pegando o arquivo utilizando o caminho absuluto
try:
    arquivo = open("./aula03/cadastro_produtosV1.csv")
except:
    print("Falha ao encontrar o arquivo.")
    exit()

# Colocando todas as informações do arquivo na variavel
linhas = csv.reader(arquivo)

lista_maior_preco = []
lista_menor_preco = []
lista_qtd_frutas = []
qtd = 1
lista_media_preco_frutas = []
lista_valor_total_frutas = []
lista_qtd_fruta_acima_media = []

lista_frutas = []

soma = 0
cursor = 0

for linha in linhas:

    if cursor > 0:

        if linha[1] not in lista_frutas:
            
            lista_frutas.append(linha[1])

            lista_maior_preco.append(float(linha[2]))

            lista_menor_preco.append(float(linha[2]))

            lista_qtd_frutas.append(qtd)

            lista_valor_total_frutas.append(0)

            lista_media_preco_frutas.append(0)

            lista_qtd_fruta_acima_media.append(0)
            
        else:
            
            # encontrado a fruta que foi repetido
            index_fruta = lista_frutas.index(linha[1])

            # Verificando o maior valor das frutas
            if float(linha[2]) > lista_maior_preco[index_fruta]:
                # Atualizando as informações pelo indice encontrado
                lista_frutas[index_fruta] = linha[1]

                lista_maior_preco[index_fruta] = float(linha[2])

                soma += float(linha[2])

                lista_valor_total_frutas[index_fruta] = soma

            # Verificando o maior valor das frutas
            if float(linha[2]) < lista_menor_preco[index_fruta]:
                # Atualizando as informações pelo indice encontrado
                lista_frutas[index_fruta] = linha[1]

                lista_menor_preco[index_fruta] = float(linha[2])
            
            # Verificando a qtd de frutas que foram repitidas
            lista_qtd_frutas[index_fruta] += 1

            # Verificando a media de preços das frutas
            #soma = float(linha[2])

            lista_media_preco_frutas[index_fruta] = lista_valor_total_frutas[index_fruta] / lista_qtd_frutas[index_fruta] 

            #Verificando a qtd de frutas que estão acima da media
            if float(linha[2]) > lista_media_preco_frutas[index_fruta]:

                lista_qtd_fruta_acima_media[index_fruta] += 1


            
    cursor += 1

print(lista_frutas[13])

print(lista_maior_preco[13])

print(lista_menor_preco[13])

print(lista_qtd_frutas[13])

print(lista_valor_total_frutas[13])

print(lista_media_preco_frutas[13])

print(lista_qtd_fruta_acima_media[13])
    

    
