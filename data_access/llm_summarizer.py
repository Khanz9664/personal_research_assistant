import requests
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Get the Hugging Face API key from the environment
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")

def summarize_text(text):
    """
    Summarizes the input text using the Hugging Face BART model hosted via their API.

    Parameters:
        text (str): The text to be summarized. Only the first 2000 characters are used 
                    due to API input limits.

    Returns:
        str: The summarized text if the API call is successful; otherwise, an error message.
    """
    api_url = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
    headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}

    # Limit input text length to comply with Hugging Face's API restrictions
    payload = {"inputs": text[:2000]}

    # Send the POST request to the Hugging Face inference API
    response = requests.post(api_url, headers=headers, json=payload)

    # If the request was successful, return the summary
    if response.status_code == 200:
        result = response.json()
        return result[0]["summary_text"]
    else:
        # If the request failed, return a fallback message
        return "[LLM summarization failed]"

