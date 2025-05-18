import requests
import os
from dotenv import load_dotenv

load_dotenv()

SERPAPI_KEY = os.getenv("SERPAPI_KEY")
PUBMED_API_KEY = os.getenv("PUBMED_API_KEY")

def search_web(query, domain="general"):
    if domain == "medical":
        return pubmed_search(query)
    elif domain == "legal":
        return courtlistener_search(query)
    else:
        return serpapi_search(query)

def serpapi_search(query):
    params = {
        "q": query,
        "api_key": SERPAPI_KEY,
        "num": 7,
        "hl": "en"
    }
    response = requests.get("https://serpapi.com/search.json", params=params)
    return [{"title": r.get("title"), "link": r.get("link")} for r in response.json().get("organic_results", [])]

def pubmed_search(query):
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": 5,
        "api_key": PUBMED_API_KEY
    }
    response = requests.get("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi", params=params)
    ids = response.json().get("esearchresult", {}).get("idlist", [])
    return [{"title": f"PubMed Article {pmid}", "link": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}"} for pmid in ids]

def courtlistener_search(query):
    params = {
        "q": query,
        "type": "opinion",
        "order_by": "score desc",
        "format": "json"
    }
    response = requests.get("https://www.courtlistener.com/api/rest/v3/search/", params=params)
    return [{
        "title": item.get("caseName", ""),
        "link": f"https://www.courtlistener.com{item.get('absolute_url', '')}"
    } for item in response.json().get("results", [])[:5]]
