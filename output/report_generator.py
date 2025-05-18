from data_access.llm_summarizer import summarize_text

def generate_report(memory_data):
    combined_text = "\n\n".join(memory_data)
    summary = summarize_text(combined_text)
    return f"### Research Report\n\n{summary}\n\n---\n\nFull Notes:\n{combined_text}"

