# views/developer_2.py
import streamlit as st

class Gabriel:
    def __init__(self):
        # Informações do desenvolvedor
        self.name = "Gabriel Freire"
        self.image_path = "./assets/gabriel_freire.png"
        self.email = "gabriel0591@hotmail.com"
        self.description = (
            "Sou formado em Engenharia de Produção."
            "Estudo na Alpha EdTech e adquiro experiência prática na Cloudwalk, atuando no Mobile Team na área de Account - Banking."
            "Meu foco é expandir conhecimentos técnicos e fortalecer a colaboração entre equipes e projetos."
        )
        self.experiences = (
            """
            - Desenvolvedor Mobile na Cloudwalk, atuando no time de Account - Banking
            - Formação em Engenharia de Produção, trazendo uma visão integrada entre processos de engenharia e tecnologia
            - Em formação pela Alpha EdTech, com foco no desenvolvimento de habilidades técnicas e práticas em Ciência de Dados com Python
            """
        )

    def display(self):
        col1, col2 = st.columns(2, gap='small', vertical_alignment='center')

        with col1:
            st.image(self.image_path, width=230)

        with col2:
            st.title(self.name, anchor=False)
            st.write(self.description)
            st.write(f"**Email:** {self.email}")  # Exibindo o e-mail

        st.markdown("---")

        st.subheader('Experiências e Qualificações', anchor=False)
        st.write(self.experiences)

    def run(self):
        self.display()
