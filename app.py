import streamlit as st
import pandas as pd
import google.generativeai as genai
from PIL import Image

# --- CONFIGURACIÓN DE IDENTIDAD ---
st.set_page_config(page_title="PROKONECTA OS v7.0", layout="wide")

# Recuperar llave de la Caja Fuerte
api_key = st.secrets.get("GEMINI_API_KEY")

if api_key:
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        st.sidebar.success("✅ JARVIS ONLINE")
    except Exception as e:
        st.sidebar.error("❌ Error de Conexión")

# --- DISEÑO PROFESIONAL ---
st.markdown("<h1 style='text-align: center; color: #00f2ff;'>PROKONECTA OS v7.0</h1>", unsafe_allow_html=True)

tab_trading, tab_radar, tab_vision = st.tabs(["📈 TRADING VISION", "🛰️ RADAR MÉXICO", "👁️ SCANNER QR/DISEÑO"])

with tab_trading:
    st.subheader("Análisis de Gráficos de Alto Nivel")
    img_file = st.file_uploader("Sube tu gráfico (Oro, BTC, Forex)", type=['jpg', 'png', 'jpeg'])
    if img_file and st.button("ANALIZAR CON INTELIGENCIA COLECTIVA"):
        with st.spinner("Analizando..."):
            img = Image.open(img_file)
            response = model.generate_content(["Actúa como un trader experto. Analiza soportes y resistencias de esta imagen en español.", img])
            st.info(response.text)

with tab_radar:
    st.subheader("Prospectos Estratégicos")
    if st.button("BUSCAR NEGOCIOS PARA DIGITALIZAR"):
        data = {"Negocio": ["Restaurante Prime", "Hotel Boutique", "Club Elite"], "Prioridad": ["Alta", "Media", "Alta"]}
        st.table(pd.DataFrame(data))

with tab_vision:
    st.subheader("Scanner y Rediseño")
    cam_img = st.camera_input("Scanner Jarvis")
    if cam_img and st.button("MEJORAR DISEÑO"):
        img_cam = Image.open(cam_img)
        response = model.generate_content(["Dime cómo hacer este diseño más futurista y elegante.", img_cam])
        st.success(response.text)
