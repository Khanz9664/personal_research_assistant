import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve the SerpAPI key from environment variables
SERPAPI_KEY = os.getenv("SERPAPI_KEY")

def search_web(query):
    """
    Performs a web search using SerpAPI and returns a list of search result titles and links.

    Parameters:
        query (str): The search query string.

    Returns:
        list: A list of dictionaries, each containing the 'title' and 'link' of a search result.
    """
    url = "https://serpapi.com/search.json"
    params = {
        "q": query,             # The query string to search
        "api_key": SERPAPI_KEY, # API key for authentication
        "num": 5                # Limit the number of search results
    }

    # Send a GET request to SerpAPI
    response = requests.get(url, params=params)

    # Extract the organic (non-sponsored) search results
    results = response.json().get("organic_results", [])

    # Format and return only the title and link from each result
    return [{"title": r.get("title"), "link": r.get("link")} for r in results]
    
