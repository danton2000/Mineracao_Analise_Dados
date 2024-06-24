# Importando a biblioteca do pandas, para utilizar suas funções
import pandas as pd
# EXTRAÇÃO
#Colocando o endereço da base que será utilizada e tratada em uma variavel
# Essa  base contem as estatisticas dos jogadores entre os anos 2016 a 2020
url = 'https://raw.githubusercontent.com/danton2000/Mineracao_Analise_Dados/main/datasets/Data.csv'

# Ler o csv e criando um data frame
dataframe = pd.read_csv(url)

# Imprimindo os dados
#print(dataframe['Player Names'])
# TRANSFORMAÇÃO
# Ordenando o dataframe pela coluna 'Goals'(quantidade de gols marcados)
dataframeordenado = dataframe.sort_values(by='Goals', ascending=False)

# Pegando os 10 jogadores que mais marcaram gols 
goleadores = dataframeordenado[['Player Names', 'Club', 'Goals', 'Year']].head(10)

# CARREGAMENTO
# Salvando e criando um arquivo com informações de um outro arquivo .csv
output_file_path = 'exercicio04/top_10_goleadores_2016_2020.csv'
goleadores.to_csv(output_file_path, index=False)
