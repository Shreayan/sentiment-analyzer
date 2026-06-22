from flask import Flask, render_template, request, jsonify
from db import insert_review, get_all_reviews, get_sentiment_counts, get_source_breakdown, get_score_over_time, get_stats
from analyzer import analyze

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/stats")
def api_stats():
    return jsonify(get_stats())

@app.route("/api/reviews")
def api_reviews():
    return jsonify(get_all_reviews())

@app.route("/api/sentiment-counts")
def api_sentiment_counts():
    data = get_sentiment_counts()
    return jsonify(data)

@app.route("/api/source-breakdown")
def api_source_breakdown():
    return jsonify(get_source_breakdown())

@app.route("/api/score-over-time")
def api_score_over_time():
    return jsonify(get_score_over_time())

@app.route("/api/analyze", methods=["POST"])
def api_analyze():
    body = request.get_json()
    text   = body.get("text", "").strip()
    source = body.get("source", "Manual")
    if not text:
        return jsonify({"error": "No text provided"}), 400
    sentiment, score = analyze(text)
    insert_review(text, source, sentiment, score)
    return jsonify({"sentiment": sentiment, "score": round(score, 3)})

if __name__ == "__main__":
    app.run(debug=True)


