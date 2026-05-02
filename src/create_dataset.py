import pandas as pd
import random

positive = [
    "I love this product",
    "This is amazing",
    "Really good experience",
    "I am very happy",
    "Excellent service",
    "Fantastic quality"
]

negative = [
    "This is bad",
    "I hate this",
    "Worst experience",
    "Very disappointing",
    "Terrible service",
    "Awful product"
]

neutral = [
    "It is okay",
    "Average experience",
    "Nothing special",
    "It works fine",
    "Just normal",
    "Not bad not good"
]

# ⚠️ MIXED / CONFUSING DATA (VERY IMPORTANT)
mixed = [
    ("I love the product but delivery was bad", "neutral"),
    ("The service is good but product is bad", "neutral"),
    ("Amazing quality but too expensive", "neutral"),
    ("Bad experience but support was helpful", "neutral"),
    ("Good but could be better", "neutral"),
    ("Not great not terrible", "neutral"),
    ("I like it but not perfect", "neutral"),
    ("Decent but has issues", "neutral")
]

data = []

for _ in range(100):
    data.append([random.choice(positive), "positive"])
    data.append([random.choice(negative), "negative"])
    data.append([random.choice(neutral), "neutral"])

# add mixed samples
for text, label in mixed:
    data.append([text, label])

df = pd.DataFrame(data, columns=["text", "sentiment"])
df.to_csv("data/social_media_data.csv", index=False)

print("Final realistic dataset created!")