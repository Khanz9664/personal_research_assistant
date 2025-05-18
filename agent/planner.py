def should_continue(memory_data, urgency):
    content_count = len(memory_data)
    if urgency == "high":
        return content_count < 2
    elif urgency == "medium":
        return content_count < 4
    return content_count < 5
