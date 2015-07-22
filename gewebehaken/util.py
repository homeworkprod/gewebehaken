# -*- coding: utf-8 -*-

"""
Gewebehaken
~~~~~~~~~~~

Utilities

:Copyright: 2015 `Jochen Kupperschmidt <http://homework.nwsnet.de/>`_
:License: MIT, see LICENSE for details.
"""

from functools import wraps
from pprint import pformat

from flask import current_app, Response


def log_incoming_request_data(data):
    delimiter_line = '-' * 40
    log_message = delimiter_line + '\n' + pformat(data)
    current_app.logger.warn(log_message)


def respond_no_content(f):
    """Decorate a callable so that a ``204 No Content`` response is
    returned after it is executed.
    """
    @wraps(f)
    def wrapper(*args, **kwargs):
        f(*args, **kwargs)
        return Response(status=204)
    return wrapper
