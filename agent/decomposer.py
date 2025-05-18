def decompose_task(prompt):
    subtasks = [
        f"Search for background information about {prompt}",
        f"Identify key challenges and gaps in {prompt}",
        f"Summarize latest trends and developments in {prompt}"
    ]
    return subtasks

