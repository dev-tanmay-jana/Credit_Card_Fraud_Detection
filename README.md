

# 💳 Credit Card Fraud Detection System

[Python](https://www.python.org?utm_source=chatgpt.com) [Streamlit](https://streamlit.io?utm_source=chatgpt.com) [Scikit-learn](https://scikit-learn.org?utm_source=chatgpt.com)

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![ML](https://img.shields.io/badge/Machine%20Learning-Model-green.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-WebApp-red.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## 📌 Overview

This project is a **Machine Learning-based Credit Card Fraud Detection System** that identifies fraudulent transactions using a trained classification model.

It provides a simple and interactive **Streamlit web application** where users can upload transaction data (CSV) and instantly get predictions.

The system is designed to help detect suspicious financial activity and reduce fraudulent transactions in real-world scenarios.

---

## 🚀 Features

* 🔍 Fraud detection using Machine Learning model
* 📂 Upload CSV file for batch prediction
* ⚡ Real-time prediction results
* 📊 Clean and interactive Streamlit UI
* 🧠 Trained on anonymized credit card dataset
* 📉 Handles imbalanced dataset problem
* 💾 Model saved using Joblib for fast inference

---

## 🧰 Tech Stack

* Python 🐍
* Pandas, NumPy
* Scikit-learn 🤖
* Streamlit 🎈
* Joblib
* Matplotlib / Seaborn (for analysis)

---

## 📁 Project Structure

```bash
Credit_Card_Fraud_Detection/
│
├── app.py                  # Streamlit web app
├── fraud_model.pkl         # Trained ML model
├── columns.pkl             # Feature columns used in training
├── requirements.txt        # Dependencies
├── README.md               # Project documentation
│
├── dataset/                # Dataset files (optional)
├── notebooks/              # Model training notebook
└── assets/                 # Images / UI screenshots
```

---

## ⚙️ How It Works

```text
Input Transaction Data (CSV)
            ↓
Data Preprocessing
            ↓
Feature Engineering
            ↓
Trained ML Model (fraud_model.pkl)
            ↓
Prediction (0 = Legit, 1 = Fraud)
            ↓
Streamlit UI Output
```

---

## ▶️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/dev-tanmay-jana/Credit_Card_Fraud_Detection.git
cd Credit_Card_Fraud_Detection
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

### 3️⃣ Activate Environment

**Windows:**

```bash
venv\Scripts\activate
```

**Mac/Linux:**

```bash
source venv/bin/activate
```

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

Then open:

```
http://localhost:8501
```

---

## 🤖 Model Details

* Algorithm: Logistic Regression / Random Forest (update if needed)
* Problem Type: Binary Classification
* Output:

  * `0` → Legitimate Transaction
  * `1` → Fraudulent Transaction

The dataset is highly **imbalanced**, so performance focuses on:

* Precision
* Recall
* F1 Score
* ROC-AUC

---

## 📊 Results

The model is optimized to:

* Detect fraudulent transactions accurately
* Reduce false negatives (critical in fraud detection)
* Maintain high recall for fraud cases

---

## 🖥️ UI Preview

📌 Add screenshot here:

```
credit_card_FraudDetection.png

```

---

## 🔮 Future Improvements

* 🚀 Deploy on Streamlit Cloud / Render
* 🧠 Add XGBoost / LightGBM models
* 🔍 Integrate SHAP for explainability
* 📡 Add real-time API using FastAPI
* ☁️ Docker containerization
* 📊 Advanced dashboard analytics

---

## 👨‍💻 Author

**Tanmay Jana**

* GitHub: [https://github.com/dev-tanmay-jana](https://github.com/dev-tanmay-jana)
* Project: Credit Card Fraud Detection System(https://cardguard-ai.streamlit.app/)

---

## 📜 License

This project is licensed under the MIT License.

---

# ⭐ Pro Tip (Important)

To make your GitHub look **professional like top AI engineers**, do this next:

### Add a banner image:

* 1200×400 “Fraud Detection ML System”

### Add GIF demo:

* Screen recording of Streamlit app

### Add live link:

* Streamlit Cloud deployment

---


