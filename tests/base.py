import json

import pytest

from gewebehaken.app import create_app


def post_json(client, path, data, headers=None):
    """Send a POST request with a JSON body."""
    return client.post(
        path,
        content_type='application/json',
        data=json.dumps(data),
        headers=headers,
    )
