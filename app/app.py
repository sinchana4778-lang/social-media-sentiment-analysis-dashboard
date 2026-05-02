import streamlit as st
import sys
import os
import matplotlib.pyplot as plt

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.predict import predict_sentiment

st.title("📊 Sentiment Analysis Dashboard")

# Store predictions
if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.text_area("Enter text:")

if st.button("Predict"):
    result = predict_sentiment(user_input)
    
    st.write("### Sentiment:", result)

    # Save history
    st.session_state.history.append(result)

# 📊 GRAPH SECTION
if st.session_state.history:
    st.write("### Sentiment Distribution")

    labels = ["positive", "negative", "neutral"]
    counts = [st.session_state.history.count(l) for l in labels]

    fig, ax = plt.subplots()
    ax.bar(labels, counts)
    ax.set_ylabel("Count")
    ax.set_title("Sentiment Count")

    st.pyplot(fig)