# views/developer_2.py
import streamlit as st

class Joao:
    def __init__(self):
        self.name = "João Pedro"
        self.image_path = "./assets/joao_marques.jpg"
        self.email = "joaofmarques.dev@gmail.com"
        self.description = (
            "Sou formado em administração e atualmente mergulho no mundo da tecnologia. "
            "Estou cursando na Alpha EdTech e ganhando experiência prática como estagiário na Cloudwalk, "
            "onde atuo no time de SRE. Gosto de encarar novos desafios e unir o que aprendi na administração "
            "com a área de infraestrutura e confiabilidade de sistemas. No momento, busco expandir meu conhecimento, "
            "explorando tanto o lado técnico quanto as interações entre times e projetos."
        )
        self.experiences = (
            """
            - Estágio em SRE na Cloudwalk, com foco em monitoramento e manutenção de infraestrutura
            - Formação em administração, trazendo uma visão ampla e estratégica para a tecnologia
            - Em formação pela Alpha EdTech, onde exploro conhecimentos técnicos em focados em Ciência de dados com Python
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
