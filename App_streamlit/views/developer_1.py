import streamlit as st

class JoseMario:
    def __init__(self):
        # Informações do desenvolvedor
        # Conteúdo da página Home
        self.name = "José Mário"
        self.image_path = "./assets/jose_mario.jpg"
        self.email = "jmariosjunior2000@gmail.com"  # Adicionando o e-mail
        self.description = (
            "Atualmente, desenvolvo minha carreira como Full Stack, com sólida experiência pelo Instituto Alpha EdTech, "
            "onde atualmente faço estágio."
            "Tenho um forte domínio em bancos de dados, especialmente SQL, e sou movido pela colaboração e integração em projetos em equipe, "
            "onde a troca de conhecimentos e a sinergia de ideias são fundamentais para alcançar resultados eficientes e inovadores."
            "Estou sempre em busca de novos conhecimentos e expandi-lo porque eu acredito que não há limites para o estudo."
        )
        self.experiences = (
            """
            - Estágio em desenvolvimento Full Stack e QA no instituto Alpha EdTech
            - Forte conhecimento em banco de dados, com ênfase em SQL, e bancos relacionais, como MySQL, SQLite e Postgres
            - Profissional colaborativo com alto valor no trabalho em equipe, visando o sucesso coletivo em cada projeto
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
