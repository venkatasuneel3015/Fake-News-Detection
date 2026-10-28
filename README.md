# 📰 Fake News Detection System

A Machine Learning-based web application that classifies news articles as **Real News** or **Fake News** using Natural Language Processing (NLP). The application combines TF-IDF feature extraction, Logistic Regression, and Streamlit to provide an interactive interface for news classification and model performance analysis.

This project demonstrates an end-to-end text classification workflow, from textual input and feature engineering to model inference and evaluation.

## 🚀 Key Features

- **News Classification:** Predicts whether an input news article belongs to the Real News or Fake News class.
- **Title and Article Input:** Accepts a news headline and article text for prediction.
- **NLP-Based Feature Extraction:** Converts text into numerical features using TF-IDF vectorization.
- **Confidence Display:** Displays model prediction confidence for the input article, where supported by the application.
- **Performance Evaluation:** Presents model evaluation metrics, including accuracy, precision, recall, and F1-score.
- **Interactive Web Interface:** Provides a user-friendly interface built with Streamlit.
- **Input Reset:** Includes a clear option to reset the input fields.
- **Model Persistence:** Uses Joblib to save and load the trained machine learning pipeline or model artifacts.
- **Responsible Predictions:** Includes a disclaimer explaining that model predictions are not definitive fact checks.

## 🧠 Machine Learning Workflow

The project follows a supervised machine learning workflow for text classification.

1. **Data Preparation:** Uses the WELFake dataset as the source of labeled news articles.
2. **Text Preprocessing:** Prepares the text for feature extraction according to the implemented preprocessing pipeline.
3. **Feature Engineering:** Applies TF-IDF vectorization to transform textual data into numerical representations.
4. **Model Training:** Uses Logistic Regression to learn patterns associated with the target classes.
5. **Model Evaluation:** Evaluates predictive performance using classification metrics on a separate test dataset.
6. **Model Serialization:** Uses Joblib to store and reload trained model artifacts.
7. **Application Deployment:** Integrates the trained model with Streamlit for interactive predictions.

### Model Architecture

```text
News Headline + Article Text
             |
             v
     Text Preprocessing
             |
             v
       TF-IDF Vectorizer
             |
             v
      Logistic Regression
             |
             v
      Classification Output
       /             \
   Real News       Fake News
             |
             v
   Streamlit Results Display
```

*The workflow should match the actual preprocessing and inference steps implemented in `app.py` and the training notebook.*

## 📊 Model Performance

The following metrics are reported for the model evaluated on a separate test dataset.

| Evaluation Metric | Reported Score |
|---|---:|
| Accuracy | 95.69% |
| Precision | 95.70% |
| Recall | 95.69% |
| F1-Score | 95.69% |

**Evaluation note:** These are the currently reported results. Confirm them against the actual evaluation output and `metrics.json` before publishing. The calculation method, class averaging, and test split should be documented for reproducibility.

### Understanding the Metrics

- **Accuracy:** Measures the proportion of test samples classified correctly.
- **Precision:** Measures the proportion of positive predictions that are correct.
- **Recall:** Measures the proportion of actual positive samples identified correctly.
- **F1-Score:** Represents the harmonic mean of precision and recall.

The metrics describe performance on the evaluation dataset and do not guarantee equivalent performance on unseen, real-world news.

## 🛠️ Technology Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Data Processing | Pandas, NumPy |
| Machine Learning | Scikit-learn |
| Natural Language Processing | TF-IDF Vectorization |
| Classification Algorithm | Logistic Regression |
| Model Persistence | Joblib |
| Web Application | Streamlit |
| Development Environment | Jupyter Notebook |
| Version Control | Git, GitHub |

## 📁 Project Structure

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

*The dataset is not included in the repository because of its size. The model files and directory names shown above should match the files actually committed to GitHub.*

## ⚙️ Installation and Setup

### Prerequisites

- Python 3.9 or a compatible version supported by your dependencies
- Git
- pip

### Step 1: Clone the repository

```bash
git clone https://github.com/venkatasuneel3015/Fake-News-Detection.git
```

### Step 2: Navigate to the project directory

```bash
cd Fake-News-Detection
```

### Step 3: Create a virtual environment (recommended)

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**

```bash
python -m venv venv
source venv/bin/activate
```

### Step 4: Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Step 5: Verify required files

Confirm that `app.py`, `requirements.txt`, and the model artifacts required by the application are present.

If the dataset or trained model files are not included, obtain them from the appropriate source or generate them by following the notebook instructions.

### Step 6: Launch the application

```bash
python -m streamlit run app.py
```

Open the local URL displayed in your terminal to access the application.

## 🔍 Example Use Case

1. Launch the Streamlit application.
2. Enter a news headline and article text.
3. Submit the input for classification.
4. Review the predicted class and any confidence information displayed.
5. Examine the model evaluation metrics available in the application.
6. Clear the fields to test another article.

## ⚠️ Limitations and Responsible Use

- **Not a fact-checking engine:** The model classifies text based on patterns learned from labeled training data; it does not independently verify claims against authoritative sources.
- **Dataset dependence:** Predictions may be affected by dataset quality, class balance, and potential biases.
- **Unseen topics:** Articles about unfamiliar subjects, new events, or different writing styles may be misclassified.
- **Confidence interpretation:** Model confidence is not the same as the probability that a news claim is factually true.
- **Generalization:** Performance on a test dataset may differ from performance on real-world news.
- **Model security:** Only load trusted model files, as serialized Python objects can execute malicious code when loaded.

Always verify important news claims using reliable, independent sources.

## 🔮 Future Improvements

Potential enhancements for future versions include:

- Compare Logistic Regression with Naive Bayes, Linear SVM, and transformer-based text classifiers.
- Add a structured text preprocessing and model training pipeline.
- Implement cross-validation and systematic hyperparameter tuning.
- Display a confusion matrix and per-class precision, recall, and F1-score.
- Add data validation and checks for missing or invalid input.
- Evaluate robustness against unfamiliar topics and changing news patterns.
- Integrate trusted external fact-checking sources to support claim verification.
- Deploy the application to a suitable cloud hosting platform.

*These are proposed improvements, not claims about existing functionality.*

## 👨‍💻 Author

**Venkata Suneel R**

B.Tech in Artificial Intelligence & Data Science

- **GitHub:** https://github.com/venkatasuneel3015
- **LinkedIn:** https://www.linkedin.com/in/venkata-suneel-3b6679344/

## 📄 License and Attribution

This repository is maintained for educational and portfolio purposes. Review the original project's license and preserve any required attribution or license notices when redistributing adapted code. Add a license to this repository only after confirming that you have the right to do so.

---

**Skills Demonstrated:** Python · Machine Learning · NLP · Text Classification · Feature Engineering · Model Evaluation · Streamlit · Git & GitHub
