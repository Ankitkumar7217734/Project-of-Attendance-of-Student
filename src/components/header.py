import streamlit as st


def header_home():
    st.markdown("""<div style="text-align: center; padding: 4rem 1rem 1rem 1rem;">
<div style="display: inline-flex; align-items: center; justify-content: center; width: 5.4rem; height: 5.4rem; margin-bottom: 0.9rem; border-radius: 1.3rem; background: linear-gradient(135deg, #2563eb, #0f766e); box-shadow: 0 18px 38px rgba(37,99,235,0.18), inset 0 1px 0 rgba(255,255,255,0.32); position: relative; overflow: hidden;">
    <span style="position: absolute; width: 3.45rem; height: 3.45rem; border: 3px solid rgba(255,255,255,0.78); border-radius: 1rem;"></span>
    <span style="position: absolute; width: 1rem; height: 1rem; border-radius: 50%; background: rgba(255,255,255,0.94); top: 1.6rem;"></span>
    <span style="position: absolute; width: 2.2rem; height: 0.95rem; border-radius: 999px 999px 0.35rem 0.35rem; background: rgba(255,255,255,0.92); bottom: 1.45rem;"></span>
</div>
<h1 style="font-family: 'Space Grotesk', sans-serif !important; font-size: 2.8rem !important; font-weight: 800 !important; color:#0f172a !important; margin: 0 0 0.5rem 0 !important; line-height: 1.2 !important; letter-spacing: -0.02em;">Attendance Management<br>System</h1>
</div>""", unsafe_allow_html=True)
