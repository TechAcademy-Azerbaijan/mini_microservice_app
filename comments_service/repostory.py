import requests

comments_list = [
    {
        "id": 1,
        "post_id": 1,
        "content": 'Comment #1'
    },
    {
        "id": 2,
        "post_id": 1,
        "content": 'Comment #2'
    },
    {
        "id": 3,
        "post_id": 2,
        "content": 'Comment #3'
    }
]


# def get_comments_by_post(post_id):
#     post_comments = []
#     for comment in comments_list:
#         if comment['post_id'] == post_id:
#             post_comments.append(comment)
#     return post_comments

def get_comments_by_post(post_id):
    return list(filter(lambda comment: comment['post_id'] == post_id, comments_list))


def create_comment(new_comment_data, post_id):
    new_comment_data['id'] = comments_list[-1]['id'] + 1
    new_comment_data['post_id'] = post_id
    comments_list.append(new_comment_data)
    event_data = {
        'type': 'CommentCreated',
        'data': new_comment_data
    }
    requests.post('http://localhost:5002/events', json=event_data)
    return new_comment_data
