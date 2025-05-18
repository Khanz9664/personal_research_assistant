import requests
import os
from dotenv import load_dotenv
load_dotenv()


SERPAPI_KEY = os.getenv("SERPAPI_KEY")

def search_web(query):
    url = "https://serpapi.com/search.json"
    params = {
        "q": query,
        "api_key": SERPAPI_KEY,
        "num": 5
    }
    response = requests.get(url, params=params)
    results = response.json().get("organic_results", [])
    return [{"title": r.get("title"), "link": r.get("link")} for r in results]

