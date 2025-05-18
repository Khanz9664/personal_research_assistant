from flask import Flask, request, render_template_string
import sys
import os

# Add the parent directory to the system path to import orchestrator
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Import the agent orchestration function
from orchestrator.orchestrator import run_agent

# Initialize Flask application
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Renders the main page with a form to input a research prompt.
    If the form is submitted, it calls `run_agent` to process the prompt
    and generate a report.
    
    Returns:
        HTML: A page with the form and the resulting research report.
    """
    report = ""  # Initialize an empty report
    
    # If the form is submitted, process the input prompt
    if request.method == 'POST':
        prompt = request.form['prompt']
        report = run_agent(prompt)  # Generate a report using the agent

    # Render the HTML page with Bootstrap styling and the generated report
    return render_template_string('''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Personal Research Assistant</title>
            <!-- Include Bootstrap and Google Fonts -->
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
            <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap" rel="stylesheet">
            <style>
                body {
                    font-family: 'Inter', sans-serif;
                    background: linear-gradient(135deg, #1e1e2f, #2c3e50);
                    color: #f5f5f5;
                    min-height: 100vh;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    padding: 40px 20px;
                }

                .container {
                    background: rgba(255, 255, 255, 0.05);
                    backdrop-filter: blur(12px);
                    -webkit-backdrop-filter: blur(12px);
                    padding: 40px;
                    border-radius: 16px;
                    box-shadow: 0 20px 50px rgba(0,0,0,0.3);
                    width: 100%;
                    max-width: 800px;
                }

                h2 {
                    font-weight: 600;
                    text-align: center;
                    margin-bottom: 30px;
                }

                .input-group input {
                    background-color: #1e1e2f;
                    color: #f5f5f5;
                    border: 1px solid #444;
                }

                .input-group input::placeholder {
                    color: #bbb;
                }

                .btn-primary {
                    background-color: #4e9af1;
                    border-color: #4e9af1;
                    transition: all 0.3s ease;
                }

                .btn-primary:hover {
                    background-color: #2e7de1;
                    border-color: #2e7de1;
                }

                .result-box {
                    white-space: pre-wrap;
                    background: rgba(255, 255, 255, 0.1);
                    padding: 20px;
                    border-radius: 10px;
                    margin-top: 25px;
                    border: 1px solid rgba(255,255,255,0.1);
                    max-height: 500px;
                    overflow-y: auto;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h2>🔍 Personal Research Assistant</h2>
                <!-- Research form -->
                <form method="post">
                    <div class="input-group mb-3">
                        <input type="text" name="prompt" class="form-control" placeholder="Enter your research topic..." required>
                        <button class="btn btn-primary" type="submit">Research</button>
                    </div>
                </form>

                <!-- Display the report if available -->
                {% if report %}
                <div class="result-box">
                    {{ report }}
                </div>
                {% endif %}
            </div>
        </body>
        </html>
    ''', report=report)

# Run the Flask app in debug mode
if __name__ == '__main__':
    app.run(debug=True)

