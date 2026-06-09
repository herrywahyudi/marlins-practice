# ⚓ Seafarer English Practice Test

AI-powered Marlins-style maritime English practice assessment. Every session generates unique questions — no two tests are ever the same.

> **Practice tool only — not affiliated with ICS Marlins or any official testing body.**

## What it does

- 85 questions across 6 sections (or 50 for Cruise Ship Staff)
- Exact Marlin test structure: Listening · Grammar · Vocabulary · Sounds · Reading · Numbers
- AI generates fresh questions every session — candidates cannot memorise answers
- Results include percentage score, readiness band, section breakdown, weakness analysis, and personalised study plan

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

Create `.streamlit/secrets.toml`:
```toml
ANTHROPIC_API_KEY = "sk-ant-your-key-here"
```

## Deploy to Streamlit Cloud

1. Push this repo to GitHub: `herrywahyudi/marlins-practice`
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Click **New app** → select `herrywahyudi/marlins-practice` → `main` → `app.py`
4. Click **Advanced settings** → **Secrets** → paste:
   ```toml
   ANTHROPIC_API_KEY = "sk-ant-your-key-here"
   ```
5. Click **Deploy**

## Test structure

| Section | Seafarer | Cruise |
|---|:-:|:-:|
| Listening Comprehension | 25 | 14 |
| Grammar | 30 | 19 |
| Vocabulary | 15 | 12 |
| Different Sounds & Pronunciation | 9 | — |
| Reading Comprehension | 1 passage | 1 passage |
| Time & Numbers | 5 | 4 |
| **Total** | **85** | **50** |

## Push to GitHub

```bash
cd marlins-practice
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/herrywahyudi/marlins-practice.git
git push -u origin main
```
