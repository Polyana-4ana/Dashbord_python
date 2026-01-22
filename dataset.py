import json
import pandas as pd

# lendo o arquivo json
with open('dados/vendas.json', encoding='utf-8') as file:
    data = json.load(file)

# criando dataframe
df = pd.DataFrame(data)

# convertendo datas de forma segura
df['Data da Compra'] = pd.to_datetime(
    df['Data da Compra'],
    dayfirst=True,
    errors='coerce'
)
