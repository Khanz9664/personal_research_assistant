from agent.decomposer import decompose_task
from agent.decision_maker import evaluate_sources
from agent.memory import Memory
from agent.planner import should_continue
from data_access.search_api import search_web
from data_access.web_scraper import scrape_page_content
from output.report_generator import generate_report

def run_agent(prompt, domain="general", urgency="low", context=""):
    memory = Memory()
    subtasks = decompose_task(prompt, domain, context)
    
    for task in subtasks:
        results = search_web(task, domain)
        credible_sources = evaluate_sources(results, domain)
        
        for source in credible_sources[:3]:
            scraped = scrape_page_content(source["link"])
            if scraped["content"]:
                memory.store(scraped["content"], scraped["metadata"])
                
        if not should_continue(memory.recall_all(), urgency):
            break
    
    return generate_report(memory.recall_all())
