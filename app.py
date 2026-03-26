import streamlit as st
import pandas as pd
import google.generativeai as genai
from PIL import Image

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="PROKONECTA OS", layout="wide")

api_key = st.secrets.get("GEMINI_API_KEY")

if api_key:
    try:
        genai.configure(api_key=api_key)
        # ESTA ES TU LÍNEA 15 CORRECTA
        model = genai.GenerativeModel('gemini-1.5-flash')
        st.sidebar.success("✅ JARVIS ONLINE")
    except Exception as e:
        st.sidebar.error("❌ Error de Conexión")

# --- INTERFAZ ---
st.markdown("<h1 style='text-align: center; color: #00f2ff;'>PROKONECTA OS v7.0</h1>", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["📈 TRADING VISION", "🛰️ RADAR"])

with tab1:
    st.subheader("Análisis de Gráficos")
    img_file = st.file_uploader("Sube tu gráfico", type=['jpg', 'png', 'jpeg'])
    if img_file and st.button("ANALIZAR"):
        with st.spinner("Jarvis analizando..."):
            img = Image.open(img_file)
            response = model.generate_content(["Analiza tendencia, soportes y resistencias de este gráfico en español.", img])
            st.info(response.text)

with tab2:
    st.subheader("Prospectos")
    st.write("Radar activo buscando negocios...")
