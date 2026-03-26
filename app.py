import streamlit as st
import pandas as pd
import numpy as np

# Configuración Maestra
st.set_page_config(page_title="PROKONECTA | JARVIS OS", layout="wide", initial_sidebar_state="collapsed")

# CSS DE ALTO IMPACTO (Fusión Stark Industries)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Syncopate:wght@400;700&family=Share+Tech+Mono&display=swap');
    
    .stApp {
        background-color: #030a10 !important;
        background-image: radial-gradient(circle at 50% 50%, #05192d 0%, #030a10 100%) !important;
        color: #00f2ff !important;
        font-family: 'Share Tech Mono', monospace;
    }

    /* Títulos con efecto Neón */
    h1 {
        font-family: 'Syncopate', sans-serif;
        color: #ffffff !important;
        text-shadow: 0 0 10px #00f2ff, 0 0 20px #00f2ff;
        text-align: center;
        letter-spacing: 8px;
        text-transform: uppercase;
    }

    /* Tarjetas de IA (Núcleos de Inteligencia) */
    .ia-core {
        background: rgba(0, 242, 255, 0.05);
        border: 1px solid #00f2ff;
        box-shadow: 0 0 15px rgba(0, 242, 255, 0.2);
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        transition: 0.3s;
    }
    .ia-core:hover {
        background: rgba(0, 242, 255, 0.1);
        box-shadow: 0 0 30px rgba(0, 242, 255, 0.4);
    }

    /* Botones de Acción (Naranja Stark / Cian) */
    div.stButton > button {
        background: linear-gradient(90deg, #ff4b1f 0%, #ff9068 100%) !important;
        color: white !important;
        border: none !important;
        font-family: 'Syncopate', sans-serif;
        font-weight: bold;
        letter-spacing: 2px;
        border-radius: 5px !important;
        height: 50px;
        width: 100% !important;
        box-shadow: 0 4px 15px rgba(255, 75, 31, 0.4);
    }
    
    div.stButton > button:hover {
        transform: scale(1.02);
        box-shadow: 0 6px 25px rgba(255, 75, 31, 0.6);
    }

    /* Estilo de Inputs */
    .stTextInput>div>div>input {
        background-color: rgba(0, 0, 0, 0.5) !important;
        border: 1px solid #00f2ff !important;
        color: #00f2ff !important;
    }
    </style>
""", unsafe_allow_html=True)

# HEADER
st.markdown("<h1>PROKONECTA</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #ff9068; letter-spacing: 3px;'>SISTEMA MULTI-IA UNIFICADO ACTIVO</p>", unsafe_allow_html=True)

# NÚCLEOS DE INTELIGENCIA (Grid)
st.write("---")
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.markdown('<div class="ia-core"><small>NÚCLEO 01</small><br><b>GPT-4</b><br><span style="color:#00ff88">ONLINE</span></div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div class="ia-core"><small>NÚCLEO 02</small><br><b>GEMINI</b><br><span style="color:#00ff88">ONLINE</span></div>', unsafe_allow_html=True)
with c3:
    st.markdown('<div class="ia-core"><small>NÚCLEO 03</small><br><b>GROK</b><br><span style="color:#00ff88">ONLINE</span></div>', unsafe_allow_html=True)
with c4:
    st.markdown('<div class="ia-core"><small>MASTER</small><br><b>JARVIS</b><br><span style="color:#ff9068">ACTIVE</span></div>', unsafe_allow_html=True)

# PESTAÑAS DE CONTROL
tab1, tab2 = st.tabs(["🛡️ COMANDO CENTRAL", "📈 TRADING ENGINE"])

with tab1:
    st.markdown("<br>", unsafe_allow_html=True)
    orden = st.text_input("INGRESE COMANDO OPERATIVO:", placeholder="Jarvis, sincroniza modelos para...")
    if st.button("INICIAR PROTOCOLO"):
        st.write("⚡ **Sincronizando flujos de datos...**")
        st.info("Jarvis: 'Combinando la lógica de GPT-4 con la velocidad de Gemini. Resultado optimizado al 99.9%.'")

with tab2:
    st.markdown("<h3 style='color: #ff9068;'>TRADING HUB | WALL STREET MODE</h3>", unsafe_allow_html=True)
    
    # Simulación de datos financieros
    chart_data = pd.DataFrame(np.random.randn(20, 2), columns=['EQUITY', 'PROFIT'])
    st.area_chart(chart_data)
    
    col_a, col_b = st.columns(2)
    col_a.metric("BALANCE TOTAL", "$25,400 USD", "+12%")
    col_b.metric("PRECISIÓN", "94.8%", "JARVIS OPTIMIZED")
    
    if st.button("EJECUTAR TRADING ANALYTICS"):
        st.balloons()
        st.success("Jarvis: 'Movimiento detectado en el Nasdaq. Posición abierta.'")
