def evaluate_sources(sources):
    credible = []
    for source in sources:
        url = source.get("link", "").lower()
        title = source.get("title", "").lower()

        # List of known credible domains or TLDs
        credible_domains = ["wikipedia.org", "nature.com", "sciencedirect.com", "jstor.org", "nasa.gov", "nih.gov", ".edu", ".gov"]

        # Keywords in title that indicate credible content
        credible_keywords = ["research", "study", "report", "analysis", "journal", "whitepaper"]

        # Check for credible domain
        if any(domain in url for domain in credible_domains):
            credible.append(source)
        # Or if the title includes any strong keywords
        elif any(keyword in title for keyword in credible_keywords):
            credible.append(source)

    return credible

