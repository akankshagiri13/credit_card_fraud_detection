import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Fraud Detection Dashboard",
    layout="wide"
)

st.title("Credit Card Fraud & Anomaly Detection Dashboard")

uploaded_file = st.file_uploader(
    "Upload transaction dataset",
    type=["csv"]
)

if uploaded_file is not None:

    # Load dataset
    df = pd.read_csv(uploaded_file)

    st.success("Dataset loaded successfully")

    # Dashboard metrics
    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Transactions",
        len(df)
    )

    col2.metric(
        "Normal",
        (df["Class"] == 0).sum()
    )

    col3.metric(
        "Fraud",
        (df["Class"] == 1).sum()
    )

    # Display transaction data
    st.subheader("Transaction Data")

    st.dataframe(df.head(100))

    # Transaction distribution graph
    st.subheader("Transaction Distribution")

    counts = df["Class"].value_counts()

    fig, ax = plt.subplots()

    ax.bar(
        ["Normal", "Fraud"],
        [counts.get(0, 0), counts.get(1, 0)]
    )

    ax.set_ylabel("Transactions")
    ax.set_xlabel("Transaction Type")
    ax.set_title("Normal vs Fraud Transactions")

    st.pyplot(fig)

else:
    st.info("Please upload a CSV dataset to view the dashboard.")