import streamlit as st
import pandas as pd
import numpy as np
import time

# --- CONFIGURACIÓN DE IDENTIDAD CORPORATIVA ---
st.set_page_config(page_title="PROKONECTA | JARVIS OS", layout="wide", initial_sidebar_state="collapsed")

# --- CSS: ESTÉTICA STARK + MONETIZACIÓN ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Share+Tech+Mono&display=swap');
    
    .stApp {
        background: radial-gradient(circle at center, #001529 0%, #000000 100%) !important;
        color: #00f2ff !important;
        font-family: 'Share Tech Mono', monospace;
    }

    h1 {
        font-family: 'Orbitron', sans-serif;
        color: #ffffff !important;
        text-shadow: 0 0 15px #00f2ff;
        text-align: center;
        letter-spacing: 10px;
    }

    /* Estilo de los Planes (Monetización) */
    .plan-card {
        background: rgba(255, 144, 104, 0.05);
        border: 1px solid #ff9068;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
    }

    /* Explicaciones de botones (Tooltips) */
    .help-text {
        color: #888;
        font-size: 0.8rem;
        margin-bottom: 5px;
    }

    /* Botones Estilo Premium */
    div.stButton > button {
        background: linear-gradient(90deg, #ff4b1f, #ff9068) !important;
        color: white !important;
        font-family: 'Orbitron', sans-serif;
        border: none !important;
        height: 50px;
        width: 100% !important;
        border-radius: 5px !important;
        box-shadow: 0 0 15px rgba(255, 75, 31, 0.3);
    }
    </style>
""", unsafe_allow_html=True)

# --- CABECERA ---
st.markdown("<h1>PROKONECTA</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #ff9068;'>INFRAESTRUCTURA DE IA Y SOLUCIONES FINANCIERAS</p>", unsafe_allow_html=True)

# --- NAVEGACIÓN DE PRODUCTO ---
tab_home, tab_nexus, tab_trading, tab_planes = st.tabs([
    "🏠 INICIO", "🧠 JARVIS NEXUS", "📈 JARVIS TRADING", "💎 PLANES"
])

with tab_home:
    st.subheader("Bienvenido al Futuro de la Productividad")
    st.write("Jarvis es el cerebro que unifica las IAs más potentes del mundo en una sola interfaz.")
    st.info("💡 **Tip para novatos:** Selecciona 'Jarvis Nexus' para tareas creativas o 'Trading' para análisis de mercado.")

with tab_nexus:
    st.markdown("### 🧠 Nexus Core (Multi-IA)")
    st.markdown('<p class="help-text">Escribe tu orden y Jarvis decidirá qué IA (GPT, Gemini o Claude) es mejor para ejecutarla.</p>', unsafe_allow_html=True)
    
    prompt = st.text_input("ORDEN COMERCIAL / CREATIVA:", placeholder="Ej: 'Diseña una campaña de marketing usando el poder de todos los modelos'...")
    
    if st.button("SINCRONIZAR NÚCLEOS"):
        with st.status("Jarvis coordinando recursos...", expanded=True):
            st.write("✅ Conectando con GPT-4 para estructura...")
            time.sleep(1)
            st.write("✅ Consultando Gemini para datos actualizados...")
            time.sleep(1)
            st.success("Jarvis: 'Protocolo completado. Aquí tiene la solución optimizada.'")

with tab_trading:
    st.markdown("### 📈 Jarvis Trading Lab")
    st.markdown('<p class="help-text">Análisis predictivo de activos. Conecta tu cuenta de Broker para ejecución automática (Próximamente).</p>', unsafe_allow_html=True)
    
    c1, c2 = st.columns([2, 1])
    with c1:
        st.line_chart(pd.DataFrame(np.random.randn(20, 2), columns=['Tendencia', 'Volumen']))
    with c2:
        st.metric("EQUITY ACTUAL", "$152,400 MXN", "+15%")
        st.metric("TASA DE ÉXITO", "94.2%")
        if st.button("ANALIZAR MERCADO"):
            st.warning("Jarvis: 'Detectando patrones de alta frecuencia...'")

with tab_planes:
    st.markdown("### Selecciona tu Nivel de Acceso")
    p1, p2, p3 = st.columns(3)
    with p1:
        st.markdown('<div class="plan-card"><h4>BÁSICO</h4><h2>$299</h2><p>1 Usuario<br>Acceso a GPT-4</p></div>', unsafe_allow_html=True)
    with p2:
        st.markdown('<div class="plan-card" style="border-width: 3px;"><h4>AVANZADO</h4><h2>$799</h2><p>Multi-IA Linked<br>Jarvis Brain v1</p></div>', unsafe_allow_html=True)
    with p3:
        st.markdown('<div class="plan-card"><h4>PREMIUM</h4><h2>$1,999</h2><p>Acceso Total<br>Trading Lab Unlocked</p></div>', unsafe_allow_html=True)

st.write("---")
st.caption("PROKONECTA OS | Powered by Jarvis")
