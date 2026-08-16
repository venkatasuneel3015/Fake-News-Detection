# 📰 Fake News Detection System

A Machine Learning-based web application that predicts whether a given news article is likely to be **Real News 🟢** or **Fake News 🔴**.

The application uses **TF-IDF text vectorization** and **Logistic Regression** for classification and is deployed as an interactive **Streamlit** web application.

## 🚀 Features

- 📰 Enter a news headline and article text
- 🤖 Predict Real News or Fake News
- 📈 Display prediction confidence
- 📊 Display model performance
  - Accuracy
  - Precision
  - Recall
  - F1-Score
- 🗑️ Clear input fields
- 📱 Interactive Streamlit interface
- ⚠️ Includes a prediction disclaimer

## 🧠 Machine Learning Approach

The project follows these steps:

1. Load the news dataset
2. Clean and preprocess the text data
3. Combine news title and article text
4. Convert text into numerical features using TF-IDF
5. Train a Logistic Regression classification model
6. Evaluate the model using a separate test dataset
7. Save the trained model using Joblib
8. Build a Streamlit web application
9. Use the saved model to make predictions on new articles

## 📊 Model Performance

The model achieved the following performance on the test dataset:

| Metric | Score |
|---|---:|
| Accuracy | 95.69% |
| Precision | 95.70% |
| Recall | 95.69% |
| F1-Score | 95.69% |

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit
- Jupyter Notebook
- Git & GitHub

## 📁 Project Structure

```text
FAKE_NEWS_DETECTION
│
├── Data
│   └── WELFake_Dataset.csv
│
├── Model
│   ├── fake_news_model.pkl
│   └── metrics.json
│
├── Notebooks
│   └── Fake_news_prediction.ipynb
│
├── app.py
├── README.md
└── requirements.txt