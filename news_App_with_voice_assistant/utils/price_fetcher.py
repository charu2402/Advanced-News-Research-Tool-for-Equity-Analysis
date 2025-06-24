import requests

def get_stock_price(stock_symbol):
    # Your Alpha Vantage API key
    api_key = "D6117Z7UPPDP37B4"  # Replace with your actual API key
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={stock_symbol}&interval=5min&apikey={api_key}"
    
    try:
        response = requests.get(url)
        
        if response.status_code != 200:
            return "Failed to fetch stock price. Please try again later."
        
        data = response.json()

        if "Time Series (5min)" not in data:
            return f"Error: No stock price data found for {stock_symbol}."
        
        # Get the latest price (most recent entry in the "Time Series" data)
        latest_data = list(data["Time Series (5min)"].values())[0]
        latest_price = latest_data["1. open"]

        return f"The current price of {stock_symbol} is ${latest_price}."
    
    except Exception as e:
        return f"Error fetching stock price: {str(e)}"
