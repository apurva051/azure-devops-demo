
from flask import Flask, render_template_string, jsonify
from datetime import datetime, timezone

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Azure DevOps Demo</title>

    <style>
        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: #f3f6fb;
            color: #1f2937;
        }

        header {
            background: #123b70;
            color: white;
            padding: 20px 8%;
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 12px;
        }

        header h2 {
            margin: 0;
        }

        nav a {
            color: white;
            text-decoration: none;
            margin-left: 20px;
            font-size: 14px;
        }

        main {
            max-width: 1100px;
            margin: 40px auto;
            padding: 0 20px;
        }

        .welcome {
            margin-bottom: 30px;
        }

        .welcome h1 {
            font-size: 32px;
            margin-bottom: 10px;
        }

        .welcome p {
            color: #64748b;
            line-height: 1.6;
        }

        .cards {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 20px;
            margin-bottom: 28px;
        }

        .card {
            background: white;
            padding: 24px;
            border-radius: 12px;
            box-shadow: 0 3px 12px rgba(0, 0, 0, 0.05);
        }

        .card h3 {
            margin-top: 0;
            font-size: 16px;
            color: #64748b;
        }

        .status {
            font-size: 22px;
            font-weight: bold;
        }

        .healthy {
            color: #15803d;
        }

        .development {
            color: #2563eb;
        }

        .pending {
            color: #a16207;
        }

        .section-title {
            margin-bottom: 22px;
        }

        .pipeline {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(130px, 1fr));
            gap: 12px;
        }

        .pipeline-step {
            text-align: center;
            padding: 18px 10px;
            border: 1px solid #dbe3ef;
            border-radius: 10px;
            background: #f8fafc;
        }

        .pipeline-step strong {
            display: block;
            margin-bottom: 8px;
        }

        .pipeline-step span {
            font-size: 13px;
            color: #64748b;
        }

        .about {
            margin-top: 24px;
            line-height: 1.7;
        }

        button {
            background: #2563eb;
            color: white;
            border: none;
            padding: 12px 20px;
            border-radius: 7px;
            cursor: pointer;
            font-size: 14px;
        }

        button:hover {
            background: #1d4ed8;
        }

        #health-result {
            margin-top: 12px;
            font-weight: bold;
        }

        footer {
            text-align: center;
            padding: 25px;
            color: #64748b;
            font-size: 13px;
        }

        @media (max-width: 600px) {
            header {
                padding: 20px;
            }

            nav a {
                margin-left: 0;
                margin-right: 14px;
            }

            .welcome h1 {
                font-size: 26px;
            }
        }
    </style>
</head>

<body>
    <header>
        <h2>☁ Azure DevOps Demo</h2>
        <nav>
            <a href="/">Overview</a>
            <a href="#pipeline">Pipeline</a>
            <a href="#about">About</a>
        </nav>
    </header>

    <main>
        <section class="welcome">
            <h1>DevOps Project Dashboard</h1>
            <p>
                Welcome! Monitor your demo application and learn
                how CI/CD works with Azure DevOps.
            </p>
        </section>

        <section class="cards">
            <div class="card">
                <h3>Application Status</h3>
                <div class="status healthy">● Healthy</div>
                <p>Flask application is responding.</p>
            </div>

            <div class="card">
                <h3>Environment</h3>
                <div class="status development">Development</div>
                <p>Local development environment.</p>
            </div>

            <div class="card">
                <h3>Pipeline Status</h3>
                <div class="status pending">CI Configured</div>
                <p>Automated testing will run in Azure Pipelines.</p>
            </div>
        </section>

        <section class="card" id="pipeline">
            <h2 class="section-title">Deployment Overview</h2>

            <div class="pipeline">
                <div class="pipeline-step">
                    <strong>01. Code</strong>
                    <span>Azure Repos</span>
                </div>

                <div class="pipeline-step">
                    <strong>02. Build</strong>
                    <span>Install dependencies</span>
                </div>

                <div class="pipeline-step">
                    <strong>03. Test</strong>
                    <span>Run pytest</span>
                </div>

                <div class="pipeline-step">
                    <strong>04. Deploy</strong>
                    <span>Future step</span>
                </div>
            </div>
        </section>

        <section class="card about" id="about">
            <h2>About This Project</h2>
            <p>
                This is a sample Python web application created to
                practise Azure DevOps, Git, automated testing,
                YAML pipelines, and CI/CD.
            </p>

            <button onclick="checkHealth()">Check Application Health</button>
            <p id="health-result"></p>
        </section>
    </main>

    <footer>
        Azure DevOps Learning Project | Built with Python and Flask
    </footer>

    <script>
        async function checkHealth() {
            const result = document.getElementById("health-result");
            result.textContent = "Checking...";

            try {
                const response = await fetch("/health");
                const data = await response.json();

                result.textContent = response.ok
                    ? "✓ " + data.status + " — " + data.message
                    : "Application health check failed.";
            } catch (error) {
                result.textContent = "Unable to reach the application.";
            }
        }
    </script>
</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(HTML_TEMPLATE)


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "message": "Application is running successfully",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
