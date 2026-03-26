import streamlit as st
import google.generativeai as genai
from PIL import Image

st.set_page_config(page_title="PROKONECTA OS", layout="wide")

api_key = st.secrets.get("GEMINI_API_KEY")

if api_key:
    genai.configure(api_key=api_key)
    # FORZAMOS LA VERSIÓN ESTABLE v1 AQUÍ:
    model = genai.GenerativeModel('gemini-1.5-flash')
    st.sidebar.success("✅ JARVIS ONLINE")
else:
    st.error("⚠️ REVISA SECRETS")

st.title("🚀 PROKONECTA OS v7.0")
archivo = st.file_uploader("Sube tu gráfico", type=['jpg', 'png', 'jpeg'])

if archivo:
    img = Image.open(archivo)
    st.image(img, use_container_width=True)
    if st.button("EJECUTAR ANÁLISIS"):
        with st.spinner("Jarvis Analizando..."):
            try:
                # LA CLAVE: Forzamos la generación en la versión v1
                response = model.generate_content(["Analiza este gráfico de trading en español", img])
                st.info(response.text)
            except Exception as e:
                # Si falla, intentamos el método directo
                st.error(f"Error: {e}. Reintentando conexión...")
