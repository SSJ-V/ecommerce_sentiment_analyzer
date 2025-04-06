def predict_age_group(review):
    review = review.lower()

    # Very basic rules just to simulate
    teen_keywords = ["omg", "lit", "slay", "cool", "bruh", "dope", "vibe"]
    young_adult_keywords = ["value", "deal", "fast shipping", "love it", "worth"]
    adult_keywords = ["quality", "durable", "reliable", "useful", "excellent"]
    senior_keywords = ["difficult", "complicated", "hard to use", "slow", "customer support"]

    if any(word in review for word in teen_keywords):
        return "Teen (13-19)"
    elif any(word in review for word in young_adult_keywords):
        return "Young Adult (20-35)"
    elif any(word in review for word in adult_keywords):
        return "Adult (36-55)"
    elif any(word in review for word in senior_keywords):
        return "Senior (56+)"
    else:
        return "Unknown"
