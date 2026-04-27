import streamlit as st


def footer_home():
    st.markdown(
        """
<div role="contentinfo" style="
    max-width: 760px;
    margin: 3.25rem auto 1.5rem auto;
    padding: 1.1rem 1.25rem;
    border-top: 1px solid rgba(100,116,139,0.18);
    text-align: center;
">
    <p style="
        font-family: Inter, sans-serif !important;
        font-size: 0.82rem !important;
        color: #64748b !important;
        font-weight: 600;
        margin: 0 0 0.35rem 0;
        letter-spacing: 0.01em;
    ">
        Face Recognition &bull; QR Codes &bull; Real-time Tracking
    </p>
    <p style="
        font-family: Inter, sans-serif !important;
        font-size: 0.74rem !important;
        color: #94a3b8 !important;
        font-weight: 500;
        margin: 0;
    ">
        Attendance Management System
    </p>
</div>
""",
        unsafe_allow_html=True,
    )
