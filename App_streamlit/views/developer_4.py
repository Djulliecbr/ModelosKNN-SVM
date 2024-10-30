# views/developer_2.py
import streamlit as st

class Andre:
    def __init__(self):
        # Informações do desenvolvedor
        self.name = "André Gloos"
        self.image_path = "./assets/andre.jpg"
        self.email = "andrehenriquegloos@gmail.com"  # Adicionando o e-mail
        self.description = (
            "Atualmente, estou desenvolvendo minha carreira com foco em banco de dados e backend. "
            "Tenho conhecimento em SQL e Python, com ênfase na manipulação e no gerenciamento de dados. "
            "No momento, trabalho na área de Monitoring, onde monitoro produtos. Minha função envolve o uso de bancos de dados "
            "para criar alertas, analisar dados e garantir que o desempenho e a segurança dos produtos estejam sempre adequados."
        )

        self.experiences = (
            """
            - Conhecimento em banco de dados, especialmente em SQL, com foco na manipulação e gerenciamento de dados
            - Experiência em backend utilizando Python, sempre buscando seguir boas práticas de desenvolvimento
            - Trabalho na área de Monitoring, onde sou responsável por monitorar produtos, garantindo que eles funcionem de maneira eficiente e segura
            - Criação de alertas e análise de dados para ajudar na identificação de problemas e melhorias no desempenho dos sistemas
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
