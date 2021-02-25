import pytest

from gewebehaken.app import create_app


def post_json(client, path, data, headers=None):
    """Send a POST request with a JSON body."""
    return client.post(path, json=data, headers=headers)
