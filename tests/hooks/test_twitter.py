from gewebehaken.hooks.twitter import twitter_followed, twitter_mentioned

from ..base import post_json


def test_followed(client):
    received_signal_data = {}

    @twitter_followed.connect
    def receive_signal(sender, **data):
        received_signal_data.update(data)

    request_data = {
        'screen_name': 'example',
        'name': 'Example User',
    }

    response = post_json(client, '/twitter/followed', data=request_data)

    assert response.status_code == 204
    assert received_signal_data == request_data


def test_mentioned(client):
    received_signal_data = {}

    @twitter_mentioned.connect
    def receive_signal(sender, **data):
        received_signal_data.update(data)

    request_data = {
        'screen_name': 'example',
        'name': 'Example User',
        'url': 'http://twitter.com/example',
    }

    response = post_json(client, '/twitter/mentioned', data=request_data)

    assert response.status_code == 204
    assert received_signal_data == request_data
