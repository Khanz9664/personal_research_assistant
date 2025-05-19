from flask import Flask, request, render_template_string, make_response
import sys
import os
import pdfkit
from markdown import markdown

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from orchestrator.orchestrator import run_agent

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    report = ""
    if request.method == 'POST':
        params = {
            'prompt': request.form['prompt'],
            'domain': request.form.get('domain', 'general'),
            'urgency': request.form.get('urgency', 'low'),
            'context': request.form.get('context', '')
        }
        report = run_agent(**params)

    return render_template_string('''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Personal Research Assistant</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
            <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap" rel="stylesheet">
            <style>
                body { font-family: 'Inter', sans-serif; background: linear-gradient(135deg, #1e1e2f, #2c3e50); color: #f5f5f5; min-height: 100vh; padding: 40px 20px; }
                .container { background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(12px); padding: 40px; border-radius: 16px; box-shadow: 0 20px 50px rgba(0,0,0,0.3); max-width: 800px; }
                .input-group > * { margin: 5px; }
                .result-box { white-space: pre-wrap; background: rgba(255, 255, 255, 0.1); padding: 20px; border-radius: 10px; margin-top: 25px; }
            </style>
        </head>
        <body>
            <div class="container">
                <h2 class="text-center mb-4">🔍 Personal Research Assistant</h2>
                <form method="post">
                    <div class="input-group mb-3">
                        <input type="text" name="prompt" class="form-control" placeholder="Research topic/question..." required>
                        <select name="domain" class="form-select">
                            <option value="general">General</option>
                            <option value="machine learning">ML</option>
                            <option value="computer science">Computer Science</option>
                        </select>
                        <select name="urgency" class="form-select">
                            <option value="low">Low</option>
                            <option value="medium">Medium</option>
                            <option value="high">High</option>
                        </select>
                    </div>
                    <div class="mb-3">
                        <textarea name="context" class="form-control" rows="2" placeholder="Additional context..."></textarea>
                    </div>
                    <button class="btn btn-primary w-100" type="submit">Research</button>
                </form>

                {% if report %}
                <div class="result-box mt-4">
                    {{ report|safe }}
                    <div class="export-buttons mt-3">
                        <a href="/export/pdf?report={{ report }}" class="btn btn-sm btn-outline-light">PDF</a>
                        <a href="/export/md?report={{ report }}" class="btn btn-sm btn-outline-light">Markdown</a>
                    </div>
                </div>
                {% endif %}
            </div>
        </body>
        </html>
    ''', report=report)

@app.route('/export/pdf')
def export_pdf():
    report = request.args.get('report')
    pdf = pdfkit.from_string(report, False)
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachment; filename=research_report.pdf'
    return response

@app.route('/export/md')
def export_md():
    report = request.args.get('report')
    response = make_response(markdown(report))
    response.headers['Content-Type'] = 'text/markdown'
    response.headers['Content-Disposition'] = 'attachment; filename=research_report.md'
    return response

if __name__ == '__main__':
    app.run(debug=True)
