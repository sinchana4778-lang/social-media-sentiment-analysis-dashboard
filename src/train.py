from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import pandas as pd

# Load data
df = pd.read_csv("data/social_media_data.csv")

X = df["text"]
y = df["sentiment"]

# Create pipeline (VERY IMPORTANT)
model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("clf", LogisticRegression(max_iter=200))
])

# 🔥 CROSS VALIDATION (REAL ACCURACY)
scores = cross_val_score(model, X, y, cv=5)

print("Cross Validation Accuracy:", scores)
print("Average Accuracy:", scores.mean())

# Train final model on full data
model.fit(X, y)

import joblib
joblib.dump(model, "models/sentiment_model.pkl")

print("Model trained and saved!")