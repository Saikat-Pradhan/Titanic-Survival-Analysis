# 🚢 Titanic Survival Prediction Web App

A smart **Machine Learning–based web application** that predicts whether a passenger would survive the Titanic disaster based on important passenger details.
Built using **Python, Scikit-learn, and Streamlit**, and deployed online for real-time predictions.

---

## 🔗 Live Demo

👉 Try the deployed web app here:
**[(https://titanic-survival-analysis-by-saikat-pradhan.streamlit.app/)]**

---

## 🚀 Project Overview

This project demonstrates how Machine Learning can analyze historical passenger data and predict survival chances on the Titanic.

Users provide passenger details through an interactive web interface, and the trained classification model instantly predicts survival probability.

### ✅ Input Features

* Passenger Class (Pclass)
* Sex
* Age
* Number of Siblings/Spouses Aboard (SibSp)
* Number of Parents/Children Aboard (Parch)
* Port of Embarkation

### 🎯 Output

* ✅ Passenger Likely to Survive
* ❌ Passenger Not Likely to Survive

---

## 🧠 Technologies Used

* Python 🐍
* Streamlit 🌐
* Pandas 📊
* NumPy 📐
* Scikit-learn 🤖
* Pickle 📦

---

## ⚙️ Setup Guide (Run Locally)

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Streamlit App

```bash
streamlit run app.py
```

Then open your browser:

```
http://localhost:8501
```

---

## 📊 Dataset

The model is trained using the **Titanic Dataset**, which includes passenger information such as:

* PassengerId
* Pclass
* Sex
* Age
* SibSp
* Parch
* Fare
* Embarked
* Survival Status

This dataset helps the model learn survival patterns based on passenger characteristics.

---

## 🏗️ Model Training

Model development is performed in:

```
Titanic_Survival_Prediction_Using_Tensorflow.ipynb
```

### Training Steps:

* Data preprocessing
* Handling missing values
* Feature encoding
* Age scaling using StandardScaler
* Model training & evaluation
* Saving trained model using Pickle

Saved Files:

* `titanic_model.pkl` → Trained ML model
* `age_scaler.pkl` → Feature scaler

---

## 🧠 How the App Works

1. User enters passenger information.
2. Age input is scaled using the trained scaler.
3. Inputs are passed to the trained ML model.
4. Model predicts survival outcome.
5. Prediction result is displayed instantly on the UI.

---

## 📁 Project Structure

```
├── app.py
├── titanic_model.pkl
├── age_scaler.pkl
├── requirements.txt
├── Titanic-Dataset.csv
├── Titanic_Survival_Prediction_Using_Tensorflow.ipynb
└── README.md
```

---

## ⭐ Support

If you like this project, don’t forget to **give it a star ⭐ on GitHub!**

It motivates me to build more Machine Learning and AI projects 🚀
