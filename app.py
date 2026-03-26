import streamlit as st
import google.generativeai as genai
from PIL import Image

st.set_page_config(page_title="PROKONECTA OS", layout="wide")

api_key = st.secrets.get("GEMINI_API_KEY")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
    st.sidebar.success("✅ JARVIS ONLINE")
else:
    st.error("⚠️ REVISA SECRETS")

st.title("🚀 PROKONECTA OS v7.0")
archivo = st.file_uploader("Sube tu captura aquí", type=['jpg', 'png', 'jpeg'])

if archivo:
    img = Image.open(archivo)
    st.image(img, use_container_width=True)
    if st.button("EJECUTAR ANÁLISIS"):
        with st.spinner("Jarvis Analizando..."):
            try:
                prompt = "Analiza la tendencia, RSI y MACD de este gráfico en español. Di si es mejor compra o venta."
                response = model.generate_content([prompt, img])
                st.info(response.text)
            except Exception as e:
                st.error(f"Error técnico: {e}")
