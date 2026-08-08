import pandas as pd
import streamlit as st
import os

DATA_PATH = r"D:\Code\Project\EMIPredict-AI\data\emi_cleaned.csv"

st.title("🗂️ Data Management")
st.markdown("Administrative interface for viewing, adding, editing, and deleting financial records.")


@st.cache_data
def load_data():
    return pd.read_csv(DATA_PATH)


if "df" not in st.session_state:
    st.session_state.df = load_data()

df = st.session_state.df

tab_view, tab_add, tab_edit, tab_delete = st.tabs(
    ["📋 View Records", "➕ Add Record", "✏️ Edit Record", "🗑️ Delete Record"])

with tab_view:
    st.subheader("All Records")
    st.write(f"Total records: {len(df)}")
    st.dataframe(df, use_container_width=True, height=400)

with tab_add:
    st.subheader("Add New Record")
    with st.form("add_form"):
        new_row = {}
        cols = st.columns(3)
        for i, col in enumerate(df.columns):
            with cols[i % 3]:
                if df[col].dtype == "object":
                    new_row[col] = st.text_input(col)
                else:
                    new_row[col] = st.number_input(col, value=0.0)
        submitted = st.form_submit_button("Add Record")
        if submitted:
            st.session_state.df = pd.concat(
                [df, pd.DataFrame([new_row])], ignore_index=True)
            st.success("Record added.")
            st.rerun()

with tab_edit:
    st.subheader("Edit Record")
    if len(df) > 0:
        row_idx = st.number_input(
            "Row index to edit", min_value=0, max_value=len(df) - 1, step=1)
        with st.form("edit_form"):
            updated_row = {}
            cols = st.columns(3)
            for i, col in enumerate(df.columns):
                with cols[i % 3]:
                    current_val = df.loc[row_idx, col]
                    if df[col].dtype == "object":
                        updated_row[col] = st.text_input(
                            col, value=str(current_val), key=f"edit_{col}")
                    else:
                        updated_row[col] = st.number_input(
                            col, value=float(current_val), key=f"edit_{col}")
            submitted = st.form_submit_button("Update Record")
            if submitted:
                for col, val in updated_row.items():
                    st.session_state.df.loc[row_idx, col] = val
                st.success(f"Record {row_idx} updated.")
                st.rerun()

with tab_delete:
    st.subheader("Delete Record")
    if len(df) > 0:
        del_idx = st.number_input(
            "Row index to delete", min_value=0, max_value=len(df) - 1, step=1, key="del_idx")
        st.dataframe(df.loc[[del_idx]], use_container_width=True)
        if st.button("Delete Record", type="primary"):
            st.session_state.df = df.drop(index=del_idx).reset_index(drop=True)
            st.success(f"Record {del_idx} deleted.")
            st.rerun()

st.markdown("---")
if st.button("💾 Save Changes to CSV"):
    st.session_state.df.to_csv(DATA_PATH, index=False)
    st.success("Changes saved to emi_cleaned.csv.")