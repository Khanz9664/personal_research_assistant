from data_access.llm_summarizer import summarize_text
from markdown import markdown
import re

def generate_report(memory_data, summary_length="medium"):
    try:
        if not memory_data:
            return "# Research Report\n\nNo relevant information found."
            
        contents, sources = zip(*memory_data)
        combined_text = "\n\n".join(contents)
        
        summary = summarize_text(combined_text, summary_length)
        
        # Format references
        references = ["## References"]
        for idx, src in enumerate(sources):
            ref = f"{idx+1}. **{src['title']}**  \n"
            ref += f"- Author: {src['author'] or 'Unknown'}  \n"
            ref += f"- Date: {src['date'] or 'Unknown'}  \n"
            ref += f"- URL: [{src['url']}]({src['url']})"
            references.append(ref)
        
        full_report = f"# Research Report\n\n{summary}\n\n{'\n\n'.join(references)}"
        
        # Clean up markdown formatting
        full_report = re.sub(r'\n{3,}', '\n\n', full_report)
        return markdown(full_report)
    except Exception as e:
        return f"# Report Generation Error\n\n{str(e)}"
