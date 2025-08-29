import requests
import json
import os

# Your API Key from NewsAPI.org
# IMPORTANT: Replace "YOUR_API_KEY" with your actual key.
# Never commit your API key directly to a public repository.
API_KEY = "52cb0a01606c4e31b83a7d15bb9129f9"

# The endpoint for getting all news articles
# You can change the search query ('q'), language, etc.
# For more options, check the NewsAPI documentation.
URL = "https://newsapi.org/v2/everything"

# Parameters for the API request
# 'q' is the query term, 'language' is the language of the articles
# 'pageSize' limits the number of articles per request (max 100 on the free plan)
# 'sortBy' can be 'relevancy', 'popularity', or 'publishedAt'
params = {
    'q': 'technology OR science OR business',  # A sample query for news related to these topics
    'language': 'en',
    'sortBy': 'publishedAt',
    'pageSize': 100,
    'apiKey': API_KEY
}

# The name of the output file
OUTPUT_FILE = "news_data.json"

def fetch_news_data():
    """
    Fetches news articles from the NewsAPI and saves them to a JSON file.
    """
    if API_KEY == "52cb0a01606c4e31b83a7d15bb9129f9":
        print("Error: API_KEY is not set. Please replace 'YOUR_API_KEY' with your actual key.")
        return

    print("Fetching news articles...")
    try:
        # Make the GET request to the NewsAPI
        response = requests.get(URL, params=params)
        
        # Raise an exception for bad status codes (4xx or 5xx)
        response.raise_for_status()

        # Parse the JSON response
        data = response.json()

        # Check for a successful response from the API itself
        if data['status'] == 'ok':
            articles = data['articles']
            print(f"Successfully fetched {len(articles)} articles.")

            # Save the articles to a JSON file
            with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
                json.dump(articles, f, ensure_ascii=False, indent=4)
            
            print(f"Articles saved to {OUTPUT_FILE}")
            
        else:
            print(f"API returned an error: {data.get('message', 'Unknown error')}")

    except requests.exceptions.RequestException as e:
        # Handle network or HTTP errors
        print(f"An error occurred while making the request: {e}")
    except json.JSONDecodeError:
        # Handle cases where the response is not valid JSON
        print("Failed to decode JSON from the response.")
    except Exception as e:
        # Catch any other potential errors
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    fetch_news_data()
