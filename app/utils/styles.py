import streamlit as st


def apply_styling():
    st.markdown("""
        <style>
        .stApp {
            background-color: #f8fafc;
        }
        h1, h2, h3, h4 {
            font-family: 'Segoe UI', sans-serif;
        }
        div[data-testid="stMarkdownContainer"] > div {
            transition: transform 0.2s ease;
        }
        </style>
    """, unsafe_allow_html=True)


def render_hero_section(title: str, subtitle: str):
    st.markdown(f"""
        <div style="
            background: linear-gradient(90deg, #1e40af, #2563eb);
            padding: 40px;
            border-radius: 16px;
            text-align: center;
            margin-bottom: 2rem;
        ">
            <h1 style="color: white; margin: 0;">{title}</h1>
            <p style="color: #dbeafe; font-size: 1.1rem; margin-top: 8px;">{subtitle}</p>
        </div>
    """, unsafe_allow_html=True)