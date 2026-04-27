import streamlit as st
from ui.base_layout import style_background_dashboard


def teacher_screen():
    style_background_dashboard()

    if st.button("← Back to Home"):
        st.session_state['login_type'] = None
        st.rerun()

    st.markdown("""<div style="padding: 1rem 0;">
<h1 style="font-family: 'Space Grotesk', sans-serif !important; font-weight: 700 !important; background: linear-gradient(135deg, #a5f3fc, #818cf8); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;">🧑‍🏫 Teacher Dashboard</h1>
<p style="font-family: 'Inter', sans-serif !important; color: rgba(203,213,225,0.7) !important; font-size: 1.05rem !important;">Welcome! Manage your classes, assignments, and students.</p>
</div>""", unsafe_allow_html=True)
