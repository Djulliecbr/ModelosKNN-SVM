# views/developer_2.py
import streamlit as st

class Djulie:
    def __init__(self):
        # Informações do desenvolvedor
        self.name = "Djullie Caroline"
        self.image_path = "./assets/djullie_caroline.jpg"
        self.email = "djulliecbr@gmail.com"
        self.description = (
            "Sou advogada, bacharel em Direito e atualmente iniciando na área de tecnologia "
            "Estou cursando ciência de dados na Alpha EdTech e ganhando experiência prática como estagiária na Cloudwalk, "
            "onde atuo no time de Compliance e Risco. Sou apaixonada pelo problema, pelas leis e por tecnologia. Gosto de me desafiar e juntar tudo o que aprendi ao longo da vida"
            "com a área regulatória de risco consigo juntar o direito e a tecnologia para automatizar os sistemas financeiros da empresa. No momento, busco me especializar mais nessa área "
            "explorando tanto o lado técnico quanto as interações entre times e projetos."
        )
        self.experiences = (
            """
            - Estágio em Compliance e Risco na Cloudwalk, com foco em regulamentação e LLM.
            - Formação em direito, trazendo uma visão ampla e estratégica para a tecnologia
            - Em formação pela Alpha EdTech, onde exploro conhecimentos técnicos focados em Ciência de dados com Python
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
