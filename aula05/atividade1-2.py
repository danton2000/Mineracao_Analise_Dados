# Importa a lib para utilizar e manipular arquivos .CSV
import csv

# Pegando o arquivo utilizando o caminho absuluto
try:
    arquivo = open("./aula05/base_clientes.csv")
except:
    print("Falha ao encontrar o arquivo.")
    exit()

#coluna 0 = codigo
#coluna 1 = Nome
#coluna 2 = Status
#coluna 3 = Tipo
       
# Colocando todas as informações do arquivo na variavel
linhas = csv.reader(arquivo)

# Variaveis de inicialização
lista_tipo_inativo = []
lista_tipo_ativo = []
lista_tipo_ativo_porcetagem = []
lista_tipo_inativo_porcetagem = []
cursor = 0

for linha in linhas:

    if cursor > 0:
        
        if linha[2] == 'Ativo':
            
            if linha[3] == 'Pessoa Física':
                lista_tipo_ativo.append([1, 'PF'])
            else:
                lista_tipo_ativo.append([1, 'PJ'])

        else:
            if linha[3] == 'Pessoa Física':
                lista_tipo_inativo.append([0, 'PF'])
            else:
                lista_tipo_inativo.append([0, 'PJ'])             
    cursor += 1

arquivo.close()

soma_pessoa_f = 0

soma_pessoa_j = 0
for x in lista_tipo_ativo:
    
    # Pessoas ativos
    if x[1] == 'PF':
        
        #print(x)

        #128 pessoas ativos fisico
        soma_pessoa_f+=1

    if x[1] == 'PJ':
        
        #print(x)

        #117 pessoas inativo fisico
        soma_pessoa_j+=1

porcentagem_pessoa_fisico = soma_pessoa_f * 100 / len(lista_tipo_ativo)

porcentagem_pessoa_fisico = round(porcentagem_pessoa_fisico,2)

porcentagem_juridico = soma_pessoa_j * 100 / len(lista_tipo_ativo)

porcentagem_juridico = round(porcentagem_juridico,2)

lista_tipo_ativo_porcetagem = [porcentagem_pessoa_fisico, porcentagem_juridico]

print(lista_tipo_ativo_porcetagem)

soma_pessoa_f = 0

soma_pessoa_j = 0
for x in lista_tipo_inativo:
    
    # Pessoas ativos
    if x[1] == 'PF':
        
        #print(x)

        #128 pessoas ativos fisico
        soma_pessoa_f+=1

    if x[1] == 'PJ':
        
        #print(x)

        #117 pessoas inativo fisico
        soma_pessoa_j+=1
        

porcentagem_pessoa_fisico = soma_pessoa_f * 100 / len(lista_tipo_inativo)

porcentagem_pessoa_fisico = round(porcentagem_pessoa_fisico,2)

porcentagem_juridico = soma_pessoa_j * 100 / len(lista_tipo_inativo)

porcentagem_juridico = round(porcentagem_juridico,2)

lista_tipo_inativo_porcetagem = [porcentagem_pessoa_fisico, porcentagem_juridico]

print(lista_tipo_inativo_porcetagem)

# Abrir o arquivo para escrita ('w' indica que o arquivo será aberto para escrita)
with open("basePercentualTipos.txt", "w") as arquivo:
    # Escrever no arquivo
    arquivo.write(f"{lista_tipo_ativo_porcetagem}\n")
    arquivo.write(f"{lista_tipo_inativo_porcetagem}\n")

print("Texto escrito com sucesso no arquivo.")