import streamlit as st

def style_background_home():
    st.markdown("""<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/icon?family=Material+Icons+Round" rel="stylesheet">
<style>
#MainMenu, header, footer,
[data-testid="stStatusWidget"],
[data-testid="stToolbar"] {
    visibility: hidden !important;
    height: 0 !important;
}
.stApp {
    background:
        radial-gradient(circle at top left, rgba(59,130,246,0.14) 0, rgba(59,130,246,0) 32%),
        linear-gradient(180deg, #f8fafc 0%, #edf2f7 100%) !important;
    min-height: 100vh;
}
.block-container {
    padding-top: 0 !important;
    max-width: 900px !important;
}
h1, h2, h3, h4, h5, h6, p, span, div, label, li {
    font-family: 'Inter', sans-serif !important;
}
.material-icons-round {
    font-family: 'Material Icons Round' !important;
    font-weight: normal !important;
    font-style: normal !important;
    line-height: 1 !important;
    letter-spacing: normal !important;
    text-transform: none !important;
    white-space: nowrap !important;
    word-wrap: normal !important;
    direction: ltr !important;
    -webkit-font-feature-settings: 'liga' !important;
    -webkit-font-smoothing: antialiased !important;
}
.stButton > button {
    font-family: 'Space Grotesk', sans-serif !important;
    font-weight: 600 !important;
    font-size: 1.1rem !important;
    padding: 0.9rem 2rem !important;
    border-radius: 14px !important;
    border: 1px solid rgba(71,85,105,0.18) !important;
    background: #ffffff !important;
    color: #1e293b !important;
    cursor: pointer !important;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    backdrop-filter: blur(10px) !important;
    width: 100% !important;
    min-height: 70px !important;
    letter-spacing: 0.02em !important;
}
.stButton > button:hover {
    background: #eff6ff !important;
    border-color: rgba(37,99,235,0.34) !important;
    color: #1d4ed8 !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 10px 28px rgba(37,99,235,0.16) !important;
}
.stButton > button:active {
    transform: translateY(0px) !important;
}
[data-testid="stMarkdownContainer"] p,
[data-testid="stMarkdownContainer"] span,
[data-testid="stMarkdownContainer"] li,
[data-testid="stMarkdownContainer"] div {
    color: #475569 !important;
}
</style>""", unsafe_allow_html=True)


def style_background_dashboard():
    st.markdown("""<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
#MainMenu, header, footer,
[data-testid="stStatusWidget"],
[data-testid="stToolbar"] {
    visibility: hidden !important;
    height: 0 !important;
}
.stApp {
    background: linear-gradient(160deg, #0f172a 0%, #1e1b4b 40%, #0f172a 100%) !important;
    min-height: 100vh;
}
.block-container {
    padding-top: 2rem !important;
    max-width: 1000px !important;
}
h1, h2, h3, h4, h5, h6 {
    font-family: 'Space Grotesk', sans-serif !important;
    color: #e2e8f0 !important;
}
p, span, div, label, li {
    font-family: 'Inter', sans-serif !important;
    color: #cbd5e1 !important;
}
h1 {
    font-size: 2.2rem !important;
    font-weight: 700 !important;
}
.stButton > button {
    font-family: 'Inter', sans-serif !important;
    font-weight: 500 !important;
    font-size: 1rem !important;
    padding: 0.6rem 1.5rem !important;
    border-radius: 10px !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
    background: rgba(255,255,255,0.06) !important;
    color: #e0e0ff !important;
    transition: all 0.25s ease !important;
}
.stButton > button:hover {
    background: rgba(99,102,241,0.3) !important;
    border-color: rgba(99,102,241,0.5) !important;
    color: #fff !important;
}
</style>""", unsafe_allow_html=True)


def style_base_layout():
    pass
