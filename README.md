# Sentiment Analyzer

A simple web application built with Flask that analyzes the sentiment of text using TextBlob and stores the results in a MongoDB database.

## Features
- **Sentiment Analysis**: Analyzes text and classifies it as Positive, Negative, or Neutral.
- **Database Storage**: Stores reviews and their sentiment scores in MongoDB.
- **API Endpoints**: Provides various API endpoints to fetch statistics, all reviews, sentiment counts, source breakdowns, and score trends over time.

## Project Structure
- `app.py`: The main Flask application providing API endpoints and rendering the frontend.
- `analyzer.py`: Contains the logic for sentiment analysis using TextBlob.
- `db.py`: Handles MongoDB connections and queries.
- `seed.py`: A script to populate the database with sample reviews.
- `templates/`: Contains HTML templates.

## Prerequisites
- Python 3
- MongoDB (running locally on port 27017)

## Installation and Setup

1. Install the required Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Make sure MongoDB is running locally on the default port (`27017`).

3. (Optional) Run the seed script to populate the database with some sample data:
   ```bash
   python seed.py
   ```

4. Start the Flask web server:
   ```bash
   python app.py
   ```

5. Open your web browser and navigate to `http://localhost:5000/`.
