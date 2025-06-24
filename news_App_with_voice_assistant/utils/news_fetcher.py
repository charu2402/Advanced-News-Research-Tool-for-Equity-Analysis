import requests

def get_stock_news(stock_name):
    # Your NewsAPI key
    api_key = "ede5374651fc4bd687e9d3b36449eaea"
    url = f"https://newsapi.org/v2/everything?q={stock_name}&apiKey={api_key}"
    
    try:
        response = requests.get(url)
        
        if response.status_code != 200:
            return ["Failed to fetch news. Please try again later."]
        
        data = response.json()
        
        if data["totalResults"] == 0:
            return [f"No news found for {stock_name}."]

        news = []
        # Get the first 3 news articles
        for article in data["articles"][:3]:
            title = article["title"]
            description = article["description"]
            news.append(f"{title}: {description}")
        
        return news
    
    except Exception as e:
        return [f"Error fetching news: {str(e)}"]
