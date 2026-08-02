from utils.styles import apply_styling, render_hero_section
import streamlit as st
import sys
import os
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))


apply_styling()

render_hero_section(
    "EMIPredict AI",
    "Intelligent Financial Risk Assessment Platform"
)

st.markdown("### 🏦 Transforming Financial Decision Making")

st.markdown(
    """
    <div style="font-size: 1.05rem; line-height: 1.7; margin-bottom: 2rem;">
    In the rapidly evolving landscape of <b style="color:#2563eb;">FinTech</b>, accurately assessing loan eligibility and repayment capacity 
    is critical for both lenders and borrowers. <b style="color:#0f172a;">EMIPredict AI</b> bridges the gap between complex financial data 
    and actionable insights using state-of-the-art machine learning algorithms.
    <br><br>
    This platform provides a robust, real-time interface for evaluating credit risk, predicting safe EMI limits, 
    and offering personalized financial recommendations.
    </div>
    """, unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown(
        """
        <div style="background-color:#ffffff; padding:22px; border-radius:14px; border:1px solid #e5e7eb;">
            <h3 style="color:#1e40af;">🚧 The Business Challenge</h3>
            <p>
            <b>High Default Rates:</b> Traditional credit scoring often misses behavioral nuances.<br><br>
            <b>Opaque Processes:</b> Borrowers struggle to understand rejection reasons.<br><br>
            <b>Manual Bottlenecks:</b> Underwriting is slow and difficult to scale.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        """
        <div style="background-color:#ffffff; padding:22px; border-radius:14px; border:1px solid #e5e7eb;">
            <h3 style="color:#15803d;">🚀 The AI Solution</h3>
            <p>
            <b>Automated Risk Assessment:</b> Instant eligibility checks using XGBoost.<br><br>
            <b>Precision Forecasting:</b> 'Max Safe EMI' prediction via XGBoost.<br><br>
            <b>Explainable AI:</b> Transparent reasoning behind every decision.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("### ⚡ Key Capabilities")

cap1, cap2, cap3 = st.columns(3)

cards = [
    ("🛡️", "Risk Classification",
     "Detect high-risk profiles instantly with 94% recall on high-risk cases."),
    ("💰", "Affordability Engine",
     "Calculate the exact maximum EMI a user can safely afford."),
    ("📊", "Interactive Insights",
     "Visualizing 22+ financial features for deeper analysis.")
]

for col, (icon, title, desc) in zip([cap1, cap2, cap3], cards):
    with col:
        st.markdown(f"""
        <div style="background-color:#ffffff; padding:22px; border-radius:14px; text-align:center; border:1px solid #e5e7eb;">
            <div style="font-size: 2rem;">{icon}</div>
            <h4 style="color:#0f172a; margin-top:10px;">{title}</h4>
            <p>{desc}</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("### 🧬 Data & Technology")

st.markdown("""
<div style="background-color:#ffffff; padding:22px; border-radius:14px; border:1px solid #e5e7eb;">
<ul style="line-height:1.8;">
<li><b>Dataset Scale:</b> Trained on <b style="color:#2563eb;">400,000+ financial records</b>.</li>
<li><b>Feature Engineering:</b> 22 key features including Demographics, Employment & DTI ratios.</li>
<li><b>Model Architecture:</b> Hybrid Classification (XGBoost) + Regression (XGBoost).</li>
</ul>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.success(
    "👉 Please use the sidebar to navigate to the **EMI Calculator** for a live demonstration."
)
