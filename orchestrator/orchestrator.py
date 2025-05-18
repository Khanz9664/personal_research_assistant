from agent.decomposer import decompose_task
from agent.decision_maker import evaluate_sources
from agent.memory import Memory
from agent.planner import should_continue
from data_access.search_api import search_web
from data_access.web_scraper import scrape_page_content
from output.report_generator import generate_report

def run_agent(prompt):
    memory = Memory()
    subtasks = decompose_task(prompt)
    
    for task in subtasks:
        print(f"[Agent] Processing subtask: {task}")
        results = search_web(task)
        credible = evaluate_sources(results)
        if not credible:
            print("[Agent] No credible sources found. Skipping.")
            continue
        for source in credible:
            print(f"[Agent] Scraping {source['link']}")
            content = scrape_page_content(source["link"])
            memory.store(f"Source: {source['title']}\n{content}")
        
        # Decision point (could loop or stop)
        if not should_continue(memory.recall_all()):
            print("[Agent] Enough data gathered. Stopping early.")
            break
    
    report = generate_report(memory.recall_all())
    return report

