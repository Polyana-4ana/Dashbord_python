import plotly.express as px
from utils import df_receita_estado, df_receita_mensal, df_receita_categoria, df_vendedor

# graficos de mapa scatter_geo
grafico_map_estado = px.scatter_geo(

    df_receita_estado,
    lat = 'lat',
    lon = 'lon',
    scope = 'south america',
    size = 'Preço',
    template = 'seaborn',
    hover_name = 'Local da compra',
    hover_data = {'lat': False, 'lon': False},
    title= 'Receita por Estados:'

)

#grafico de linha
grafico_receita_mensal = px.line(
    df_receita_mensal,
    x = 'Mes',
    y = 'Preço',
    markers= True,
    range_y = (0, df_receita_mensal.max()),
    color = 'Ano',
    line_dash= 'Ano',
    title = 'Receita mensal'

)

grafico_receita_mensal.update_layout(yaxis_title = 'Receita' )

grafico_receita_estado = px.bar(
    df_receita_estado.head(7),
    x = 'Local da compra',
    y = 'Preço',
    text_auto= True,
    title= 'Top 7  maiores receitas por Estados'
)

grafico_receita_categoria = px.bar(
    df_receita_categoria.head(7),
    text_auto= True,
    title='Top 7 categorias com maior receita'
)

grafico_receita_vendedores = px.bar(
    df_vendedor[['sum']].sort_values('sum', ascending= False).head(7),
    x = 'sum',
    y = df_vendedor[['sum']].sort_values('sum', ascending= False).head(7).index,
    text_auto= True,
    title='Top 7 vendedores por receita'
)

grafico_vendas_por_vendedor = px.bar(
    df_vendedor[['count']].sort_values('count', ascending=False).head(7),
    x = 'count',
    y = df_vendedor[['count']].sort_values('count', ascending=False).head(7).index,
    text_auto= True,
    title= 'Top 7 vendedores por venda'
)