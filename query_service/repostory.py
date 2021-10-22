import requests

post_list = [
    {
        'id': 1,
        'title': 'Post 1',
        'comments': [],
    },
    {
        'id': 2,
        'title': 'Post 2',
        'comments': [],
    },
]


def get_posts():
    return post_list


def create_post(new_post):
    new_post['comments'] = []
    post_list.append(new_post)
    return new_post


def create_comment(new_comment):
    post_id = new_comment['post_id']
    for post in post_list:
        if post['id'] == post_id:
            post['comments'].append(new_comment)
    return new_comment