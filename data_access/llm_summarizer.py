import requests
import os
from dotenv import load_dotenv
load_dotenv()


HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")

def summarize_text(text):
    api_url = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
    headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}
    payload = {"inputs": text[:2000]}  # HF API limits input size
    response = requests.post(api_url, headers=headers, json=payload)
    if response.status_code == 200:
        result = response.json()
        return result[0]["summary_text"]
    else:
        return "[LLM summarization failed]"

