import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

# =========================
# Load Model
# =========================

model = joblib.load("fraud_model.pkl")
columns = joblib.load("columns.pkl")

# =========================
# Page Config
# =========================

st.set_page_config(
    page_title="Credit Card Fraud Detector",
    page_icon="💳",
    layout="wide"
)

# =========================
# Header
# =========================

st.title("💳 Credit Card Fraud Detection System")

st.markdown(
    """
    Upload a CSV file containing transaction data and detect
    fraudulent credit card transactions using the trained
    XGBoost model.
    """
)

# =========================
# Sidebar
# =========================

st.sidebar.title("About")

st.sidebar.info(
    """
    Model: XGBoost

    Dataset Size: 284,807 Transactions

    ROC-AUC Score: 0.9788

    Fraud Detection using Machine Learning
    """
)

# =========================
# Upload File
# =========================

uploaded_file = st.file_uploader(
    "📂 Upload CSV File",
    type=["csv"]
)

# =========================
# Prediction
# =========================

if uploaded_file is not None:

    try:

        # Read file
        df = pd.read_csv(uploaded_file)

        st.subheader("📄 Uploaded Dataset")

        st.dataframe(
            df.head(),
            use_container_width=True
        )

        # Select required columns
        df = df[columns]

        # Predictions
        predictions = model.predict(df)

        probabilities = model.predict_proba(df)[:, 1]

        # Create result dataframe
        result = df.copy()

        result["Fraud_Prediction"] = predictions

        result["Fraud_Probability"] = probabilities

        # Convert labels
        result["Fraud_Prediction"] = result[
            "Fraud_Prediction"
        ].map({
            0: "Normal",
            1: "Fraud"
        })

        # Sort by risk
        result = result.sort_values(
            by="Fraud_Probability",
            ascending=False
        )

        # =========================
        # Metrics
        # =========================

        fraud_count = (
                result["Fraud_Prediction"] == "Fraud"
        ).sum()

        normal_count = (
                result["Fraud_Prediction"] == "Normal"
        ).sum()

        st.subheader("📊 Summary")

        col1, col2 = st.columns(2)

        col1.metric(
            "🚨 Fraud Transactions",
            fraud_count
        )

        col2.metric(
            "✅ Normal Transactions",
            normal_count
        )

        # =========================
        # Pie Chart
        # =========================

        st.subheader("📈 Transaction Distribution")

        fig, ax = plt.subplots(figsize=(5, 5))

        ax.pie(
            [normal_count, fraud_count],
            labels=["Normal", "Fraud"],
            autopct="%1.1f%%"
        )

        st.pyplot(fig)

        # =========================
        # Top Risk Transactions
        # =========================

        st.subheader("⚠️ Top Risk Transactions")

        st.dataframe(
            result[
                [
                    "Amount",
                    "Fraud_Prediction",
                    "Fraud_Probability"
                ]
            ].head(20),
            use_container_width=True
        )

        # =========================
        # Fraud Transactions
        # =========================

        st.subheader("🚨 Detected Fraud Transactions")

        frauds = result[
            result["Fraud_Prediction"] == "Fraud"
            ]

        if len(frauds) > 0:

            st.dataframe(
                frauds,
                use_container_width=True
            )

        else:

            st.success(
                "No Fraud Transactions Detected."
            )

        # =========================
        # Full Dataset
        # =========================

        with st.expander(
                "🔍 View Full Prediction Dataset"
        ):

            st.dataframe(
                result,
                use_container_width=True
            )

        # =========================
        # Download Results
        # =========================

        csv = result.to_csv(
            index=False
        )

        st.download_button(
            label="📥 Download Prediction Results",
            data=csv,
            file_name="fraud_predictions.csv",
            mime="text/csv"
        )

    except Exception as e:

        st.error(
            f"Error: {e}"
        )