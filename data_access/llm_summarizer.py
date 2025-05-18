def summarize_text(text, summary_length="medium"):
    try:
        # Improved extractive step
        sentences = [s.strip() for s in re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text) if len(s) > 50]
        top_sentences = sorted(sentences, key=lambda x: len(x), reverse=True)[:15]
        extractive_text = ' '.join(top_sentences)[:3000]

        # Abstractive step
        headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}
        payload = {
            "inputs": extractive_text,
            "parameters": {
                "max_length": 300 if summary_length == "short" else 600,
                "min_length": 150 if summary_length == "short" else 300,
                "do_sample": True
            }
        }
        
        response = requests.post(
            "https://api-inference.huggingface.co/models/facebook/bart-large-cnn",
            headers=headers,
            json=payload,
            timeout=30
        )
        
        if response.status_code == 200:
            return response.json()[0]["summary_text"]
        else:
            return extractive_text[:2000] + "... [full text available in references]"
            
    except Exception as e:
        print(f"Summarization error: {e}")
        return text[:2000] + "... [full content available in references]"
