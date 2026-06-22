from pymongo import MongoClient, ASCENDING, DESCENDING
from datetime import datetime

client = MongoClient("mongodb://localhost:27017/")
db = client["sentiment_db"]
collection = db["reviews"]

def insert_review(text, source, sentiment, score):
    doc = {
        "text": text,
        "source": source,
        "sentiment": sentiment,
        "score": round(score, 3),
        "timestamp": datetime.utcnow()
    }
    return collection.insert_one(doc)

def get_all_reviews(limit=50):
    return list(collection.find({}, {"_id": 0}).sort("timestamp", DESCENDING).limit(limit))

def get_sentiment_counts():
    pipeline = [
        {"$group": {"_id": "$sentiment", "count": {"$sum": 1}}}
    ]
    return list(collection.aggregate(pipeline))

def get_source_breakdown():
    pipeline = [
        {"$group": {"_id": {"source": "$source", "sentiment": "$sentiment"}, "count": {"$sum": 1}}},
        {"$sort": {"_id.source": ASCENDING}}
    ]
    return list(collection.aggregate(pipeline))

def get_score_over_time():
    pipeline = [
        {"$sort": {"timestamp": ASCENDING}},
        {"$project": {
            "_id": 0,
            "score": 1,
            "timestamp": {"$dateToString": {"format": "%Y-%m-%d %H:%M", "date": "$timestamp"}}
        }}
    ]
    return list(collection.aggregate(pipeline))

def get_stats():
    total = collection.count_documents({})
    avg = list(collection.aggregate([{"$group": {"_id": None, "avg": {"$avg": "$score"}}}]))
    avg_score = round(avg[0]["avg"], 3) if avg else 0
    positive = collection.count_documents({"sentiment": "Positive"})
    negative = collection.count_documents({"sentiment": "Negative"})
    neutral  = collection.count_documents({"sentiment": "Neutral"})
    return {"total": total, "avg_score": avg_score, "positive": positive, "negative": negative, "neutral": neutral}
