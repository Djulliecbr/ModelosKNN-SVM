import streamlit as st
from componentes.chars import correlation_target, positive_features, negative_features

def dashboard(data):
    st.title("Dashboard")

    if data is not None:
        # Cálculo das métricas
        total_dados = data.shape[0] * data.shape[1]  # Número total de dados
        media_valores = data.mean().mean()  # Média de todos os valores
        total_nan = data.isna().sum().sum()  # Total de valores NaN

        # Exibir as métricas em três colunas
        col1, col2, col3 = st.columns(3, gap="large")
        with col1:
            st.info("📊 Total de Dados")  # Emoji de gráfico de barras
            st.metric(label="Total de Dados", value=f"{total_dados}", label_visibility="collapsed")

        with col2:
            st.info("📈 Média dos Valores")  # Emoji de gráfico de linha
            st.metric(label="Média dos Valores", value=f"{media_valores:.2f}", label_visibility="collapsed")

        with col3:
            st.info("⚠️ Total de NaN")  # Emoji de alerta
            st.metric(label="Total de NaN", value=f"{total_nan}", label_visibility="collapsed")
            
        st.markdown("---")

        # Exibir gráficos de correlação
        correlation_target(data)
        
        fig_pos = positive_features(data)
        fig_neg = negative_features(data)

        st.markdown("---")

        # Exibir gráficos lado a lado
        col1, col2 = st.columns(2)
        with col1:
            st.plotly_chart(fig_pos)
        with col2:
            st.plotly_chart(fig_neg)

    else:
        st.write("Nenhum dado disponível para exibir.")

