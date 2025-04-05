from flask import Flask, render_template, request
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = Flask(__name__)
analyzer = SentimentIntensityAnalyzer()
# Boost weight of custom negative words
custom_words = {
    "trash": -4.0,
    "breaks": -2.5,
    "broken": -3.0,
    "easily": -1.0,
    "useless": -3.5,
    "worst": -4.0
}

analyzer.lexicon.update(custom_words)


@app.route("/", methods=["GET", "POST"])
def index():
    sentiment = ""
    score_display = None
    review = ""

    if request.method == "POST":
        review = request.form["review"]
        score = analyzer.polarity_scores(review)

        # Decide sentiment based on neg/pos values instead of compound
        if score["neg"] > score["pos"]:
            sentiment = "Negative"
        elif score["pos"] > score["neg"]:
            sentiment = "Positive"
        else:
            sentiment = "Neutral"

        # Show the difference between pos and neg as a makeshift score
        score_display = round(score["pos"] - score["neg"], 2)

    return render_template("index.html", sentiment=sentiment, score=score_display, review=review)

if __name__ == "__main__":
    app.run(debug=True)
