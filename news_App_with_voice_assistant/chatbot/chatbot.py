from utils.news_fetcher import get_stock_news
from utils.price_fetcher import get_stock_price
from utils.summarizer import simple_summarizer
from utils.sentiment_analyzer import analyze_sentiment
from utils.voice_assistant import speak

class FinanceChatbot:
    def __init__(self):
        pass  # No model needed for these functions

    def handle_query(self, query):
        query = query.lower()

        if "price" in query:
            stock = query.split()[-1]
            return get_stock_price(stock)

        elif "news" in query or "tell me about" in query:
            stock = query.split()[-1]
            news = get_stock_news(stock)
            summary = simple_summarizer(news)
            sentiment = analyze_sentiment(news)
            full_response = f"Summary: {summary}\n\nSentiment: {sentiment}"
            speak(full_response)
            return full_response

        else:
            return "I'm sorry, I can only fetch stock news and prices currently."

    def voice_mode(self):
        from utils.voice_assistant import listen
        query = listen()
        return self.handle_query(query)
