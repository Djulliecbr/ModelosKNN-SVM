import streamlit as st
from PIL import Image
import base64

# Carregamento do Ícone
def load_icon():
    icon_path = "./assets/6951531.png"

    try:
        icon = Image.open(icon_path)
    except FileNotFoundError:
        st.error(f"Arquivo não encontrado: {icon_path}")
        raise

    # Converter a imagem para base64
    with open(icon_path, "rb") as image_file:
        icon_base64 = base64.b64encode(image_file.read()).decode()

    return icon_base64