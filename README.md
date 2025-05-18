# Personal Research Assistant

## Currently working on it

An AI-powered tool designed to assist researchers by automating data retrieval, analysis, and summarization, streamlining the research process.

---

## 🚀 Overview

The **Personal Research Assistant** is a Python-based application that integrates various modules to facilitate efficient research workflows. It automates tasks such as data access, orchestration, and output generation, providing a seamless experience for researchers.

---

## 🛠️ Features

- **Agent Module**: Handles task execution and logic processing.
- **Data Access**: Facilitates retrieval of relevant research data.
- **Orchestrator**: Coordinates the workflow between different modules.
- **Output Generation**: Produces summaries, reports, and other outputs.
- **User Interface**: Provides an interactive interface for user interactions.

---

## 📁 Project Structure

The repository is organized into the following directories:

```
personal_research_assistant/
│
├── ui/
│   └── app.py
├── orchestrator/
│   ├── __init__.py
│   └── orchestrator.py
├── agent/
│   ├── __init__.py
│   ├── decomposer.py
│   ├── decision_maker.py
│   ├── planner.py
│   └── memory.py
├── data_access/
│   ├── __init__.py
│   ├── search_api.py
│   ├── web_scraper.py
│   └── llm_summarizer.py
├── output/
│   ├── __init__.py
│   └── report_generator.py
├── .env
└── requirements.txt
```


- **agent/**: Contains the core logic and task execution scripts.
- **data_access/**: Includes modules for fetching and processing research data.
- **orchestrator/**: Manages the workflow and coordination between modules.
- **output/**: Generates summaries, reports, and other outputs.
- **ui/**: Provides the user interface components.

---

## ⚙️ Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Khanz9664/personal_research_assistant.git
   cd personal_research_assistant
   ```
2. **Set up a virtual environment:**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install dependencies:**:

   ```bash
   pip install -r requirements.txt
   ```

## 🧪 Usage
  **To start the Personal Research Assistant, run the following command:**
  ```
  python ui/app.py
  ```
  - Follow the on-screen prompts to interact with the assistant.

📬 Contact




