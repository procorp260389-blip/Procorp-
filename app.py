import streamlit as st

# Configuración de nivel ejecutivo
st.set_page_config(
    page_title="PROKONECTA | JARVIS OS", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# --- CSS: FUSIÓN CASA STARK + OFICINA SPECTER ---
st.markdown("""
    <style>
    /* Fondo Negro Infinito con degradado sutil */
    .stApp {
        background: radial-gradient(circle, #0a0a0a 0%, #000000 100%) !important;
        color: #E0E0E0 !important;
    }
    
    /* Título Principal en Oro 24k */
    h1 {
        color: #D4AF37 !important;
        font-family: 'Helvetica Neue', sans-serif;
        font-weight: 100 !important;
        letter-spacing: 5px !important;
        text-align: center;
        text-transform: uppercase;
        margin-top: -50px;
    }

    /* Tarjetas de Estatus (Hologramas dorados) */
    .stInfo {
        background-color: rgba(212, 175, 55, 0.05) !important;
        border: 1px solid #D4AF37 !important;
        color: #D4AF37 !important;
        border-radius: 5px !important;
    }

    /* El Botón Harvey Specter: Elegante y potente */
    div.stButton > button {
        width: 100% !important;
        border: 1px solid #D4AF37 !important;
        background-color: transparent !important;
        color: #D4AF37 !important;
        height: 55px !important;
        font-size: 16px !important;
        letter-spacing: 3px !important;
        text-transform: uppercase;
        font-weight: bold;
        transition: 0.4s all ease;
        border-radius: 2px;
    }
    
    div.stButton > button:hover {
        background-color: #D4AF37 !important;
        color: black !important;
        box-shadow: 0 0 25px rgba(212, 175, 55, 0.4);
    }

    /* Input de texto minimalista */
    .stTextInput>div>div>input {
        background-color: #111 !important;
        color: white !important;
        border: 1px solid #333 !important;
        text-align: center;
    }

    /* Ocultar basura visual de Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- INTERFAZ DE USUARIO ---

# Encabezado
st.markdown("<h1>PROKONECTA</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #666; letter-spacing: 2px;'>ADVANCED ANALYTICS | EXECUTIVE INTERFACE</p>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Fila de Estatus de IA
col1, col2 = st.columns(2)
with col1:
    st.info("🤖 SYSTEM: GPT-4 ONLINE")
with col2:
    st.info("🧠 CORE: GEMINI LINKED")

st.markdown("<br><br>", unsafe_allow_html=True)

# Entrada de comando central
orden = st.text_input("DIME TU SIGUIENTE MOVIMIENTO, SOCIO:", placeholder="Escribe aquí tu estrategia...")

st.markdown("<br>", unsafe_allow_html=True)

# Botón de ejecución
if st.button("EJECUTAR PROTOCOLO"):
    with st.spinner('Analizando variables de mercado...'):
        st.success("Jarvis: 'Considerando todas las variables... Movimiento magistral, señor.'")
        st.balloons()
