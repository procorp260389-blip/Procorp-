import streamlit as st
import google.generativeai as genai
from PIL import Image

# Configuración de página
st.set_page_config(page_title="PROKONECTA OS", layout="wide")

# Conexión con la llave
api_key = st.secrets.get("GEMINI_API_KEY")

if api_key:
    genai.configure(api_key=api_key)
    # EL CEREBRO DE LA IA (Versión estable)
    model = genai.GenerativeModel('gemini-1.5-flash')
    st.sidebar.success("✅ JARVIS ONLINE")
else:
    st.sidebar.error("❌ FALTA LLAVE")

st.markdown("<h1 style='color: #00f2ff;'>PROKONECTA OS v7.0</h1>", unsafe_allow_html=True)

# Subida de archivos
img_file = st.file_uploader("Sube tu captura aquí", type=['jpg', 'png', 'jpeg'])

if img_file:
    st.image(img_file, caption="Imagen cargada", use_container_width=True)
    
    if st.button("EJECUTAR ANÁLISIS"):
        try:
            with st.spinner("Jarvis analizando..."):
                img = Image.open(img_file)
                # Comando directo a la IA
                response = model.generate_content(["Analiza esta imagen detalladamente en español.", img])
                st.subheader("🤖 Análisis de Jarvis:")
                st.write(response.text)
        except Exception as e:
            st.error(f"Error técnico: {e}")
