import streamlit as st
from src.components.footer import footer_dashboard
from ui.base_layout import style_background_dashboard, style_base_layout


def teacher_screen():
    style_background_dashboard()
    style_base_layout()
    teacher_screen_styles()

    if "teacher_authenticated" not in st.session_state:
        st.session_state["teacher_authenticated"] = False
    if "teacher_auth_choice" not in st.session_state:
        st.session_state["teacher_auth_choice"] = "Login"

    render_teacher_topbar()

    if not st.session_state["teacher_authenticated"]:
        render_teacher_auth_panel()
        return

    render_teacher_dashboard()


def teacher_screen_styles():
    st.markdown(
        """<style>
.teacher-access-hero {
    background: rgba(255, 255, 255, 0.82);
    border: 1px solid rgba(186, 230, 253, 0.8);
    border-radius: 18px;
    padding: 1.4rem 1.6rem;
    box-shadow: 0 16px 36px rgba(15, 23, 42, 0.08);
    width: 100%;
    margin: 0 0 1.2rem 0;
}
.teacher-auth-title {
    font-family: 'Space Grotesk', sans-serif !important;
    font-size: 2rem;
    font-weight: 700;
    color: #0f172a;
    margin-bottom: 0.35rem;
}
.teacher-auth-sub {
    font-family: 'Space Grotesk', sans-serif !important;
    color: #475569;
    font-size: 1.05rem;
    margin-bottom: 1.1rem;
}
.teacher-auth-note {
    font-size: 0.85rem;
    color: #64748b;
    margin-top: 0.8rem;
}
.teacher-auth-actions button {
    background: #0f766e !important;
    color: #f8fafc !important;
    border: 1px solid rgba(15, 118, 110, 0.35) !important;
    box-shadow: 0 10px 24px rgba(15, 118, 110, 0.18) !important;
    cursor: pointer !important;
}
.teacher-auth-actions button:hover {
    background: #0d9488 !important;
    color: #f8fafc !important;
    border-color: rgba(13, 148, 136, 0.45) !important;
    box-shadow: 0 14px 28px rgba(13, 148, 136, 0.24) !important;
}
.teacher-auth-actions button:active {
    transform: translateY(0px) !important;
}
[data-testid="stForm"] {
    background: linear-gradient(145deg, rgba(224, 242, 254, 0.9), rgba(255, 247, 237, 0.96));
    border: 1px solid rgba(94, 234, 212, 0.3);
    border-radius: 18px;
    padding: 1.6rem;
    box-shadow: 0 18px 40px rgba(15, 23, 42, 0.08);
    width: 100%;
}
[data-testid="stTextInput"],
[data-testid="stPassword"],
[data-testid="stTextInput"] > div,
[data-testid="stPassword"] > div {
    width: 100%;
    max-width: 100%;
}
[data-testid="stTextInput"] div[data-testid="stMarkdownContainer"],
[data-testid="stTextInput"] p,
[data-testid="stTextInput"] small {
    display: none !important;
}
[data-testid="InputInstructions"],
[data-testid="stTextInput"] div[data-testid="stMarkdownContainer"] * {
    display: none !important;
}
</style>""",
        unsafe_allow_html=True,
    )


def render_teacher_topbar():
    top_left, _, top_right = st.columns([1, 2, 1])
    with top_left:
        if st.button("← Back to Home"):
            st.session_state["login_type"] = None
            st.session_state["teacher_authenticated"] = False
            st.session_state["teacher_auth_choice"] = "Login"
            st.rerun()
    with top_right:
        st.markdown(
            """<div style="text-align: right; font-size: 0.8rem; letter-spacing: 0.18em; text-transform: uppercase; color: #64748b; font-weight: 600;">Teacher Portal</div>""",
            unsafe_allow_html=True,
        )


def render_teacher_auth_panel():
    hero_left, hero_center, hero_right = st.columns([1, 5, 1])
    with hero_center:
        st.markdown(
            """<div class="teacher-access-hero">
<div class="teacher-auth-title">Teacher Access</div>
<div class="teacher-auth-sub">Sign in to manage classes, assignments, and attendance.</div>
</div>""",
            unsafe_allow_html=True,
        )

    form_left, form_center, form_right = st.columns([1, 2.2, 1])
    with form_center:
        toggle_left, toggle_right = st.columns(2)
        active_choice = st.session_state["teacher_auth_choice"]
        with toggle_left:
            if st.button(
                "Login",
                type="primary" if active_choice == "Login" else "secondary",
                use_container_width=True,
                key="teacher_auth_login_btn",
            ):
                st.session_state["teacher_auth_choice"] = "Login"
        with toggle_right:
            if st.button(
                "Register",
                type="primary" if active_choice == "Register" else "secondary",
                use_container_width=True,
                key="teacher_auth_register_btn",
            ):
                st.session_state["teacher_auth_choice"] = "Register"

        if st.session_state["teacher_auth_choice"] == "Login":
            render_teacher_login_form()
        else:
            render_teacher_register_form()

        st.markdown(
            """<div class="teacher-auth-note">Demo only: any email + password will let you in.</div>""",
            unsafe_allow_html=True,
        )


def render_teacher_login_form():
    with st.form("teacher_login_form", clear_on_submit=False):
        email = st.text_input("School email", placeholder="name@school.edu")
        password = st.text_input("Password", type="password", placeholder="Enter your password")
        remember = st.checkbox("Remember me", value=True)
        submitted = st.form_submit_button("Sign in", type="primary")

    if submitted:
        if not email or not password:
            st.warning("Please enter your email and password.")
            return

        st.session_state["teacher_authenticated"] = True
        st.session_state["teacher_name"] = format_teacher_name(email)
        st.session_state["teacher_remember"] = remember
        st.rerun()


def render_teacher_register_form():
    with st.form("teacher_register_form", clear_on_submit=False):
        name = st.text_input("Full name", placeholder="Avery Cole")
        email = st.text_input("School email", placeholder="name@school.edu")
        password = st.text_input("Create password", type="password")
        confirm = st.text_input("Confirm password", type="password")
        submitted = st.form_submit_button("Create account", type="secondary")

    if submitted:
        if not name or not email or not password or not confirm:
            st.warning("Please complete all fields to register.")
            return
        if password != confirm:
            st.warning("Passwords do not match. Try again.")
            return

        st.session_state["teacher_auth_choice"] = "Login"
        st.success("Account created. Use the Login tab to sign in.")


def render_teacher_dashboard():
    teacher_name = st.session_state.get("teacher_name", "Teacher")
    st.markdown(
        f"""<div style="padding: 1rem 0 1.25rem 0;">
<h1 style="font-family: 'Space Grotesk', sans-serif !important; font-weight: 700 !important; color:#0f172a !important; margin-bottom: 0.35rem !important;">Welcome back, {teacher_name}</h1>
<p style="font-family: 'Space Grotesk', sans-serif !important; color:#475569 !important; font-size: 1.05rem !important;">Manage your classes, assignments, and students from one place.</p>
</div>""",
        unsafe_allow_html=True,
    )
    footer_dashboard()


def format_teacher_name(email):
    if "@" not in email:
        return "Teacher"
    name_part = email.split("@", 1)[0]
    name_part = name_part.replace(".", " ").replace("_", " ")
    cleaned = " ".join(chunk for chunk in name_part.split(" ") if chunk)
    return cleaned.title() or "Teacher"