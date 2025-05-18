def evaluate_sources(sources):
    """
    Filters a list of source dictionaries to identify credible ones based on 
    domain names and keywords in the title.

    Parameters:
        sources (list): A list of dictionaries, each representing a source 
                        with at least 'link' and 'title' keys.

    Returns:
        list: A list of sources deemed credible.
    """
    credible = []

    for source in sources:
        # Extract and normalize the link and title for easier comparison
        url = source.get("link", "").lower()
        title = source.get("title", "").lower()

        # List of domains and TLDs that are generally considered reliable
        credible_domains = [
            "wikipedia.org", "nature.com", "sciencedirect.com",
            "jstor.org", "nasa.gov", "nih.gov", ".edu", ".gov"
        ]

        # Keywords that typically indicate scholarly or serious content
        credible_keywords = [
            "research", "study", "report", "analysis", "journal", "whitepaper"
        ]

        # If the source URL contains a trusted domain, consider it credible
        if any(domain in url for domain in credible_domains):
            credible.append(source)

        # Alternatively, if the title includes keywords suggesting credibility
        elif any(keyword in title for keyword in credible_keywords):
            credible.append(source)

    return credible

