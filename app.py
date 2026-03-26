import streamlit as st
import google.generativeai as genai
from PIL import Image

# 1. Configuración de Llave (Desde Secrets)
api_key = st.secrets.get("GEMINI_API_KEY")

# 2. Configuración del Modelo (EL CEREBRO GRATUITO)
if api_key:
    genai.configure(api_key=api_key)
    # Cambiamos el nombre del modelo a la versión más universal
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    st.error("Falta la llave GEMINI_API_KEY en Secrets.")

# 3. Interfaz Básica para probar
st.title("PROKONECTA OS - TEST")
img_file = st.file_uploader("Sube una foto para probar a Jarvis", type=['jpg', 'png', 'jpeg'])

if img_file and st.button("ANALIZAR"):
    img = Image.open(img_file)
    response = model.generate_content(["Analiza esta imagen de forma breve.", img])
    st.write(response.text)
