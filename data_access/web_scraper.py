import requests
from bs4 import BeautifulSoup

def scrape_page_content(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        paragraphs = soup.find_all("p")
        text = " ".join([p.get_text() for p in paragraphs])
        return text[:3000]  # Limit to 1000 chars
    except:
        return ""

