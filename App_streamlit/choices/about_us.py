import streamlit as st
from views.developer_1 import JoseMario 
from views.developer_2 import Carlos 
from views.developer_3 import Djulie 
from views.developer_4 import Andre 
from views.developer_5 import Joao
from views.developer_6 import Gabriel

def about_us():
    st.title("Sobre Nós")
    st.write("Aqui estão algumas informações sobre os desenvolvedores deste projeto...")
    # Exibe a escolha de desenvolvedores
    developer_selected = st.selectbox("Escolha um desenvolvedor:", ["José Mário", "Carlos Moura", "Djullie Caroline", "André Gloos", "João Pedro", "Gabriel Freire"])

    # Lógica para inicializar a classe correspondente
    if developer_selected == "José Mário":
        about_me = JoseMario() 
        about_me.run()

    elif developer_selected == "Carlos Moura":
        about_me = Carlos()
        about_me.run() 

    elif developer_selected == "Djullie Caroline":
        about_me = Djulie()
        about_me.run() 

    elif developer_selected == "André Gloos":
        about_me = Andre()
        about_me.run() 

    elif developer_selected == "João Pedro":
        about_me = Joao()
        about_me.run() 

    elif developer_selected == "Gabriel Freire":
        about_me = Gabriel()
        about_me.run()