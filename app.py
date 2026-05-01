# app.py
from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/health')
def health():
    return jsonify({"status": "OK", "service": "env-monitor-api"})

@app.route('/api/v1/readings/latest')
def latest_readings():
    # Эмуляция последних показаний с датчиков
    return jsonify({
        "sensor_id": "NODE_01",
        "location": "Living Room",
        "temperature_celsius": 23.5,
        "humidity_percent": 45.0,
        "co2_index": 1.15,
        "timestamp": "2026-05-01T12:00:00Z"
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
