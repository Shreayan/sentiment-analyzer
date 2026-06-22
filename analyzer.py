from textblob import TextBlob

def analyze(text):
    blob = TextBlob(text)
    score = blob.sentiment.polarity  # -1.0 to 1.0

    if score > 0.1:
        sentiment = "Positive"
    elif score < -0.1:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return sentiment, score
