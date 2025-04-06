import json
from datetime import datetime

def log_customer_behavior(review_text):
    behavior_data = {
        "review_length": len(review_text),
        "timestamp": datetime.now().isoformat(),
        "keywords": extract_keywords(review_text),
    }

    try:
        with open("behavior_data.json", "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []

    data.append(behavior_data)

    with open("behavior_data.json", "w") as f:
        json.dump(data, f, indent=4)

def extract_keywords(review):
    keywords = []
    important_words = ["price", "quality", "delivery", "support", "refund", "broken", "amazing", "return", "cheap"]
    for word in important_words:
        if word in review.lower():
            keywords.append(word)
    return keywords
