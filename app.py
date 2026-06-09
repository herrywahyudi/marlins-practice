# ── Streamlit Cloud Secrets ──────────────────────────────
# Paste this into: share.streamlit.io → your app → Settings → Secrets
# Remove this comment block before saving.

# Your Anthropic API key
ANTHROPIC_API_KEY = "sk-ant-your-key-here"

# Option A — Single shared password (simplest)
# All candidates use the same password
APP_PASSWORD = "CTI2025"

# Option B — Individual usernames + passwords (more secure)
# Add as many candidates as needed
# Passwords must be SHA-256 hashed, OR use plain text (less secure)
# To generate a hash: https://emn178.github.io/online-tools/sha256.html
# Plain text example (works but less secure):
[users]
john = "password123"
maria = "seafarer2025"
admin = "ctiindonesia"
