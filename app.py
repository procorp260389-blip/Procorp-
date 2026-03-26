import streamlit as st
import google.generativeai as genai
from PIL import Image

st.set_page_config(page_title="PROKONECTA OS", layout="wide")

# Conexión directa
api_key = st.secrets.get("GEMINI_API_KEY")

if api_key:
    genai.configure(api_key=api_key)
    # Modelo estándar estable para evitar el 404
    model = genai.GenerativeModel('gemini-1.5-flash')
    st.sidebar.success("✅ JARVIS ONLINE")
else:
    st.error("⚠️ FALTA LLAVE EN SECRETS")

st.title("🚀 PROKONECTA OS v7.0")
archivo = st.file_uploader("Sube tu gráfico", type=['jpg', 'png', 'jpeg'])

if archivo and st.button("EJECUTAR ANÁLISIS"):
    img = Image.open(archivo)
    with st.spinner("Analizando como Súper Trader..."):
        prompt = "Actúa como un trader de élite. Analiza esta imagen, identifica tendencia, RSI y MACD, y da una recomendación clara de COMPRA o VENTA en español."
        try:
            response = model.generate_content([prompt, img])
            st.markdown("### 🤖 Veredicto de Jarvis:")
            st.write(response.text)
        except Exception as e:
            st.error(f"Error técnico: {e}")
