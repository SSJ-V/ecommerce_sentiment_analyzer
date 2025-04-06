from age_predictor import predict_age_group
from database import insert_review, init_db
from customer_behavior import log_customer_behavior
from flask import Flask, request, render_template
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from database import get_all_reviews  

# Initialize the database
init_db()

app = Flask(__name__)
analyzer = SentimentIntensityAnalyzer()

# 🔧 Define custom sentiment weights
custom_words = {
    "trash": -3.0,
    "trashy": -3.0,
    "breaks": -2.0,
    "breaks easily": -2.5,
    "poor quality": -2.8,
    "fragile": -2.2,
    "cheaply made": -2.7,
    "useless": -2.5,
    "disappointed": -2.6,
    "doesn't work": -2.8,
    "never buying again": -3.0,
    "garbage": -3.0,
    "flimsy": -2.5,
    "broke": -2.6,
    "defective": -2.8,
    "not worth it": -2.7,
    "waste of money": -3.0,
}

# 💬 Add them to VADER's lexicon
analyzer.lexicon.update(custom_words)

@app.route("/", methods=["GET", "POST"])
def index():
    sentiment = ""
    score = 0
    review = ""
    age_group = ""

    if request.method == "POST":
        review = request.form["review"]
        if review.strip():
            result = analyzer.polarity_scores(review)
            compound_score = result["compound"]

            if compound_score >= 0.05:
                sentiment = "Positive"
            elif compound_score <= -0.05:
                sentiment = "Negative"
            else:
                sentiment = "Neutral"

            # ✅ Predict age group from review
            age_group = predict_age_group(review)

            # ✅ Log behavior
            log_customer_behavior(review)

            # ✅ Save to database
            insert_review(review, sentiment, compound_score, age_group)

            return render_template(
                "index.html",
                sentiment=sentiment,
                score=round(compound_score, 2),
                review=review,
                age_group=age_group
            )

    # fallback in case of GET or empty form
    return render_template("index.html", sentiment=sentiment, score=score, review=review, age_group=age_group)

@app.route("/reviews")
def reviews():
    all_reviews = get_all_reviews()
    return render_template("reviews.html", reviews=all_reviews)

if __name__ == "__main__":
    app.run(debug=True)
