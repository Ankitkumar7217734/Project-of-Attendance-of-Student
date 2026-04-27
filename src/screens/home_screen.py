import streamlit as st
from src.components.footer import footer_home
from src.components.header import header_home
from ui.base_layout import style_base_layout, style_background_home


def home_screen():
    style_background_home()
    style_base_layout()
    header_home()

    st.markdown("<div style='height: 1.5rem'></div>", unsafe_allow_html=True)

    st.markdown('<p style="text-align: center; font-family: Inter, sans-serif !important; font-size: 0.9rem !important; color: #64748b !important; text-transform: uppercase; letter-spacing: 0.15em; font-weight: 700; margin-bottom: 0.5rem;">Select your role to continue</p>', unsafe_allow_html=True)

    col_pad_l, col1, col_mid, col2, col_pad_r = st.columns([1, 3, 0.5, 3, 1])

    with col1:
        st.markdown("""<div style="text-align:center; margin-bottom:0.65rem;">
<span style="display:inline-flex; align-items:center; justify-content:center; width:3.8rem; height:3.8rem; border-radius:1rem; background:#ffffff; border:1px solid rgba(37,99,235,0.16); box-shadow:0 12px 28px rgba(15,23,42,0.08), inset 0 1px 0 rgba(255,255,255,0.9);">
    <svg width="34" height="34" viewBox="0 0 24 24" fill="none" aria-hidden="true">
        <path d="M4 5.5h16v11H4z" stroke="#2563eb" stroke-width="1.7" stroke-linejoin="round"/>
        <path d="M8 19h8" stroke="#2563eb" stroke-width="1.7" stroke-linecap="round"/>
        <path d="M12 16.5V19" stroke="#2563eb" stroke-width="1.7" stroke-linecap="round"/>
        <path d="M8.2 10h3.2M8.2 13h5.8" stroke="#334155" stroke-width="1.6" stroke-linecap="round"/>
        <path d="M16.6 9.2a1.4 1.4 0 1 1-2.8 0 1.4 1.4 0 0 1 2.8 0Z" fill="#334155"/>
        <path d="M13.3 13.2c.4-1 1.1-1.5 1.9-1.5s1.5.5 1.9 1.5" stroke="#334155" stroke-width="1.5" stroke-linecap="round"/>
    </svg>
</span>
</div>""", unsafe_allow_html=True)
        if st.button("Login as Teacher", use_container_width=True):
            st.session_state['login_type'] = "teacher"
            st.rerun()

    with col2:
        st.markdown("""<div style="text-align:center; margin-bottom:0.65rem;">
<span style="display:inline-flex; align-items:center; justify-content:center; width:3.8rem; height:3.8rem; border-radius:1rem; background:#ffffff; border:1px solid rgba(15,118,110,0.16); box-shadow:0 12px 28px rgba(15,23,42,0.08), inset 0 1px 0 rgba(255,255,255,0.9);">
    <svg width="36" height="36" viewBox="0 0 24 24" fill="none" aria-hidden="true">
        <path d="M3.5 8.2 12 4.5l8.5 3.7-8.5 3.7-8.5-3.7Z" stroke="#0f766e" stroke-width="1.7" stroke-linejoin="round"/>
        <path d="M7 10v4.1c1.4 1.1 3 1.7 5 1.7s3.6-.6 5-1.7V10" stroke="#0f766e" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/>
        <path d="M20.5 8.3v5" stroke="#334155" stroke-width="1.6" stroke-linecap="round"/>
        <path d="M20.5 15.8v.1" stroke="#334155" stroke-width="2.4" stroke-linecap="round"/>
    </svg>
</span>
</div>""", unsafe_allow_html=True)
        if st.button("Login as Student", use_container_width=True):
            st.session_state['login_type'] = "student"
            st.rerun()

    footer_home()
