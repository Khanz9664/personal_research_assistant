import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import dateutil.parser as parser

def scrape_page_content(url):
    try:
        response = requests.get(url, timeout=15, headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract metadata
        metadata = {
            "title": soup.title.string.strip() if soup.title else urlparse(url).netloc,
            "author": "",
            "date": "",
            "url": url
        }

        # Author extraction
        author_selectors = [
            'meta[name="author"]',
            '[rel="author"]',
            '.author-name',
            '[itemprop="author"]'
        ]
        for selector in author_selectors:
            if soup.select(selector):
                metadata["author"] = soup.select(selector)[0].get_text().strip()
                break

        # Date extraction
        date_selectors = [
            'meta[property="article:published_time"]',
            'time[datetime]',
            '.date-published',
            '[itemprop="datePublished"]'
        ]
        for selector in date_selectors:
            if soup.select(selector):
                date_str = soup.select(selector)[0].get('content') or soup.select(selector)[0].get_text()
                try:
                    metadata["date"] = parser.parse(date_str).strftime("%Y-%m-%d")
                except:
                    metadata["date"] = date_str.strip()
                break

        # Content extraction
        paragraphs = []
        content_selectors = [
            'article', 
            'div.article-body',
            'div.main-content',
            'div.content'
        ]
        
        for selector in content_selectors:
            elements = soup.select(selector)
            if elements:
                paragraphs = [p.get_text().strip() for p in elements[0].find_all(['p', 'li', 'h2', 'h3'])]
                break

        return {
            "content": ' '.join(paragraphs)[:4000],  # Increased content limit
            "metadata": metadata
        }
    except Exception as e:
        print(f"Scraping error: {e}")
        return {"content": "", "metadata": {}}
