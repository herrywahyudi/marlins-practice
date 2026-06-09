import streamlit as st
import streamlit.components.v1 as components
import os
import hashlib

st.set_page_config(
    page_title="Seafarer English Practice Test",
    page_icon="⚓",
    layout="wide"
)

# ── HELPERS ────────────────────────────────────────────────
def hash_pw(pw):
    return hashlib.sha256(pw.encode()).hexdigest()

def check_login(username, password):
    u = username.strip().lower()
    pw = password.strip()

    # Try individual users dict in secrets
    try:
        stored = st.secrets["users"].get(u)
        if stored and (stored == pw or stored == hash_pw(pw)):
            return True
    except Exception:
        pass

    # Try single shared password
    try:
        if pw == st.secrets["APP_PASSWORD"]:
            return True
    except Exception:
        pass

    return False

# ── SESSION STATE ──────────────────────────────────────────
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "login_name" not in st.session_state:
    st.session_state.login_name = ""

# ── LOGIN SCREEN ───────────────────────────────────────────
if not st.session_state.logged_in:
    st.markdown("""
    <style>
    [data-testid="stSidebar"] {display:none}
    .block-container {padding-top: 3rem}
    </style>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1.2, 1])
    with col2:
        st.markdown(
            "<div style='text-align:center;margin-bottom:2rem'>"
            "<div style='font-size:44px'>⚓</div>"
            "<h2 style='font-size:22px;font-weight:600;margin:10px 0 4px;color:#0d3b6e'>"
            "Seafarer English Practice Test</h2>"
            "<p style='font-size:13px;color:#888;margin:0'>"
            "CTI Indonesia &mdash; Candidate Assessment Portal</p>"
            "</div>",
            unsafe_allow_html=True
        )

        with st.form("login_form"):
            username = st.text_input("Username", placeholder="Enter your username")
            password = st.text_input("Password", type="password", placeholder="Enter your password")
            submitted = st.form_submit_button("Sign in →", use_container_width=True)

            if submitted:
                if not username or not password:
                    st.error("Please enter both username and password.")
                elif check_login(username, password):
                    st.session_state.logged_in = True
                    st.session_state.login_name = username.strip().lower()
                    st.rerun()
                else:
                    st.error("Incorrect username or password.")

        st.markdown(
            "<div style='text-align:center;margin-top:1.5rem;font-size:11px;color:#aaa'>"
            "Contact your CTI recruiter if you need access.<br>"
            "Practice tool only — not affiliated with ICS Marlins."
            "</div>",
            unsafe_allow_html=True
        )
    st.stop()

# ── API KEY ────────────────────────────────────────────────
api_key = ""
try:
    api_key = st.secrets["ANTHROPIC_API_KEY"]
except Exception:
    pass

# ── SIDEBAR ────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## ⚓ Seafarer English Practice")
    st.markdown(f"👤 **{st.session_state.login_name}**")
    st.divider()
    st.markdown(
        "AI-generated questions every session — no two tests are the same. "
        "Structured to match the official Marlin-style competency test format."
    )
    st.divider()
    st.markdown("**Test structure**")
    st.markdown("""
| Section | Seafarer | Cruise |
|---|:-:|:-:|
| Listening | 25 | 14 |
| Grammar | 30 | 19 |
| Vocabulary | 15 | 12 |
| Sounds | 9 | — |
| Reading | 1 | 1 |
| Numbers | 5 | 4 |
| **Total** | **85** | **50** |
""")
    st.divider()
    st.caption(
        "⚠️ Practice tool only. Not affiliated with ICS Marlins "
        "or any official testing body."
    )
    st.divider()
    if st.button("🚪 Sign out", use_container_width=True):
        st.session_state.logged_in = False
        st.session_state.login_name = ""
        st.rerun()

# ── MAIN ───────────────────────────────────────────────────
if not api_key:
    st.warning("⚠️ API key not configured. Add ANTHROPIC_API_KEY to Streamlit secrets.")
    st.stop()

template_path = os.path.join(os.path.dirname(__file__), "test_template.html")
with open(template_path, "r", encoding="utf-8") as f:
    html_content = f.read()

html_content = html_content.replace("__ANTHROPIC_API_KEY__", api_key)

components.html(html_content, height=920, scrolling=True)

st.markdown(
    "<div style='text-align:center;font-size:11px;color:#aaa;margin-top:1rem'>"
    "Practice tool only — not affiliated with ICS Marlins or any official testing body."
    "</div>",
    unsafe_allow_html=True
)
