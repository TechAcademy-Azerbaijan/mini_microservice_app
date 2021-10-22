import requests

post_list = [
    {
        'id': 1,
        'title': 'Post 1'
    },
    {
        'id': 2,
        'title': 'Post 2'
    }
]


def get_posts():
    return post_list


def create_post(new_post):
    new_post['id'] = post_list[-1]['id'] + 1
    post_list.append(new_post)
    event_data = {
        'type': 'PostCreated',
        'data': new_post
    }
    requests.post('http://localhost:5002/events', json=event_data)
    return new_post