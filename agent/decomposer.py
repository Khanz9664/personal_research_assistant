def decompose_task(prompt):
    """
    Breaks down a given prompt into a set of subtasks to guide research or analysis.

    Parameters:
        prompt (str): The main topic or question to be explored.

    Returns:
        list: A list of subtasks related to the prompt.
    """
    subtasks = [
        # Gather general background knowledge on the topic
        f"Search for background information about {prompt}",

        # Look into what problems or knowledge gaps exist in this area
        f"Identify key challenges and gaps in {prompt}",

        # Stay up-to-date by checking current trends and new developments
        f"Summarize latest trends and developments in {prompt}"
    ]

    return subtasks

