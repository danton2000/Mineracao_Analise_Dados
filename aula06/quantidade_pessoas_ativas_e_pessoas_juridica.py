# Importa a lib para utilizar e manipular arquivos .CSV
import csv
from itertools import chain

# Pegando o arquivo utilizando o caminho absuluto
try:
    arquivo = open("./aula06/base_clientes.csv")
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
lista_pessoas_ativos = []
lista_pessoas_juridicas = []
cursor = 0

for linha in linhas:

    if cursor > 0:
        
        if linha[2] == 'Ativo':

            lista_pessoas_ativos.append(linha)

        if linha[3] == 'Pessoa Jurídica':

            lista_pessoas_juridicas.append(linha)  
                       
    cursor += 1
    
    #Saindo do laço ao encontrar os 125 clientes
    if cursor == 125:
        break

arquivo.close()

def encontrando_interceção(lista_pessoas_ativos, lista_pessoas_juridicas):
    
    conjunto_a = []
    conjunto_b = []
    interccao = []

    for x in lista_pessoas_ativos:
        conjunto_a.append(x[0])

    for y in lista_pessoas_juridicas:
        conjunto_b.append(y[0])

    """
    Esse código está criando uma lista chamada intersecção que contém os elementos 
    que estão presentes tanto no conjunto_a quanto no conjunto_b. Em seguida, 
    a lista intersecção é ordenada em ordem crescente.
    """
    for item in chain(conjunto_a, conjunto_b):
        if (item in conjunto_a) and (item in conjunto_b) and (item not in interccao):
            interccao.append(item)
    interccao.sort() 

    return len(interccao)
    # print(len(interccao))

quantidade_pessoas_ativas_e_pessoas_juridica = {
    "Ativo": len(lista_pessoas_ativos),
    "PJ": len(lista_pessoas_juridicas),
    "Ativos Intercção PJ": encontrando_interceção(lista_pessoas_ativos, lista_pessoas_juridicas)
}

print(quantidade_pessoas_ativas_e_pessoas_juridica)

    
