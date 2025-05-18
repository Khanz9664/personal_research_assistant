def evaluate_sources(sources, domain):
    credibility_rules = {
        "general": {
            "domains": [".edu", ".gov", "wikipedia.org", "nature.com"],
            "keywords": ["study", "research", "report", "analysis"]
        },
        "medical": {
            "domains": ["nih.gov", "who.int", "pubmed.ncbi.nlm.nih.gov"],
            "keywords": ["clinical trial", "peer-reviewed", "meta-analysis"]
        },
        "legal": {
            "domains": ["courtlistener.com", "supremecourt.gov", ".gov"],
            "keywords": ["opinion", "ruling", "statute"]
        }
    }
    
    rules = credibility_rules.get(domain, credibility_rules["general"])
    credible = []
    
    for source in sources:
        url = source["link"].lower()
        title = source["title"].lower()
        
        domain_match = any(d in url for d in rules["domains"])
        keyword_match = any(k in title for k in rules["keywords"])
        
        if domain_match or keyword_match:
            credible.append(source)
    
    return credible[:5]  # Return top 5 credible sources
