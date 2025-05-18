import requests
from bs4 import BeautifulSoup

def scrape_page_content(url):
    """
    Scrapes the visible text content (from <p> tags) of a web page.

    Parameters:
        url (str): The URL of the web page to scrape.

    Returns:
        str: A string containing the concatenated text from paragraph tags,
             limited to the first 3000 characters. Returns an empty string if scraping fails.
    """
    try:
        # Send a GET request to the URL
        response = requests.get(url)

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract all paragraph elements
        paragraphs = soup.find_all("p")

        # Combine the text from all paragraphs into one string
        text = " ".join([p.get_text() for p in paragraphs])

        # Return the first 3000 characters of the content
        return text[:3000]
    
    except:
        # Return an empty string if any error occurs during scraping
        return ""

