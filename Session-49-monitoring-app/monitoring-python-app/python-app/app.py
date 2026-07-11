from flask import Flask
from prometheus_client import Counter, generate_latest

app = Flask(__name__)
REQUEST_COUNT = Counter('http_requests_total','Total HTTP Request')

@app.route("/")
def hello():
    REQUEST_COUNT.inc() # increase count on every Request
    return "Hello From Python app"

@app.route("/metrics")
def metrics():
    return generate_latest(),200, {'content-type':'text/plain'}

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)

# 2 Path
# localhost:5000
# localhost:5000/metrics (this we integrate with prometheus)