"""
AI Assistant Page - EMIPredict AI
Interactive project knowledge assistant.
"""

import streamlit as st
import time
import sys
import os
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

try:
    from utils.styles import apply_styling
    apply_styling()
except Exception:
    pass

st.markdown("""
<style>
html, body, .stApp { background-color: #f8fafc !important; color: #0f172a !important; }
section[data-testid="stSidebar"] { background-color: #0f172a !important; color: #f8fafc !important; }
section[data-testid="stSidebar"] div[role="radiogroup"] > label { color: #f8fafc !important; }
</style>
""", unsafe_allow_html=True)

st.markdown("## 🤖 Project AI Assistant")
st.markdown("Your personal guide to understanding Financial Risk Assessment.")

qa_knowledge_base = {
    "What is EMI Eligibility?":
        "EMI Eligibility measures a borrower's ability to repay a loan without financial stress. "
        "It considers income, debts, credit score, and job stability.",

    "Why EMI calculator may fail?":
        "The calculator may fail if inputs are invalid (e.g., zero income) or if models encounter unexpected patterns. "
        "Strict validation ensures realistic inputs before processing.",

    "How does credit score affect eligibility?":
        "Credit score is critical. Scores above 740 significantly improve eligibility. "
        "Scores below 600 usually result in rejection or high-risk classification.",

    "What is safe EMI?":
        "Safe EMI is the maximum monthly installment you can pay without compromising essential expenses.",

    "How is max EMI calculated?":
        "Calculated using a XGBoost Regression model combined with financial logic rules.",

    "Why expenses matter?":
        "Higher expenses reduce disposable income, increasing Debt-to-Income ratio and financial risk.",

    "What models are used?":
        "Hybrid approach:\n"
        "• XGBoost Classifier → Eligibility Status\n"
        "• XGBoost Regressor → Safe EMI Value",

    "How accurate is this system?":
        "Validated with 94% classification accuracy and R² Score of 0.89 for EMI estimation.",

    "What causes high-risk status?":
        "Low credit score (<650), high DTI (>50%), or unstable employment history.",

    "Can eligibility be improved?":
        "Improve eligibility by reducing EMIs, increasing tenure, improving credit score, or adding co-applicant.",

    "Is this system used in real banks?":
        "This is a production-grade prototype similar to systems used by FinTechs and Neo-banks."
}


def get_bot_response(user_input):
    user_input = user_input.lower()

    for question, answer in qa_knowledge_base.items():
        if user_input in question.lower():
            return answer

    if "fail" in user_input or "error" in user_input:
        return qa_knowledge_base["Why EMI calculator may fail?"]
    elif "eligible" in user_input:
        return qa_knowledge_base["What is EMI Eligibility?"]
    elif "score" in user_input:
        return qa_knowledge_base["How does credit score affect eligibility?"]
    elif "safe" in user_input:
        return qa_knowledge_base["What is safe EMI?"]
    elif "expenses" in user_input:
        return qa_knowledge_base["Why expenses matter?"]
    elif "risk" in user_input:
        return qa_knowledge_base["What causes high-risk status?"]
    elif "calculate" in user_input or "max" in user_input:
        return qa_knowledge_base["How is max EMI calculated?"]
    elif "accuracy" in user_input:
        return qa_knowledge_base["How accurate is this system?"]
    elif "improve" in user_input:
        return qa_knowledge_base["Can eligibility be improved?"]
    elif "work" in user_input or "models" in user_input:
        return qa_knowledge_base["What models are used?"]
    elif "hello" in user_input or "hi" in user_input:
        return "Hello! I am your EMIPredict Assistant. Ask me about eligibility, risk factors, or AI models."
    else:
        return (
            "I believe you're asking about the system. "
            + qa_knowledge_base["What models are used?"]
            + "\n\nTry asking: 'How accurate is this system?'"
        )


if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi! Ask me anything about EMIPredict AI."}
    ]

col1, col2 = st.columns([1, 3])

with col1:
    st.markdown("### 📌 Common Questions")
    for q in qa_knowledge_base.keys():
        st.markdown(f"- {q}")

with col2:
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    if prompt := st.chat_input("Ask about the project logic..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)

        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            response_text = get_bot_response(prompt)

            for chunk in response_text.split():
                full_response += chunk + " "
                time.sleep(0.03)
                message_placeholder.write(full_response + "▌")

            message_placeholder.write(full_response)

        st.session_state.messages.append(
            {"role": "assistant", "content": full_response}
        )