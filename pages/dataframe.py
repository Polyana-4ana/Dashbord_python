import streamlit as st
import pandas as pd
from dataset import df
from utils import convert_csv, mensagem_sucesso

st.title('Dataset de vendas')

df['Data da Compra'] = pd.to_datetime(df['Data da Compra'], format='%d/%m/%Y')

with st.sidebar.form(key='form_filtros'):

    st.subheader('Filtros')

    categorias = st.multiselect(
        'Categoria do Produto',
        df['Categoria do Produto'].unique()
    )

    preco = st.slider(
        'Preço do Produto',
        int(df['Preço'].min()),
        int(df['Preço'].max()),
        (int(df['Preço'].min()), int(df['Preço'].max()))
    )

    data_compra = st.date_input(
        'Data da Compra',
        (df['Data da Compra'].min(), df['Data da Compra'].max())
    )

    colunas = st.multiselect(
        'Colunas',
        list(df.columns),
        list(df.columns)
    )

    botao_pesquisar = st.form_submit_button('Pesquisar 🔍')

filtro_dados = df.copy()

if botao_pesquisar:

    if categorias:
        filtro_dados = filtro_dados[
            filtro_dados['Categoria do Produto'].isin(categorias)
        ]

    filtro_dados = filtro_dados[
        (filtro_dados['Preço'] >= preco[0]) &
        (filtro_dados['Preço'] <= preco[1])
    ]

    filtro_dados = filtro_dados[
        (filtro_dados['Data da Compra'] >= pd.to_datetime(data_compra[0])) &
        (filtro_dados['Data da Compra'] <= pd.to_datetime(data_compra[1]))
    ]

    filtro_dados = filtro_dados[colunas]

st.dataframe(filtro_dados)

st.markdown(
    f'A tabela possui :blue[{filtro_dados.shape[0]}] linhas e '
    f':blue[{filtro_dados.shape[1]}] colunas'
)

coluna1, coluna2 = st.columns(2)

with coluna1:
    nome_arquivo = st.text_input('', label_visibility='collapsed')
    nome_arquivo += '.csv'

with coluna2:
    st.download_button(
        'Baixar arquivo',
        data=convert_csv(filtro_dados),
        file_name=nome_arquivo,
        mime='text/csv',
        on_click=mensagem_sucesso
    )
