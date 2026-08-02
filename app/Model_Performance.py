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


@st.cache_data
def get_runs(experiment_name):
    exp = client.get_experiment_by_name(experiment_name)
    if exp is None:
        return pd.DataFrame()
    runs = client.search_runs(exp.experiment_id, order_by=[
                              "start_time DESC"], max_results=50)
    rows = []
    for r in runs:
        row = {"run_name": r.data.tags.get(
            "mlflow.runName", "unnamed"), "run_id": r.info.run_id}
        row.update(r.data.metrics)
        rows.append(row)
    return pd.DataFrame(rows)


st.subheader("🏷️ Classification Models")
clf_df = get_runs("EMIPredict_Classification_final")
if not clf_df.empty:
    st.dataframe(clf_df, use_container_width=True)
else:
    st.info("No classification runs found.")

st.subheader("📉 Regression Models")
reg_df = get_runs("EMIPredict_Classification_final")
reg_df = reg_df[reg_df['run_name'].str.contains(
    'Regress|Regression', case=False, na=False)] if not reg_df.empty else reg_df
if not reg_df.empty:
    st.dataframe(reg_df, use_container_width=True)

st.markdown("---")
st.subheader("🏆 Registered Models (Model Registry)")

for name in ["EMI_Eligibility_Classifier", "Max_EMI_Regressor"]:
    st.markdown(f"**{name}**")
    versions = client.search_model_versions(f"name='{name}'")
    for v in versions:
        st.write(
            f"- Version {v.version} | Run ID: `{v.run_id}` | Stage: {v.current_stage or 'None'}")
