# views/developer_2.py
import streamlit as st

class Carlos:
    def __init__(self):
        # Informações do desenvolvedor
        self.name = "Carlos Moura"
        self.image_path = "./assets/carlos.jpg" 
        self.email = "carlosmourapires88@gmail.com" 
        self.description = (
            "Sou formado em Direito e atualmente estou em transição de carreira para a área de tecnologia. "
            "Atualmente estou fazendo o curso na Alpha EdTech e atuando como estagiário na CloudWalk"
            "onde atuo na área de inteligência artificial. Aproveito a chance de aplicar minha visão analítica "
            "e habilidades críticas do Direito em um contexto técnico, desenvolvendo novas competências para resolver problemas complexos. "
            "Meu foco atual é fortalecer minha base técnica e entender a dinâmica de trabalho colaborativo entre diferentes equipes e projetos."
        ) 
        self.experiences = (
            """
            - Estágio em Inteligência Artificial na Cloudwalk, com foco em aplicação de modelos e análise de dados
            - Formação em Direito, trazendo uma visão analítica e detalhista para a área de tecnologia
            - Em formação pela Alpha EdTech, onde desenvolvo habilidades técnicas voltadas para Ciência de Dados e Inteligência Artificial com Python
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
