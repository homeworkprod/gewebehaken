"""
Gewebehaken
~~~~~~~~~~~

Utilities

:Copyright: 2015-2022 Jochen Kupperschmidt
:License: MIT, see LICENSE for details.
"""

from functools import wraps
from pprint import pformat

from flask import abort, current_app, Response


def get_all_or_400(data, keys):
    """Return a dictionary of the given keys mapped to their values
    taken from the given dictionary.

    If at least one of the keys is not found in the dictionary, a
    response is sent with status code 400 and an error message
    indicating the missing key.
    """
    return {key: get_or_400(data, key) for key in keys}


def get_or_400(data, key):
    """Return the value for the given key in the given dictionary

    If the key is not found in the dictionary, a response is sent with
    status code 400 and an error message indicating the missing key.
    """
    try:
        return data[key]
    except KeyError:
        abort(400, 'Missing key: ' + key)


def log_incoming_request_data(data):
    delimiter_line = '-' * 40
    log_message = delimiter_line + '\n' + pformat(data)
    current_app.logger.warning(log_message)


def respond_no_content(f):
    """Decorate a callable so that a ``204 No Content`` response is
    returned after it is executed.
    """

    @wraps(f)
    def wrapper(*args, **kwargs):
        f(*args, **kwargs)
        return Response(status=204)

    return wrapper
