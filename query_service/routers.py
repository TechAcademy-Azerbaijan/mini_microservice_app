from flask import request, jsonify
from repostory import *
from app import app


@app.route('/posts', methods=['GET'])
def posts():
    post_list = get_posts()
    return jsonify(post_list), 200


@app.route('/events', methods=['POST'])
def events():
    event_data = dict(request.form or request.json)
    if event_data['type'] == 'PostCreated':
        create_post(event_data['data'])
    elif event_data['type'] == 'CommentCreated':
        create_comment(event_data['data'])
    return jsonify({'message': 'success'}), 200
