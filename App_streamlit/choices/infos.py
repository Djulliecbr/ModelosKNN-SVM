import streamlit as st

def infos(train_data, test_data):
    st.title("Informações do Dataset")
    dataset_choice = st.selectbox("Escolha o dataset para visualizar:", ["Treino", "Teste"])
    
    if dataset_choice == "Treino":
        st.write(train_data)
    else:
        st.write(test_data)