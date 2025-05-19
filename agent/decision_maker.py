def evaluate_sources(sources, domain):
    credibility_rules = {
        "general": {
            "domains": [".edu", ".gov", "wikipedia.org", "nature.com"],
            "keywords": ["study", "research", "report", "analysis"]
        },
        "machine_learning": {
            "domains": ["arxiv.org", "paperswithcode.com", "nips.cc", "openreview.net"],
            "keywords": ["neural network", "transformer", "gradient descent", "benchmark", "loss function"]
        },
       "computer_science": {
            "domains": ["acm.org", "ieee.org", "usenix.org", "cs.stanford.edu"],
            "keywords": ["algorithm", "data structure", "computational complexity", "distributed systems", "programming language"]
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
