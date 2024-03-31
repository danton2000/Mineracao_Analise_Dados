# Deadline 26/03
# Entrega: planilha de estudo de tempos + código-fonte comentado 
# Descrição:
# Com base em nossa base de testes, criar um código que devolva o nome do produto e:
# O menor valor deste produto;
# O Maior valor deste produto;
# O valor médio deste produto;
# A quantidade deste produto que apresenta valor acima da média.

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

# Variaveis de inicialização
lista_maior_preco = []
lista_menor_preco = []
lista_qtd_frutas = []
lista_media_preco_frutas = []
lista_valor_total_frutas = []
lista_qtd_fruta_acima_media = []
lista_valor_frutas = []
lista_frutas = []
cursor = 0

def verificaMaiorValorFruta(valor_fruta, nome_fruta, index_fruta):
    if valor_fruta > lista_maior_preco[index_fruta]:
        # Atualizando as informações pelo indice encontrado
        lista_frutas[index_fruta] = nome_fruta

        lista_maior_preco[index_fruta] = valor_fruta
        
def verificaMenorValorFruta(valor_fruta, nome_fruta, index_fruta):
    if valor_fruta < lista_menor_preco[index_fruta]:
        # Atualizando as informações pelo indice encontrado
        lista_frutas[index_fruta] = nome_fruta

        lista_menor_preco[index_fruta] = valor_fruta

def verificaQuantidadeFruta(index_fruta):
    lista_qtd_frutas[index_fruta] += 1

def VerificaValorTotalFruta(index_fruta):
    lista_valor_total_frutas[index_fruta] += float(linha[2])

def verificaMediaFruta(index_fruta):
    lista_media_preco_frutas[index_fruta] = lista_valor_total_frutas[index_fruta] / lista_qtd_frutas[index_fruta] 


for linha in linhas:

    if cursor > 0:

        # Se o nome da fruta não estiver na lista de frutas
        if linha[1] not in lista_frutas:
            
            lista_frutas.append(linha[1])

            lista_maior_preco.append(float(linha[2]))

            lista_menor_preco.append(float(linha[2]))

            lista_qtd_frutas.append(1)
    
            lista_valor_total_frutas.append(float(linha[2]))

            lista_media_preco_frutas.append(0)
            
            lista_valor_frutas.append(float(linha[2]))   

            lista_qtd_fruta_acima_media.append(0)   
        else:
            
            # encontrado a fruta que foi repetido
            index_fruta = lista_frutas.index(linha[1])
            
            VerificaValorTotalFruta(index_fruta)
            
            # Verificando o maior valor das frutas
            verificaMaiorValorFruta(float(linha[2]), linha[1], index_fruta)

            # Verificando o menor valor das frutas
            verificaMenorValorFruta(float(linha[2]), linha[1], index_fruta)
            
            # Verificando a qtd de frutas que foram repitidas
            verificaQuantidadeFruta(index_fruta)
            
            # Verificando a media de preços das frutas
            verificaMediaFruta(index_fruta)

            #Verificando a qtd de frutas que estão acima da media
            # Não consegui fazer ...
                 
    cursor += 1

arquivo.close()

# Pegando o arquivo utilizando o caminho absuluto
try:
    arquivo2 = open("./aula03/cadastro_produtosV1.csv")
except:
    print("Falha ao encontrar o arquivo.")
    exit()
       
# Colocando todas as informações do arquivo na variavel
linhas2 = csv.reader(arquivo2)

for linha2 in linhas2:
    
    if cursor > 0:
        
        pass
    
    
    cursor += 1
    
# print(lista_frutas[13])

# print(lista_maior_preco[13])

# print(lista_menor_preco[13])

# print(lista_qtd_frutas[13])

# print(lista_valor_total_frutas[13])

# print(lista_media_preco_frutas[13])

# print(lista_qtd_fruta_acima_media[13])
    

    
