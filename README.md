# 📰 Fake News Detection System

A Machine Learning based web application that predicts whether a given news article is **Real News** or **Fake News**.

The application is built using **Python, Scikit-learn, TF-IDF, Logistic Regression, and Streamlit**.

---

## 🚀 Features

* 📰 Enter a news title and article text
* 🤖 Predicts Real News or Fake News
* 📈 Displays prediction confidence for each article
* 📊 Displays overall model performance
* 🎯 Shows Accuracy, Precision, Recall, and F1-Score
* 🗑️ Clear button to reset the input
* ⚠️ Provides a disclaimer that predictions are not definitive fact checks

---

## 🧠 Machine Learning

The project uses:

* **TF-IDF Vectorization** for converting text into numerical features
* **Logistic Regression** for binary classification
* **Scikit-learn** for model training and evaluation
* **Joblib** for saving and loading the trained model

---

## 📊 Model Performance

The model was evaluated on a separate test dataset.

| Metric    |      Score |
| --------- | ---------: |
| Accuracy  | **95.69%** |
| Precision | **95.70%** |
| Recall    | **95.69%** |
| F1-Score  | **95.69%** |

---

## 🗂️ Project Structure

```text
Fake-News-Detection/
│
├── Data/
│   └── WELFake_Dataset.csv
│
├── Model/
│   ├── fake_news_model.pkl
│   └── metrics.json
│
├── Notebooks/
│   └── Fake_news_prediction.ipynb
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

> The dataset is not included in the GitHub repository because of its large size.

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* TF-IDF
* Logistic Regression
* Joblib
* Streamlit
* Jupyter Notebook
* Git & GitHub

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/Tirthahazra/Fake-News-Detection.git
```

### 2. Navigate to the project

```bash
cd Fake-News-Detection
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
python -m streamlit run app.py
```

The application will open in your browser.

---

## 📌 Important Note

This project is a Machine Learning based text classification system. It does not independently verify news using external sources or fact-checking databases.

The prediction should therefore be treated as a model-based classification rather than a definitive statement about whether a news article is factually true or false.

---

## 👨‍💻 Author

**Tirtha Hazra**

Computer Science & Engineering
