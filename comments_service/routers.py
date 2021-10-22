from flask import request, jsonify
from repostory import *
from app import app


@app.route('/posts/<int:post_id>/comments', methods=['GET', 'POST'])
def comments(post_id):
    if request.method == 'POST':
        new_comment_data = dict(request.form or request.json)
        new_comment = create_comment(new_comment_data=new_comment_data, post_id=post_id)
        return jsonify(new_comment), 201
    comments_list = get_comments_by_post(post_id)
    return jsonify(comments_list), 200


@app.route('/events', methods=['POST'])
def events():
    return jsonify({'message': 'success'}), 200