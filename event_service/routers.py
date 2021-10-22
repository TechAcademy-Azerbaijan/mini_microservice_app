from flask import request, jsonify
import requests
from app import app


@app.route('/events', methods=['POST'])
def events():
    event_data = dict(request.form or request.json)
    requests.post('http://localhost:5003/events', json=event_data)  # query service
    requests.post('http://localhost:5001/events', json=event_data)  # comments service
    requests.post('http://localhost:5000/events', json=event_data)  # post service
    return jsonify({'message': 'success'}), 200
