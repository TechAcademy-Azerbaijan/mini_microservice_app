from flask import request, jsonify
from repostory import *
from app import app


@app.route('/posts', methods=['GET', 'POST'])
def posts():
    if request.method == 'POST':
        new_post_data = dict(request.form or request.json)
        new_post = create_post(new_post=new_post_data)
        return jsonify(new_post), 201
    post_list = get_posts()
    return jsonify(post_list), 200


@app.route('/events', methods=['POST'])
def events():
    return jsonify({'message': 'success'}), 200