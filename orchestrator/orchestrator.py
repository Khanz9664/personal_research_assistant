from agent.decomposer import decompose_task
from agent.decision_maker import evaluate_sources
from agent.memory import Memory
from agent.planner import should_continue
from data_access.search_api import search_web
from data_access.web_scraper import scrape_page_content
from output.report_generator import generate_report

def run_agent(prompt):
    """
    Coordinates the end-to-end process of breaking down a prompt, 
    performing web searches, filtering credible information, 
    and generating a final report.

    Parameters:
        prompt (str): The main topic or question to process.

    Returns:
        str: A generated report based on aggregated and credible content.
    """
    # Initialize the memory to store gathered content
    memory = Memory()

    # Break the main prompt into smaller subtasks
    subtasks = decompose_task(prompt)
    
    for task in subtasks:
        print(f"[Agent] Processing subtask: {task}")

        # Perform a web search for the current subtask
        results = search_web(task)

        # Filter the results for credible sources
        credible = evaluate_sources(results)

        # Skip this subtask if no credible sources are found
        if not credible:
            print("[Agent] No credible sources found. Skipping.")
            continue

        # Scrape and store content from each credible source
        for source in credible:
            print(f"[Agent] Scraping {source['link']}")
            content = scrape_page_content(source["link"])
            memory.store(f"Source: {source['title']}\n{content}")
        
        # Check if enough information has been gathered to stop early
        if not should_continue(memory.recall_all()):
            print("[Agent] Enough data gathered. Stopping early.")
            break
    
    # Generate a final report based on all collected content
    report = generate_report(memory.recall_all())
    return report

