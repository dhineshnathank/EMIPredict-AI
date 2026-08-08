# EMIPredict AI — Intelligent Financial Risk Assessment Platform

A FinTech capstone project that predicts **EMI eligibility** (classification) and **maximum safe monthly EMI** (regression) from a 400,000-record financial dataset, with full MLflow experiment tracking and a multi-page Streamlit application.

**Live App:** _add your Streamlit Cloud URL here_
**Repository:** https://github.com/dhineshnathank/EMIPredict-AI

---

## Overview

Financial institutions often struggle with manual, inconsistent loan underwriting. EMIPredict AI automates this using machine learning to:

- Classify applicants into **Eligible / High_Risk / Not_Eligible**
- Predict the **maximum safe monthly EMI** an applicant can afford

Built for the FinTech and Banking domain, this project follows a complete ML lifecycle — from raw data to a production-deployed web application.

---

## Problem Statement

People often struggle to repay EMIs due to poor financial planning and inadequate risk assessment. EMIPredict AI addresses this by providing data-driven, real-time risk assessment for financial institutions, FinTech companies, banks, and loan officers.

---

## Dataset

- **404,800 records**, 27 columns (22 input features + engineered features)
- **5 EMI scenarios:** E-commerce Shopping, Home Appliances, Vehicle, Personal Loan, Education
- **Classification target:** `emi_eligibility` (Eligible / High_Risk / Not_Eligible)
- **Regression target:** `max_monthly_emi` (500–50,000 INR)

---

## Approach

1. **Data Cleaning** — fixed malformed numeric strings, imputed missing values (<1.1%), standardized categorical fields
2. **Feature Engineering** — derived `debt_to_income`, `expense_to_income`, `affordability_ratio`; one-hot encoded categoricals; scaled numeric features
3. **Model Training** — 3 classification models (Logistic Regression, Random Forest, XGBoost) and 3 regression models (Linear Regression, Random Forest, XGBoost), all tracked in MLflow
4. **Model Selection** — best models registered in the MLflow Model Registry
5. **Application Development** — 6-page Streamlit app for predictions, insights, monitoring, and admin operations
6. **Cloud Deployment** — deployed on Streamlit Cloud with GitHub CI/CD

---

## Model Performance

### Classification (EMI Eligibility)

| Model | Accuracy | High_Risk Recall | High_Risk Precision | Notes |
|---|---|---|---|---|
| Logistic Regression | 87.96% | — | — | Baseline |
| Random Forest (balanced) | 87.34% | 67% | 23% | Class-weighted |
| **XGBoost (balanced) — Final** | 88.34% | **94%** | 27% | Selected for deployment |

The balanced XGBoost model was chosen for production despite a lower headline accuracy than unbalanced alternatives, because it catches far more actual High_Risk applicants (94% recall vs. as low as 12% recall in unbalanced runs) — critical for a risk-assessment use case where missing a high-risk applicant is costlier than a false positive.

### Regression (Maximum Safe EMI)

| Model | RMSE (INR) | MAE (INR) | R² |
|---|---|---|---|
| Linear Regression | 4,143.80 | 2,982.15 | 0.716 |
| Random Forest Regressor | 1,046.84 | 367.98 | 0.982 |
| **XGBoost Regressor — Final** | **836.97** | 348.97 | **0.988** |

XGBoost Regressor meets the project's target of RMSE under 2,000 INR.

---

## Application Pages

| Page | Description |
|---|---|
| 🏠 **Home** | Project overview and capabilities |
| 🧮 **EMI Calculator** | Real-time eligibility and max-EMI predictions from user input |
| 📊 **Data Insights** | Exploratory data analysis and visualizations |
| 📈 **Model Performance** | MLflow experiment tracking dashboard and model registry view |
| 🗂️ **Data Management** | CRUD interface for managing the underlying dataset |
| 🤖 **AI Assistant** | Q&A chatbot for questions about the project and its models |

---

## Tech Stack

- **Language:** Python
- **ML:** scikit-learn, XGBoost
- **Experiment Tracking:** MLflow (SQLite backend, model registry)
- **App Framework:** Streamlit
- **Data Processing:** pandas, NumPy
- **Visualization:** Matplotlib, Seaborn
- **Deployment:** Streamlit Cloud, GitHub CI/CD

---

## Project Structure

```
EMIPredict-AI/
├── app/
│   ├── main.py              # Navigation entry point
│   ├── Home.py
│   ├── EMI_Calculator.py
│   ├── Data_Insights.py
│   ├── Model_Performance.py
│   ├── Data_Management.py
│   ├── AI_Assistant.py
│   └── utils/
│       ├── model_loader.py
│       ├── preprocessing.py
│       └── styles.py
├── Data/
│   └── emi_prediction_dataset.csv
├── data/
│   └── emi_cleaned.csv
├── models/
│   ├── emi_eligibility_classifier.pkl
│   ├── max_emi_regressor.pkl
│   ├── label_encoder.pkl
│   └── feature_scaler.pkl
├── mlruns/
│   └── mlflow.db
├── notebooks/
├── requirements.txt
└── README.md
```

---

## Running Locally

```bash
# Clone the repo
git clone https://github.com/dhineshnathank/EMIPredict-AI.git
cd EMIPredict-AI

# Create and activate a virtual environment
python -m venv .venv
.venv\Scripts\Activate.ps1      # Windows PowerShell

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app/main.py
```

---

## Deployment

The app is deployed on **Streamlit Cloud**, connected directly to this GitHub repository's `main` branch. Any push to `main` triggers an automatic redeploy.

**Main file path:** `app/main.py`

---

## Key Design Decisions

- **Balanced vs. unbalanced classification models:** chose the balanced XGBoost classifier for deployment to maximize detection of High_Risk applicants, prioritizing recall on the minority class over overall accuracy.
- **MLflow SQLite backend:** experiment tracking data is stored in a small SQLite database (`mlruns/mlflow.db`), force-tracked in git so the Model Performance dashboard works both locally and on Streamlit Cloud, while large model artifact binaries remain excluded to keep the repository lightweight.
- **Cross-platform path handling:** all file paths in the app are resolved relative to each script's location rather than hardcoded, to ensure compatibility between local Windows development and Streamlit Cloud's Linux environment.

---

## Author

**Dhinesh**
Data Analytics | Business Intelligence | Machine Learning
