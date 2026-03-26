import streamlit as st
import google.generativeai as genai
from PIL import Image

st.set_page_config(page_title="PROKONECTA OS", layout="wide")

# Conexión ultra-directa
api_key = st.secrets.get("GEMINI_API_KEY")

if api_key:
    genai.configure(api_key=api_key)
    # Usamos el nombre más estándar para evitar el error 404
    model = genai.GenerativeModel('gemini-1.5-flash')
    st.sidebar.success("✅ JARVIS ONLINE")
else:
    st.error("⚠️ REVISA TUS SECRETS")

st.title("🚀 PROKONECTA OS v7.0")

archivo = st.file_uploader("Sube tu gráfico de Trading", type=['jpg', 'png', 'jpeg'])

if archivo and st.button("ANALIZAR CON JARVIS"):
    img = Image.open(archivo)
    st.image(img, caption="Gráfico Cargado", use_container_width=True)
    
    with st.spinner("Analizando como Súper Trader..."):
        # Instrucciones precisas para que Jarvis no falle
        prompt = "Actúa como un trader de élite. Analiza esta imagen, identifica tendencia, RSI y MACD, y da una recomendación clara de COMPRA o VENTA en español."
        try:
            response = model.generate_content([prompt, img])
            st.markdown("### 🤖 Veredicto de Jarvis:")
            st.write(response.text)
        except Exception as e:
            st.error(f"Error de conexión: {e}")
