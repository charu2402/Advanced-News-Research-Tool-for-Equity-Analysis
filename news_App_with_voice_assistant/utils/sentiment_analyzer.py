from textblob import TextBlob

def analyze_sentiment(news_list):
    text = " ".join(news_list)
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0.2:
        return "Buy ✅ (Positive Sentiment)"
    elif polarity < -0.2:
        return "Sell ❌ (Negative Sentiment)"
    else:
        return "Hold ⏸️ (Neutral Sentiment)"
