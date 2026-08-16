import streamlit as st
import joblib
import json


# -----------------------------
# Load Model and Metrics
# -----------------------------

model = joblib.load("Model/fake_news_model.pkl")

with open("Model/metrics.json", "r") as file:
    metrics = json.load(file)


# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="Fake News Detector",
    page_icon="📰"
)


# -----------------------------
# Header
# -----------------------------

st.title("📰 Fake News Detection System")

st.subheader("AI-powered news classification using Machine Learning")

st.write(
    "Enter a news headline and article text below to check "
    "whether the news is likely to be real or fake."
)

st.divider()


# -----------------------------
# News Input
# -----------------------------
def clear_inputs():
    st.session_state.title_input = ""
    st.session_state.text_input = ""
st.subheader("📝 Enter News")


title = st.text_input(
    "News Title",
    placeholder="Enter the news headline...",
    key="title_input"
)

text = st.text_area(
    "News Text",
    placeholder="Paste the complete news article here...",
    height=250,
    key="text_input"
)


# -----------------------------
# Buttons
# -----------------------------

col1, col2 = st.columns(2)

with col1:
    check_news = st.button(
        "🔍 Check News",
        type="primary",
        use_container_width=True
    )

with col2:
    st.button(
        "🗑️ Clear",
        use_container_width=True,
        on_click=clear_inputs
    )


# -----------------------------
# Prediction
# -----------------------------

if check_news:

    if title.strip() == "" or text.strip() == "":
        st.warning(
            "⚠️ Please enter both the news title and news text."
        )

    else:

        # Combine title and article text
        news = title + " " + text

        # Make prediction
        prediction = model.predict([news])[0]

        # Get prediction probabilities
        probabilities = model.predict_proba([news])[0]

        # Calculate confidence
        if prediction == 1:
            confidence = probabilities[1] * 100
        else:
            confidence = probabilities[0] * 100

        st.divider()

        st.subheader("🎯 Prediction")

        if prediction == 1:
            st.success("Real News 🟢")
        else:
            st.error("Fake News 🔴")

        st.subheader("📈 Prediction Confidence")

        st.progress(int(confidence))

        st.write(f"**{confidence:.2f}%**")


# -----------------------------
# Model Performance
# -----------------------------

st.divider()

st.subheader("📊 Model Performance")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Accuracy",
    f"{metrics['accuracy'] * 100:.2f}%"
)

col2.metric(
    "Precision",
    f"{metrics['precision'] * 100:.2f}%"
)

col3.metric(
    "Recall",
    f"{metrics['recall'] * 100:.2f}%"
)

col4.metric(
    "F1-Score",
    f"{metrics['f1_score'] * 100:.2f}%"
)

st.caption("Performance measured on the test dataset.")


# -----------------------------
# Disclaimer
# -----------------------------

st.divider()

st.info(
    "⚠️ This system is a machine learning prediction tool. "
    "The result should not be considered a definitive judgment of whether "
    "a news article is true or false. Always verify important information "
    "using reliable sources."
)