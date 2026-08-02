import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import matplotlib
matplotlib.use("Agg")

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

DATA_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'emi_prediction_dataset.csv'))

st.title("📊 Data Insights")
st.markdown("Exploratory analysis of the EMIPredict AI dataset (400K+ financial records).")

@st.cache_data
def load_data():
    return pd.read_csv(DATA_PATH)

df = load_data()

st.subheader("Dataset Overview")
col1, col2, col3 = st.columns(3)
col1.metric("Total Records", f"{len(df):,}")
col2.metric("Features", df.shape[1])
col3.metric("EMI Scenarios", df['emi_scenario'].nunique())

st.markdown("---")

st.subheader("Eligibility Distribution")
fig, ax = plt.subplots(figsize=(6, 4))
sns.countplot(data=df, x='emi_eligibility', order=df['emi_eligibility'].value_counts().index, ax=ax)
ax.set_xlabel("Eligibility")
ax.set_ylabel("Count")
st.pyplot(fig)

st.subheader("EMI Scenario Distribution")
fig, ax = plt.subplots(figsize=(8, 4))
sns.countplot(data=df, y='emi_scenario', order=df['emi_scenario'].value_counts().index, ax=ax)
ax.set_xlabel("Count")
ax.set_ylabel("Scenario")
st.pyplot(fig)

st.subheader("Monthly Salary Distribution")
fig, ax = plt.subplots(figsize=(8, 4))
sns.histplot(df['monthly_salary'], bins=50, kde=True, ax=ax)
ax.set_xlabel("Monthly Salary (₹)")
st.pyplot(fig)

st.subheader("Credit Score vs Eligibility")
fig, ax = plt.subplots(figsize=(8, 4))
sns.boxplot(data=df, x='emi_eligibility', y='credit_score', ax=ax)
st.pyplot(fig)

st.subheader("Correlation Heatmap (Numeric Features)")
numeric_df = df.select_dtypes(include='number')
fig, ax = plt.subplots(figsize=(12, 8))
sns.heatmap(numeric_df.corr(), cmap='coolwarm', center=0, ax=ax)
st.pyplot(fig)