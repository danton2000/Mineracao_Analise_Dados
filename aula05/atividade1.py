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
#coluna 2 = Staus
#coluna 3 = Tipo
       
# Colocando todas as informações do arquivo na variavel
linhas = csv.reader(arquivo)

# Variaveis de inicialização
lista_pessoa_juridica = []
lista_pessoa_fisica = []
lista_pessoa_fisica_porcetagem = []
lista_pessoa_juridica_porcetagem = []
cursor = 0

for linha in linhas:

    if cursor > 0:
        
        if linha[3] == 'Pessoa Física':
            
            if linha[2] == 'Ativo':
                lista_pessoa_fisica.append(['PF', 1])
            else:
                lista_pessoa_fisica.append(['PF', 0])

        else:
            if linha[2] == 'Ativo':
                lista_pessoa_juridica.append(['PJ', 1])
            else:
                lista_pessoa_juridica.append(['PJ', 0])      
                
       
                 
    cursor += 1

arquivo.close()

print(len(lista_pessoa_fisica))
#245

soma_ativo = 0

soma_inativo = 0
for x in lista_pessoa_fisica:
    
    # Pessoas ativos
    if x[1] == 1:
        
        #print(x)

        #128 pessoas ativos fisico
        soma_ativo+=1

    if x[1] == 0:
        
        #print(x)

        #117 pessoas inativo fisico
        soma_inativo+=1
        

porcentagem_ativo = soma_ativo * 100 / len(lista_pessoa_fisica)

porcentagem_ativo = round(porcentagem_ativo,2)

porcentagem_inativo = soma_inativo * 100 / len(lista_pessoa_fisica)

porcentagem_inativo = round(porcentagem_inativo,2)

lista_pessoa_fisica_porcetagem = [porcentagem_ativo, porcentagem_inativo]

print(lista_pessoa_fisica_porcetagem)

soma_ativo = 0
soma_inativo = 0

for x in lista_pessoa_juridica:
    
    # Pessoas ativos
    if x[1] == 1:
        
        #print(x)

        #126 pessoas ativos juridica
        soma_ativo+=1

    if x[1] == 0:
        
        #print(x)

        #126 pessoas inativo juridica
        soma_inativo+=1


porcentagem_ativo = soma_ativo * 100 / len(lista_pessoa_juridica)

porcentagem_ativo = round(porcentagem_ativo,2)

porcentagem_inativo = soma_inativo * 100 / len(lista_pessoa_juridica)

porcentagem_inativo = round(porcentagem_inativo,2)

lista_pessoa_juridica_porcetagem = [porcentagem_ativo, porcentagem_inativo]

# Abrir o arquivo para escrita ('w' indica que o arquivo será aberto para escrita)
with open("basePercentualPessoas.txt", "w") as arquivo:
    # Escrever no arquivo
    arquivo.write(f"{lista_pessoa_fisica_porcetagem}\n")
    arquivo.write(f"{lista_pessoa_juridica_porcetagem}\n")

print("Texto escrito com sucesso no arquivo.")
    

    
