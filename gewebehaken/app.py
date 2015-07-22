# -*- coding: utf-8 -*-

"""
Gewebehaken
~~~~~~~~~~~

The WSGI application

:Copyright: 2015 `Jochen Kupperschmidt <http://homework.nwsnet.de/>`_
:License: MIT, see LICENSE for details.
"""

import logging
from logging import FileHandler, Formatter

from flask import Flask

from .hooks.twitter import blueprint as twitter_blueprint


def create_app(log_filename=None):
    """Create the actual application."""
    app = Flask(__name__, static_folder=None)

    if log_filename:
        configure_logging(app, log_filename)

    app.register_blueprint(twitter_blueprint)

    return app


def configure_logging(app, filename):
    """Configure app to log to that file."""
    handler = FileHandler(filename, encoding='utf-8')
    handler.setFormatter(Formatter('%(asctime)s %(funcName)s %(message)s'))
    handler.setLevel(logging.INFO)

    app.logger.addHandler(handler)
