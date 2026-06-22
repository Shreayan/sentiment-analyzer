from db import insert_review, collection
from analyzer import analyze

sample_reviews = [
    ("This product is absolutely amazing! Best purchase I've made.", "Amazon"),
    ("Terrible quality. Broke after two days. Total waste of money.", "Amazon"),
    ("It's okay. Nothing special but does the job.", "Amazon"),
    ("Fantastic customer support! They resolved my issue instantly.", "Twitter"),
    ("I hate this service. They never respond to complaints.", "Twitter"),
    ("Pretty decent experience overall. Would consider buying again.", "Twitter"),
    ("Blown away by the quality! Exceeded all my expectations.", "Reddit"),
    ("Absolute garbage. Do not buy this under any circumstances.", "Reddit"),
    ("Meh. Average product for the price.", "Reddit"),
    ("Love it! Using it every single day now.", "Amazon"),
    ("Disappointed. The description was very misleading.", "Amazon"),
    ("Works fine. No complaints but nothing impressive either.", "Twitter"),
    ("Incredible value for money. Highly recommend!", "Reddit"),
    ("Worst experience of my life. Never again.", "Amazon"),
    ("Neutral feeling about this. Has pros and cons.", "Twitter"),
    ("Super fast delivery and great packaging!", "Amazon"),
    ("Product stopped working after a week. Very frustrated.", "Reddit"),
    ("Solid build quality. Happy with my purchase.", "Twitter"),
    ("Not bad, not great. Just average.", "Reddit"),
    ("Outstanding! Will definitely be buying more from this brand.", "Amazon"),
]

def seed():
    collection.drop()
    print("Dropped existing collection.")
    for text, source in sample_reviews:
        sentiment, score = analyze(text)
        insert_review(text, source, sentiment, score)
        print(f"[{sentiment:8s}] ({score:+.2f}) [{source}] {text[:50]}")
    print(f"\n✅ Seeded {len(sample_reviews)} reviews into MongoDB.")

if __name__ == "__main__":
    seed()
