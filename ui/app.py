import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from flask import Flask, request, render_template_string
from orchestrator.orchestrator import run_agent

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    report = ""
    if request.method == 'POST':
        prompt = request.form['prompt']
        report = run_agent(prompt)
    return render_template_string('''
        <h2>Personal Research Assistant</h2>
        <form method="post">
            <input name="prompt" placeholder="Enter your research topic" size="50">
            <input type="submit" value="Research">
        </form>
        <pre>{{report}}</pre>
    ''', report=report)

if __name__ == '__main__':
    app.run(debug=True)

