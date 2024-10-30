import streamlit as st
from models.model_elevations import (
    train_knn,
    train_svm,
    hyperparameter_tuning_knn,
    hyperparameter_tuning_svm
)
from services.data_processing import process_data

def select_model(train_data, test_data, model_selection):
    # Exibir o modelo selecionado
    st.subheader(f"Modelo Selecionado: {model_selection}")

    # Processar os dados de treinamento e teste
    X_train_scaled, y_train, X_test_scaled, y_test = process_data(train_data, test_data, target_column='y')

    # Seleção do modelo KNN
    if model_selection == "KNN":
        n_neighbors = st.number_input("Número de Vizinhos (k):", min_value=1, max_value=20, value=5)
        
        # Botão para treinar o modelo KNN
        if st.button("Treinar KNN"):
            train_knn(X_train_scaled, y_train, X_test_scaled, y_test, n_neighbors)

        # Botão para otimizar hiperparâmetros do KNN
        if st.button("Otimizar Hiperparâmetros KNN"):
            hyperparameter_tuning_knn(X_train_scaled, y_train)

    # Seleção do modelo SVM
    elif model_selection == "SVM":
        C = st.number_input("Valor de C:", min_value=0.01, max_value=10.0, value=1.0)
        kernel = st.selectbox("Kernel:", ["linear", "rbf", "poly"])
        
        # Botão para treinar o modelo SVM
        if st.button("Treinar SVM"):
            train_svm(X_train_scaled, y_train, X_test_scaled, y_test, C, kernel)

        # Botão para otimizar hiperparâmetros do SVM
        if st.button("Otimizar Hiperparâmetros SVM"):
            hyperparameter_tuning_svm(X_train_scaled, y_train)
