import streamlit as st
import google.generativeai as genai
from PIL import Image

# 1. Configuración de Identidad
st.set_page_config(page_title="PROKONECTA OS", layout="wide")

# 2. Conexión con la llave de Secrets
api_key = st.secrets.get("GEMINI_API_KEY")

if api_key:
    try:
        genai.configure(api_key=api_key)
        # ESTA LÍNEA ES LA QUE QUITA EL ERROR 404
        model = genai.GenerativeModel('gemini-1.5-flash')
        st.sidebar.success("✅ CONECTADO CON ÉXITO")
    except Exception as e:
        st.sidebar.error("❌ Error de API")
else:
    st.error("⚠️ PEGA TU LLAVE EN SECRETS")

# 3. Interfaz de Usuario
st.title("🚀 PROKONECTA OS v7.0")

img_file = st.file_uploader("Sube una imagen para analizar", type=['jpg', 'png', 'jpeg'])

if img_file and st.button("EJECUTAR ANÁLISIS"):
    with st.spinner("Procesando..."):
        img = Image.open(img_file)
        # Pedimos el análisis
        response = model.generate_content(["Analiza esta imagen y dame puntos clave en español.", img])
        st.markdown("### 🤖 Resultado de Jarvis:")
        st.write(response.text)
