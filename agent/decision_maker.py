def evaluate_sources(sources):
    credible = []
    for source in sources:
        if "wikipedia" in source["link"] or "research" in source["title"].lower():
            credible.append(source)
    return credible

