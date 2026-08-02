import streamlit as st

pg = st.navigation([
    st.Page("Home.py", title="Home", icon="🏠", default=True),
    st.Page("EMI_Calculator.py", title="EMI Calculator", icon="🧮"),
    st.Page("Data_Insights.py", title="Data Insights", icon="📊"),
    st.Page("Model_Performance.py", title="Model Performance", icon="📈"),
    st.Page("AI_Assistant.py", title="AI Assistant", icon="🤖"),
    st.Page("Data_Management.py", title="Data Management", icon="🗂️"),
])

pg.run()