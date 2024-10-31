import streamlit as st
from services.data_loader import load_datasets
from choices.about_us import about_us
from choices.dashboard import dashboard
from choices.infos import infos
from choices.models import select_model
from services.icon_load import load_icon

icon_base64 = load_icon()

# Configuração da Página
def configure_page(icon_base64):
    st.set_page_config(
        page_title="Online Analytics",
        page_icon=f"data:image/png;base64,{icon_base64}",
        layout="wide"
    )

# Função para criar a barra lateral
def create_sidebar():
    st.markdown(
        """
        <style>
        .sidebar-title {
            font-size: 36px;
            color: #007BFF;
            text-align: center;
            margin: 0;
            padding: 20px 0;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    with st.sidebar:
        st.sidebar.image("./assets/6951531.png")
        st.sidebar.markdown("<h1 class='sidebar-title'>Online Analytics</h1>", unsafe_allow_html=True) 
        selected = st.sidebar.radio("Escolha uma opção:", ["Dashboard", "Sobre nós", "Informações Dataset", "Modelos"])
        
        model_selection = None
        if selected == "Modelos":
            model_selection = st.sidebar.radio("Selecione o Modelo:", ["KNN", "SVM"])
        
    return selected, model_selection

# Função principal
def main():
    configure_page(icon_base64)
    selected, model_selection = create_sidebar()

    # Carregar datasets de treino e teste se a seleção não for "Sobre nós"
    train_data, test_data = (None, None)
    if selected != "Sobre nós":
        sample_option = st.selectbox("Selecione a quantidade de dados:", ["Todos", "Amostra personalizada"])
        sample_size = 100  # Valor padrão para amostra personalizada

        if sample_option == "Amostra personalizada":
            sample_size = st.number_input("Quantidade de linhas:", min_value=1000, value=1000)

        train_data, test_data = load_datasets("./data/train.csv", "./data/test.csv", sample_option, sample_size)

    # Funções das Páginas
    if selected == "Dashboard":
        dashboard(train_data)

    elif selected == "Sobre nós":
        about_us()

    elif selected == "Informações Dataset":
        infos(train_data, test_data)

    elif selected == "Modelos" and model_selection:
        select_model(train_data, test_data, model_selection)

# Execução do script
if __name__ == "__main__":
    main()
