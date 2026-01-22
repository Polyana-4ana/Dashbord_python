import json
import pandas as pd

# lendo o arquivo json corretamente
with open('dados/vendas.json', encoding='utf-8') as file:
    data = json.load(file)

# criando dataframe
df = pd.DataFrame.from_dict(data)

# convertendo a coluna de data
df['Data da Compra'] = pd.to_datetime(
    df['Data da Compra'],
    format='%d/%m/%y'
)
