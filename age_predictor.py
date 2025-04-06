# age_predictor.py

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
import joblib
import os

# 📥 Load dataset
df = pd.read_csv("age_group_dataset.csv")

# ✂️ Split (optional, we train on full data for this small dataset)
X = df["review"]
y = df["age_group"]

# 🔄 Create pipeline
model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("clf", MultinomialNB())
])

# 🎯 Train the model
model.fit(X, y)

# 💾 Save the model
joblib.dump(model, "age_group_model.pkl")

print("✅ Age group model trained and saved.")

# 🎯 Prediction function
def predict_age_group(review_text):
    if os.path.exists("age_group_model.pkl"):
        model = joblib.load("age_group_model.pkl")
        return model.predict([review_text])[0]
    else:
        return "Unknown"
