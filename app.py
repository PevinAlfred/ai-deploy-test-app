from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics
import random

app = Flask(__name__)
# This automatically creates the /metrics endpoint and tracks requests
metrics = PrometheusMetrics(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

# Adding this new route to simulate a problem
@app.route('/error')
def trigger_error():
    """This endpoint will frequently raise an error to test incident response."""
    # We'll simulate an 80% failure rate for this endpoint
    if random.random() > 0.2:
        # This raises a 500 Internal Server Error
        raise Exception("Simulating a critical database connection error!")
    
    return "This time it worked!", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
