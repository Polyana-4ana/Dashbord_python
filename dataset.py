import json
import pandas as pd


# fazendo o python ler o arquivo json
file = open('dados/vendas.json')
data = json.load(file)

#print(data)

#criando dataframe baseado em dicionario
df = pd.DataFrame.from_dict(data)

print(df)

file.close()