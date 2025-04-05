from flask import Flask, render_template, request
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = Flask(__name__)
analyzer = SentimentIntensityAnalyzer()

@app.route("/", methods=["GET", "POST"])
def index():
    sentiment = None
    score = None
    review = ""

    if request.method == "POST":
        review = request.form["review"]
        result = analyzer.polarity_scores(review)
        compound_score = result["compound"]

        # Determine sentiment label
        if compound_score >= 0.2:
            sentiment = "Positive"
        elif compound_score <= -0.2:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"

        score = round(compound_score, 2)

    return render_template("index.html", sentiment=sentiment, score=score, review=review)

if __name__ == "__main__":
    app.run(debug=True)
