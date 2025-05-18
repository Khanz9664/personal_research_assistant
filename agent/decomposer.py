def decompose_task(prompt, domain, context=""):
    base_tasks = [
        f"Search for comprehensive background information about {prompt}",
        f"Identify current challenges and debates surrounding {prompt}",
        f"Find recent developments and future trends related to {prompt}"
    ]
    
    domain_specific = {
        "medical": [
            f"Find clinical trial data about {prompt}",
            f"Search for FDA approvals related to {prompt}"
        ],
        "legal": [
            f"Find relevant court cases about {prompt}",
            f"Search for legislative history of {prompt}"
        ]
    }
    
    return base_tasks + domain_specific.get(domain, []) + (
        [f"Investigate {context}"] if context else []
    )
