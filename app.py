from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello from Python Flask App running on Azure App Service!-updated"


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "application": "python-azure-demo"
    })


@app.route("/api/message")
def message():
    return jsonify({
        "message": "Hello from Azure DevOps CI/CD!",
        "version": "1.0"
    })


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=3000)