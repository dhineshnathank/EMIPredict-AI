import mlflow
import pandas as pd
import streamlit as st
import sys
import os
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))


st.title("📈 Model Performance")
st.markdown("MLflow experiment tracking results for all trained models.")

mlflow.set_tracking_uri(
    "sqlite:///D:/Code/Project/EMIPredict-AI/mlruns/mlflow.db")
client = mlflow.tracking.MlflowClient()

EXPERIMENT_NAME = "EMIPredict_Classification_final"
REGRESSION_RUN_NAMES = ["Linear_Regression", "Random_Forest_Regressor", "XGBoost_Regressor"]


@st.cache_data
def get_all_runs():
    exp = client.get_experiment_by_name(EXPERIMENT_NAME)
    if exp is None:
        return pd.DataFrame()
    runs = client.search_runs(exp.experiment_id, order_by=[
                              "start_time DESC"], max_results=100)
    rows = []
    for r in runs:
        row = {"run_name": r.data.tags.get(
            "mlflow.runName", "unnamed"), "run_id": r.info.run_id}
        row.update(r.data.metrics)
        rows.append(row)
    return pd.DataFrame(rows)


all_runs_df = get_all_runs()

st.subheader("🏷️ Classification Models")
if not all_runs_df.empty:
    clf_df = all_runs_df[~all_runs_df['run_name'].isin(REGRESSION_RUN_NAMES)]
    st.dataframe(clf_df, use_container_width=True)
else:
    st.info("No classification runs found.")

st.subheader("📉 Regression Models")
if not all_runs_df.empty:
    reg_df = all_runs_df[all_runs_df['run_name'].isin(REGRESSION_RUN_NAMES)]
    st.dataframe(reg_df, use_container_width=True)
else:
    st.info("No regression runs found.")

st.markdown("---")
st.subheader("🏆 Registered Models (Model Registry)")

for name in ["EMI_Eligibility_Classifier", "Max_EMI_Regressor"]:
    st.markdown(f"**{name}**")
    versions = client.search_model_versions(f"name='{name}'")
    for v in versions:
        st.write(
            f"- Version {v.version} | Run ID: `{v.run_id}` | Stage: {v.current_stage or 'None'}")