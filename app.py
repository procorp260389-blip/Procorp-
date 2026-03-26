import streamlit as st
from streamlit_option_menu import option_menu

# --- CONFIGURACIÓN DE IDENTIDAD ---
st.set_page_config(page_title="ProKonecta | Jarvis OS", layout="wide", page_icon="⚡")

# CSS para el look "Harvey Specter" (Negro Profundo y Oro)
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #ffffff; }
    [data-testid="stHeader"] { background: rgba(0,0,0,0); }
    .stButton>button { border: 1px solid #D4AF37; background: transparent; color: #D4AF37; font-weight: bold; }
    .stButton>button:hover { background: #D4AF37; color: black; }
    h1, h2, h3 { color: #D4AF37 !important; }
    </style>
""", unsafe_allow_html=True)

# --- MENÚ DE NAVEGACIÓN ---
with st.sidebar:
    st.title("PROKONECTA")
    st.write("`Status: Active` | `User: Specter`")
    selected = option_menu(
        menu_title=None,
        options=["Jarvis Hub", "Trading Lab", "Settings"],
        icons=["cpu", "graph-up-arrow", "gear"],
        default_index=0,
        styles={
            "container": {"padding": "5!important", "background-color": "#111"},
            "nav-link": {"color": "white", "font-size": "15px", "text-align": "left"},
            "nav-link-selected": {"background-color": "#D4AF37", "color": "black"},
        }
    )

# --- SECCIONES ---
if selected == "Jarvis Hub":
    st.header("⚡ Jarvis: Central Intelligence")
    st.subheader("Fusión de Modelos Activa")
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("Estatus de IA:")
        st.success("ChatGPT-4: Online")
        st.success("Gemini 1.5: Online")
    
    pregunta = st.text_input("Orden para Jarvis:", placeholder="¿Cuál es el siguiente movimiento, socio?")
    if st.button("Ejecutar"):
        st.write("Jarvis: *'Entendido. Analizando variables para maximizar el impacto.'*")

elif selected == "Trading Lab":
    st.header("📈 Trading & Market Intelligence")
    st.write("Simulación de Equity en tiempo real.")
    # Gráfica de ejemplo de crecimiento
    st.line_chart([10, 25, 45, 30, 80, 120])
