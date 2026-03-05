from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return f"""
    <html>
        <head>
            <title>Azure DevOps CI/CD Demo</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background-color: #f4f6f8;
                    text-align: center;
                    padding: 40px;
                }}
                .card {{
                    background: white;
                    padding: 30px;
                    border-radius: 10px;
                    box-shadow: 0px 2px 10px rgba(0,0,0,0.1);
                    max-width: 600px;
                    margin: auto;
                }}
                h1 {{
                    color: #0078D4;
                }}
                .status {{
                    color: green;
                    font-weight: bold;
                }}
            </style>
        </head>

        <body>
            <div class="card">
                <h1>Azure DevOps CI/CD Pipeline</h1>
                <p class="status">Application Running Successfully</p>

                <h3>Project Information</h3>
                <p>This application is deployed using an automated CI/CD pipeline.</p>

                <ul style="text-align:left;">
                    <li>Docker Containerization</li>
                    <li>GitHub Actions CI/CD</li>
                    <li>Azure Container Registry</li>
                    <li>Azure Container Apps Deployment</li>
                </ul>

                <p><b>Current Server Time:</b> {datetime.now()}</p>

                <p><b>Developer:</b> Sumanth U</p>
            </div>
        </body>
    </html>
    """

@app.route("/health")
def health():
    return {
        "status": "healthy",
        "service": "Azure DevOps CI/CD Demo",
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)