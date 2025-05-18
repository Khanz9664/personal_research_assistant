from data_access.llm_summarizer import summarize_text

def generate_report(memory_data):
    """
    Generates a research report by summarizing collected memory data.

    Parameters:
        memory_data (list): A list of strings, each representing a piece of stored information.

    Returns:
        str: A formatted report including a summary and the full collected notes.
    """
    # Combine all stored memory content into one large text block
    combined_text = "\n\n".join(memory_data)

    # Use an LLM to generate a summary of the combined content
    summary = summarize_text(combined_text)

    # Format the final report with a header, summary, and full notes
    return f"### Research Report\n\n{summary}\n\n---\n\nFull Notes:\n{combined_text}"

