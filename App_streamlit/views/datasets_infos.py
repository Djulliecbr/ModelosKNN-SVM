import pandas as pd
import streamlit as st

def datasets_info(df):
    # Configuração da barra lateral para selecionar colunas
    st.sidebar.header("Selecionar Colunas para Visualização")
    selected_columns = st.sidebar.multiselect("Escolha as colunas que deseja visualizar:", df.columns)

    # Exibir cabeçalho e informações do DataFrame filtrado
    if selected_columns:
        st.subheader("Dados Selecionados")
        st.dataframe(df[selected_columns].head())
    else:
        st.write("Nenhuma coluna selecionada para visualização.")
        st.dataframe(df.head())

    st.markdown("---")

    # Exibir informações sobre as colunas
    st.subheader("Informações sobre as Colunas")
    st.write(df.describe())  # Estatísticas descritivas

    st.markdown("---")

    # Colunas lado a lado para "Análise de Dataset" e "Colunas com Valores Nulos"
    col1, col2 = st.columns(2, gap='small', vertical_alignment='bottom')

    with col1:
        st.subheader("Colunas com Valores NaN")
        null_columns = df.isnull().sum()
        st.write(null_columns[null_columns > 0])

    with col2:
        st.subheader("Análise de Dataset")
        # Resumo do DataFrame para visualização compacta
        info_buffer = pd.DataFrame({
            'Coluna': df.columns,
            'Tipo': df.dtypes.astype(str),  # Converte os tipos para string
            'Não Nulos': df.notnull().sum(),
            'Nulos': df.isnull().sum(),
            'Exemplo': [df[col].sample(1).values[0] for col in df.columns]
        })
        st.dataframe(info_buffer)