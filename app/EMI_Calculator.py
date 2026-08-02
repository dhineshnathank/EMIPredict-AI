import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from utils.model_loader import load_classifier, load_regressor, load_label_encoder, load_scaler
from utils.preprocessing import preprocess_input

st.set_page_config(page_title="EMI Calculator", page_icon="🧮", layout="wide")

st.title("🧮 EMI Eligibility & Calculator")
st.markdown("Enter your financial details to check eligibility and your maximum safe EMI.")

with st.form("emi_form"):
    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Personal")
        age = st.number_input("Age", 18, 70, 30)
        gender = st.selectbox("Gender", ["Male", "Female"])
        marital_status = st.selectbox("Marital Status", ["Single", "Married"])
        education = st.selectbox("Education", ["High School", "Graduate", "Post Graduate", "Professional"])
        family_size = st.number_input("Family Size", 1, 15, 3)
        dependents = st.number_input("Dependents", 0, 10, 1)

    with col2:
        st.subheader("Employment & Housing")
        monthly_salary = st.number_input("Monthly Salary (₹)", 0, 500000, 50000)
        employment_type = st.selectbox("Employment Type", ["Private", "Government", "Self-employed"])
        company_type = st.selectbox("Company Type", ["Large Indian", "MNC", "Mid-size", "Small", "Startup"])
        years_of_employment = st.number_input("Years of Employment", 0, 40, 5)
        house_type = st.selectbox("House Type", ["Rented", "Own", "Family"])
        monthly_rent = st.number_input("Monthly Rent (₹)", 0, 100000, 10000)

    with col3:
        st.subheader("Expenses")
        school_fees = st.number_input("School Fees (₹)", 0, 100000, 0)
        college_fees = st.number_input("College Fees (₹)", 0, 100000, 0)
        travel_expenses = st.number_input("Travel Expenses (₹)", 0, 50000, 3000)
        groceries_utilities = st.number_input("Groceries & Utilities (₹)", 0, 50000, 8000)
        other_monthly_expenses = st.number_input("Other Expenses (₹)", 0, 50000, 2000)

    st.subheader("Credit & Loan Request")
    col4, col5, col6 = st.columns(3)

    with col4:
        credit_score = st.number_input("Credit Score", 300, 850, 700)
        existing_loans = st.selectbox("Existing Loans?", ["No", "Yes"])
        current_emi_amount = st.number_input("Current EMI Amount (₹)", 0, 100000, 0)

    with col5:
        bank_balance = st.number_input("Bank Balance (₹)", 0, 5000000, 50000)
        emergency_fund = st.number_input("Emergency Fund (₹)", 0, 2000000, 20000)

    with col6:
        emi_scenario = st.selectbox(
            "EMI Scenario",
            ["E-commerce Shopping EMI", "Home Appliances EMI", "Vehicle EMI", "Personal Loan EMI", "Education EMI"]
        )
        requested_amount = st.number_input("Requested Amount (₹)", 0, 2000000, 100000)
        requested_tenure = st.number_input("Requested Tenure (months)", 1, 84, 12)

    submitted = st.form_submit_button("🔍 Check Eligibility")

if submitted:
    raw_input = {
        'age': age, 'monthly_salary': monthly_salary, 'years_of_employment': years_of_employment,
        'monthly_rent': monthly_rent, 'family_size': family_size, 'dependents': dependents,
        'school_fees': school_fees, 'college_fees': college_fees, 'travel_expenses': travel_expenses,
        'groceries_utilities': groceries_utilities, 'other_monthly_expenses': other_monthly_expenses,
        'current_emi_amount': current_emi_amount, 'credit_score': credit_score,
        'bank_balance': bank_balance, 'emergency_fund': emergency_fund,
        'requested_amount': requested_amount, 'requested_tenure': requested_tenure,
        'gender': gender, 'marital_status': marital_status, 'education': education,
        'employment_type': employment_type, 'company_type': company_type,
        'house_type': house_type, 'existing_loans': existing_loans, 'emi_scenario': emi_scenario,
    }

    scaler = load_scaler()
    le = load_label_encoder()
    clf = load_classifier()
    reg = load_regressor()

    X = preprocess_input(raw_input, scaler)

    pred_class_encoded = clf.predict(X)[0]
    pred_class = le.inverse_transform([pred_class_encoded])[0]
    pred_max_emi = reg.predict(X)[0]

    st.markdown("---")
    st.subheader("📋 Result")

    result_col1, result_col2 = st.columns(2)

    with result_col1:
        if pred_class == "Eligible":
            st.success(f"✅ Eligibility: **{pred_class}**")
        elif pred_class == "High_Risk":
            st.warning(f"⚠️ Eligibility: **{pred_class}**")
        else:
            st.error(f"❌ Eligibility: **{pred_class}**")

    with result_col2:
        st.metric("💰 Maximum Safe Monthly EMI", f"₹{pred_max_emi:,.0f}")