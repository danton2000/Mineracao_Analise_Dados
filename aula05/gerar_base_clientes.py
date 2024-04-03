import csv
import random

# Lista de nomes para os clientes
nomes = ['João', 'Maria', 'Pedro', 'Ana', 'Lucas', 'Carla', 'Fernanda', 'Marcos', 'Julia', 'Ricardo']

# Abre um arquivo CSV para escrita
with open('./aula04/base_clientes.csv', mode='w', newline='') as file:
    # Define os cabeçalhos do arquivo CSV
    headers = ['Código', 'Nome', 'Situação Cadastral', 'Classe']
    
    # Cria o objeto escritor do arquivo CSV
    writer = csv.writer(file)
    
    # Escreve os cabeçalhos no arquivo CSV
    writer.writerow(headers)
    
    # Escreve os dados dos clientes no arquivo CSV
    for i in range(500):
        codigo = i + 1
        nome = random.choice(nomes) + ' ' + random.choice(nomes)
        situacao_cadastral = random.choice(['Ativo', 'Inativo'])
        classe = random.choice(['Pessoa Jurídica', 'Pessoa Física'])
        
        # Escreve uma linha com os dados do cliente
        writer.writerow([codigo, nome, situacao_cadastral, classe])

print("Base de dados de clientes criada e salva com sucesso no arquivo 'base_clientes.csv'.")