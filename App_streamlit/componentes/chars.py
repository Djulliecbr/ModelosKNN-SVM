import streamlit as st
import plotly.express as px
from sklearn.metrics import confusion_matrix
import plotly.graph_objects as go

def correlation_target(data):
    # Calcular a correlação com a coluna target 'y'
    if 'y' in data.columns:
        correlation = data.corr()['y'].drop('y')
        correlation_df = correlation.reset_index()
        correlation_df.columns = ['Feature', 'Correlation']
        
        # Criar gráfico de barras para a correlação
        fig_corr = px.bar(correlation_df, x='Feature', y='Correlation', 
                          title='Correlação das Features com a Coluna Target (y)',
                          labels={'Correlation': 'Correlação', 'Feature': 'Características'},
                          color='Correlation',
                          color_continuous_scale=px.colors.sequential.Viridis)
        st.plotly_chart(fig_corr)

def positive_features(data):
    # Calcular a correlação com a coluna target 'y'
    if 'y' in data.columns:
        correlation = data.corr()['y'].drop('y')
        correlation_df = correlation.reset_index()
        correlation_df.columns = ['Feature', 'Correlation']
        
        # Ordenar o DataFrame pelas correlações
        correlation_df = correlation_df.sort_values(by='Correlation', ascending=False)

        # Selecionar as 10 features com maior correlação
        top_10_positive = correlation_df.head(10)

        # Criar gráfico de barras para a correlação
        fig_corr = px.bar(top_10_positive, x='Feature', y='Correlation', 
                          title='Top 10 Features com Maior Correlação com (y)',
                          labels={'Correlation': 'Correlação', 'Feature': 'Características'},
                          color='Correlation',
                          color_continuous_scale=px.colors.sequential.Viridis)
        return fig_corr  # Retorna a figura em vez de exibir

def negative_features(data):
    # Calcular a correlação com a coluna target 'y'
    if 'y' in data.columns:
        correlation = data.corr()['y'].drop('y')
        correlation_df = correlation.reset_index()
        correlation_df.columns = ['Feature', 'Correlation']
        
        # Ordenar o DataFrame pelas correlações
        correlation_df = correlation_df.sort_values(by='Correlation')

        # Selecionar as 10 features com menor correlação
        top_10_negative = correlation_df.head(10)

        # Criar gráfico de barras para a correlação
        fig_corr_neg = px.bar(top_10_negative, x='Feature', y='Correlation', 
                              title='Top 10 Features com Menor Correlação com (y)',
                              labels={'Correlation': 'Correlação', 'Feature': 'Características'},
                              color='Correlation',
                              color_continuous_scale=px.colors.sequential.Viridis)
        return fig_corr_neg  # Retorna a figura em vez de exibir
    
def plot_confusion_matrix(y_test, y_pred):
    cm = confusion_matrix(y_test, y_pred)
    labels = ["Classe 0", "Classe 1"]
    
    # Criar a matriz de confusão com Plotly
    fig = go.Figure(data=go.Heatmap(
        z=cm,
        x=labels,
        y=labels,
        colorscale="Blues",
        showscale=True,
        text=cm,
        texttemplate="%{text}",
    ))
    
    # Configurar rótulos e título
    fig.update_layout(
        title="Matriz de Confusão",
        xaxis=dict(title="Predito"),
        yaxis=dict(title="Verdadeiro")
    )
    
    # Exibir a figura no Streamlit
    st.plotly_chart(fig)