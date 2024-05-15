from flask import Flask
from prometheus_client import Gauge, generate_latest, CONTENT_TYPE_LATEST
import random
import time

app = Flask(__name__)
gauge = Gauge('custom_metric', 'Custom Metric Description')

@app.route('/metrics')
def metrics():
    gauge.set(random.randint(0, 100))
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

@app.route("/")
def handle_view():
    return "Hello World"
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
