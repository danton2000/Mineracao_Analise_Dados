# Importa a lib para utilizar e manipular arquivos .CSV
import csv

# Pegando o arquivo utilizando o caminho absuluto
arquivo = open("C:/Users/181810032/Desktop/Mineracao_Analise_Dados/aula02/cadastro_produtosV1.csv")

# Colocando todas as informações do arquivo na variavel
linhas = csv.reader(arquivo)

# Percorrendo a lista de linhas e mostrando uma linha em um loop
# for linha in linhas:

#     print(linha)

# Adaptar o código de leitura do Python para listar as linhas com o valor superior a R$ 400,00

cursor = 0

for linha in linhas:

    if cursor > 0:
        valor_formatado = float(linha[2])

        if(valor_formatado > 400):
            print(f"{linha[0], linha[1], valor_formatado}")

    cursor += 1

    
