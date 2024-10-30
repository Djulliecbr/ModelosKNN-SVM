import streamlit as st
from sklearn.preprocessing import StandardScaler

def sync_columns(train_df, test_df):
    """Sincroniza as colunas de train_df e test_df para garantir que tenham as mesmas colunas."""
    common_columns = train_df.columns.intersection(test_df.columns)
    return train_df[common_columns], test_df[common_columns]

def process_data(train_df, test_df, target_column='y'):
    # Exibir número de linhas antes da remoção de valores ausentes
    st.write("Número de linhas do conjunto de treino antes de remover valores ausentes:", train_df.shape[0])
    st.write("Número de linhas do conjunto de teste antes de remover valores ausentes:", test_df.shape[0])

    # Calcular a porcentagem de valores ausentes
    missing_values_percentage = train_df.isnull().mean() * 100

    # Remover colunas com mais de 50% de valores ausentes (com base na primeira análise)
    columns_to_drop = missing_values_percentage[missing_values_percentage > 50].index
    
    # Inicializar os DataFrames limpos como cópias dos originais
    train_df_cleaned = train_df.drop(columns=columns_to_drop, errors='ignore')
    test_df_cleaned = test_df.drop(columns=columns_to_drop, errors='ignore')

    # Exibir número de colunas após a remoção de colunas com muitos valores ausentes
    st.write("Número de colunas após remover valores ausentes do dataset de treino:", train_df_cleaned.shape[1])
    st.write("Número de colunas após remover valores ausentes do dataset de teste:", test_df_cleaned.shape[1])

    # Mostrar colunas removidas
    st.write("Colunas removidas no conjunto de treino:", columns_to_drop)

    # Preencher valores ausentes nas colunas restantes com a mediana de cada coluna
    train_df_cleaned = train_df_cleaned.fillna(train_df_cleaned.median())
    test_df_cleaned = test_df_cleaned.fillna(test_df_cleaned.median())

    # Sincronizar colunas após o pré-processamento
    train_df_cleaned, test_df_cleaned = sync_columns(train_df_cleaned, test_df_cleaned)

    # Separar features (X) e rótulo (y)
    X_train = train_df_cleaned.drop(columns=[target_column])
    y_train = train_df_cleaned[target_column]
    X_test = test_df_cleaned.drop(columns=[target_column])
    y_test = test_df_cleaned[target_column]

    # Normalizar os dados (StandardScaler para padronização)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    return X_train_scaled, y_train, X_test_scaled, y_test
