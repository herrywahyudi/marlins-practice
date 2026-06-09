import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(
    page_title="Seafarer English Practice Test",
    page_icon="⚓",
    layout="wide"
)

# ── API KEY ────────────────────────────────────────────────
api_key = ""
try:
    api_key = st.secrets["ANTHROPIC_API_KEY"]
except Exception:
    pass

if not api_key:
    with st.sidebar:
        st.markdown("### 🔑 API Key required")
        api_key = st.text_input(
            "Enter your Anthropic API key",
            type="password",
            placeholder="sk-ant-...",
            help="Get your key at console.anthropic.com"
        )

# ── SIDEBAR ────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## ⚓ Seafarer English Practice")
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
        "or any official testing body. All questions are AI-generated originals."
    )

# ── MAIN ───────────────────────────────────────────────────
if not api_key:
    st.warning("Please enter your Anthropic API key in the sidebar to start the test.")
    st.info("💡 Get your API key at [console.anthropic.com](https://console.anthropic.com)")
    st.stop()

# Load HTML template and inject API key
template_path = os.path.join(os.path.dirname(__file__), "test_template.html")
with open(template_path, "r", encoding="utf-8") as f:
    html_content = f.read()

# Safely inject the API key
html_content = html_content.replace("__ANTHROPIC_API_KEY__", api_key)

components.html(html_content, height=920, scrolling=True)

st.markdown(
    "<div style='text-align:center;font-size:11px;color:#aaa;margin-top:1rem'>"
    "Practice tool only — not affiliated with ICS Marlins or any official testing body. "
    "All questions are AI-generated originals."
    "</div>",
    unsafe_allow_html=True
)
