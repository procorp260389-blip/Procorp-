import streamlit as st
import pandas as pd
import numpy as np
import time

# --- CONFIGURACIÓN DEL SISTEMA JARVIS OS ---
st.set_page_config(page_title="JARVIS | PROKONECTA GLOBAL", layout="wide", initial_sidebar_state="collapsed")

# --- INTERFAZ HOLOGRÁFICA (CSS AVANZADO DE GRADO STARK) ---
# Este código crea el efecto de vidrio, neón y movimiento dinámico.
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Syncopate:wght@400;700&family=JetBrains+Mono:wght@300&family=Inter:wght@400;700&display=swap');
    
    /* Fondo Dinámico Espacial */
    .stApp {
        background: radial-gradient(circle at center, #001529 0%, #000000 100%) !important;
        background-attachment: fixed;
        color: #00f2ff !important;
        font-family: 'Inter', sans-serif;
    }

    /* Ocultar elementos estándar para limpieza total */
    header, footer, #MainMenu {visibility: hidden;}
    .stHeader { background: transparent !important; }

    /* Título con Neón Activo (Syncopate) */
    h1 {
        font-family: 'Syncopate', sans-serif;
        color: #fff !important;
        text-shadow: 0 0 10px #00f2ff, 0 0 20px #00f2ff, 0 0 30px #00f2ff;
        text-align: center;
        letter-spacing: 15px;
        text-transform: uppercase;
        margin-top: -60px;
    }

    /* Subtítulo Táctico */
    .tech-sub {
        font-family: 'JetBrains Mono', monospace;
        text-align: center;
        color: #fff;
        opacity: 0.8;
        letter-spacing: 5px;
        font-weight: 300;
        margin-top: -10px;
    }

    /* Paneles de Vidrio Holográfico Flotante (Glassmorphism) */
    .hologram-panel {
        background: rgba(0, 242, 255, 0.01);
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        border: 1px solid rgba(0, 242, 255, 0.1);
        border-radius: 4px;
        padding: 25px;
        box-shadow: 0 8px 32px 0 rgba(0, 242, 255, 0.05);
        transition: 0.5s all ease;
        min-height: 280px;
    }
    .hologram-panel:hover {
        border-color: rgba(0, 242, 255, 0.6);
        background: rgba(0, 242, 255, 0.03);
        transform: translateY(-8px) scale(1.01);
        box-shadow: 0 0 50px rgba(0, 242, 255, 0.2);
    }

    /* Títulos de Módulo (Con brillo sutil) */
    .module-title {
        font-family: 'Syncopate', sans-serif;
        color: #fff;
        text-shadow: 0 0 5px #00f2ff;
        font-size: 1.1rem;
        letter-spacing: 2px;
        margin-bottom: 15px;
    }

    /* Estado de Núcleos (Multi-color sutil) */
    .core-status {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.8rem;
        margin-top: 10px;
    }

    /* Botón Maestro Táctico (Interactivo) */
    div.stButton > button {
        background: transparent !important;
        border: 1px solid #00f2ff !important;
        color: #00f2ff !important;
        font-family: 'Syncopate', sans-serif;
        font-weight: bold;
        height: 60px;
        width: 100% !important;
        text-transform: uppercase;
        letter-spacing: 3px;
        transition: 0.5s;
        border-radius: 2px;
        font-size: 0.9rem;
    }
    div.stButton > button:hover {
        background: #00f2ff !important;
        color: #000 !important;
        box-shadow: 0 0 60px #00f2ff;
        transform: scale(1.02);
    }

    /* Estilo de Inputs (Campos de texto transparentes) */
    .stTextInput>div>div>input {
        background-color: rgba(0, 0, 0, 0.6) !important;
        color: #00f2ff !important;
        border: 1px solid rgba(0, 242, 255, 0.2) !important;
        border-radius: 2px;
        text-align: center;
        font-family: 'JetBrains Mono', monospace;
    }

    /* Gráficas con estilo Stark (Transparentes) */
    .stVegaLiteChart {
        background-color: transparent !important;
        border: none !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- CABECERA ---
st.markdown("<h1>PROKONECTA</h1>", unsafe_allow_html=True)
st.markdown("<p class='tech-sub'>GLOBAL OS | UNIFIED INTELLIGENCE</p>", unsafe_allow_html=True)

# --- SISTEMA DE NAVEGACIÓN HOLOGRÁFICA ---
st.write("---")
tab_command, tab_trading, tab_creative = st.tabs(["🏛️ COMANDO OPERATIVO", "📈 TRADING ENGINE", "🚀 CREATIVOS"])

# 1. MÓDULO DE COMANDO OPERATIVO (CEO, COACH, GLOBAL MAPS)
with tab_command:
    col_c1, col_c2 = st.columns(2)
    with col_c1:
        st.markdown("""<div class="hologram-panel">
            <h3 class="module-title">🏢 CEO GLOBAL COMMAND</h3>
            <p style="color:#fff; opacity:0.7;">Sincronización de CRM, Inteligencia de Mercado Google Maps México, Logística Avanzada.</p>
            <div class="core-status">● Potenciado por <span style="color:#ff9068">GPT-4</span> + <span style="color:#00ff88">Gemini 1.5</span></div>
        </div>""", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("INICIAR PROTOCOLO EMPRESARIAL"):
            st.info("🛰️ Jarvis: 'Sincronizando satélites de datos comerciales...'")
            
    with col_c2:
        st.markdown("""<div class="hologram-panel">
            <h3 class="module-title">🧠 COACH CENTRAL OPERATIVO</h3>
            <p style="color:#fff; opacity:0.7;">Análisis de riesgos, optimización de decisiones de alto impacto y soporte estratégico emocional.</p>
            <div class="core-status">● <span style="color:#00f2ff">EMPATHY ENGINE ACTIVE</span></div>
        </div>""", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("INICIAR CONSULTA ESTRATÉGICA"):
            st.success("Jarvis: 'El motor analítico está listo, socio. ¿Cuál es el desafío de hoy?'")

# 2. MÓDULO TRADING LAB
with tab_trading:
    st.subheader("📊 Jarvis Trading Lab | Wall Street")
    # Gráfica limpia con el color de Jarvis
    tr_data = pd.DataFrame(np.random.randn(25, 1), columns=['Rendimiento'])
    st.area_chart(tr_data, color="#00f2ff")
    
    col_t1, col_t2 = st.columns(2)
    with col_t1:
        st.metric("CAPITAL SIMULADO", "$152,400 USD", "+$4,200")
    with col_t2:
        if st.button("EJECUTAR ANÁLISIS AGRESIVO"):
            st.warning("Jarvis: 'Escaneando flujos de capital en tiempo real...'")

# 3. MÓDULO CREATIVO (TikTok)
with tab_creative:
    st.subheader("🤳 Viralidad Bajo Demanda")
    creative_prompt = st.text_input("Ingresa tu visión creativa:", placeholder="Ej: 'Genera un guion viral para vender mi nuevo producto en CDMX'...")
    if st.button("CREAR IMPACTO VIRAL"):
        with st.status("Jarvis orquestando núcleos...", expanded=True):
            st.write("1. **Claude** analizando psicología...")
            time.sleep(1)
            st.write("2. **Gemini** buscando tendencias en México...")
            time.sleep(1)
            st.success("Jarvis: 'Estrategia de impacto generada.'")

# --- FOOTER ---
st.write("---")
st.markdown("<p style='text-align: center; font-size: 10px; color: #333; letter-spacing: 2px;'>JARVIS NEURAL NETWORK OS v3.0 | PROKONECTA ©</p>", unsafe_allow_html=True)
