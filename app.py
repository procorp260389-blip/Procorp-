import streamlit as st
import google.generativeai as genai
from PIL import Image

# Configuración de identidad
st.set_page_config(page_title="PROKONECTA OS", layout="wide")

# Conexión con la llave desde Secrets
api_key = st.secrets.get("GEMINI_API_KEY")

if api_key:
    try:
        genai.configure(api_key=api_key)
        # Nombre estándar que NO da error 404
        model = genai.GenerativeModel('gemini-1.5-flash')
        st.sidebar.success("✅ JARVIS ONLINE")
    except Exception as e:
        st.sidebar.error(f"Error: {e}")
else:
    st.error("⚠️ PEGA TU LLAVE EN SECRETS")

st.markdown("<h1 style='color: #00f2ff;'>PROKONECTA OS v7.0</h1>", unsafe_allow_html=True)

img_file = st.file_uploader("Sube tu gráfico de Trading", type=['jpg', 'png', 'jpeg'])

if img_file:
    st.image(img_file, caption="Gráfico listo", use_container_width=True)
    if st.button("EJECUTAR ANÁLISIS"):
        with st.spinner("Analizando como Súper Trader..."):
            try:
                img = Image.open(img_file)
                response = model.generate_content(["Analiza tendencia, RSI y MACD de este gráfico en español.", img])
                st.info(response.text)
            except Exception as e:
                st.error(f"Error técnico: {e}")
