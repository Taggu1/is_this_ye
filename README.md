# 🌊 The Ye-mometer: Kanye West Quote Classifier

**The Ye-mometer** is an end-to-end Data Science project designed to distinguish the iconic, often controversial linguistic style of Kanye West from other general quotes. By leveraging Natural Language Processing (NLP) and Machine Learning, this project analyzes sentence structure and vocabulary to guess: *"Would Kanye say this?"*

## 🚀 Project Overview

This project covers the entire data science lifecycle:

1. **Data Collection:** Scraping and cleaning Kanye's tweets and general quotes.
2. **Preprocessing:** Using Regular Expressions (Regex) to remove social media noise.
3. **NLP Pipeline:** Vectorizing text using TF-IDF.
4. **Modeling:** Training a Multinomial Naive Bayes classifier.
5. **Deployment:** A Streamlit web application for real-time predictions.

## 📊 The Dataset

* **Kanye Data:** Tweets from Kanye West (up to 2020) sourced from Kaggle.
* **Non-Kanye Data:** A balanced sample of generic quotes to provide a "baseline" for the model.
* **Total Samples:** ~44,000 labeled rows (Balanced 50/50).

## 🛠️ Tech Stack

* **Language:** Python
* **Data Analysis:** `Pandas`, `NumPy`
* **Visualization:** `Matplotlib`, `Seaborn`
* **Machine Learning:** `Scikit-Learn` (Pipeline, TfidfVectorizer, Naive Bayes)
* **Text Cleaning:** `re` (Regular Expressions)

## 🧹 Data Cleaning Process

To ensure the model learns Kanye's *voice* rather than Twitter artifacts, the following were removed:

* **URLs/Links:** Removed via Regex.
* **Hashtags:** Stripped to prevent "keyword cheating" (e.g., #KanyeWest).
* **Promotional Spam:** Built a custom "Ad-Exterminator" to remove tweets containing "50% OFF," "Limited offer," and "Buy now."
* **Short Junk:** Deleted rows with fewer than 15 characters.

## 📈 Model Performance

* **Accuracy:** ~92% on the test set.
* **Insights:** The model successfully identifies high-weight "Ye" keywords such as *God, Love, Vision, Yeezy,* and *Presidential*.

## 💻 How to use the Model

You can use the exported `kanye_model.pkl` to make predictions in any Python environment:

```python
import joblib

# Load the brain
model = joblib.load('kanye_model.pkl')

def guess_ye(phrase):
    prediction = model.predict([phrase])
    return "🔥 That sounds like Ye!" if prediction[0] == 1 else "🤷 Probably not Kanye."

print(guess_ye("I am a god"))

```

## 🗺️ Roadmap

* [x] Data cleaning and Ad-removal
* [x] Balanced dataset training
* [x] Export model via Joblib
* [x] Build Streamlit UI with tabs for "Predictor" and "Data Insights"
* [x] Deploy to Streamlit Cloud