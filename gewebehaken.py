#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Gewebehaken
~~~~~~~~~~~

:Copyright: 2015 `Jochen Kupperschmidt <http://homework.nwsnet.de/>`_
:Date: 28-Jun-2015
:License: MIT, see LICENSE for details.
:Version: 0.0
"""

from argparse import ArgumentParser
from functools import wraps
import logging
from logging import FileHandler, Formatter
from pprint import pformat

from blinker import signal
from flask import Flask, request, Response


DEFAULT_HOST = '127.0.0.1'
DEFAULT_PORT = 5000
DEFAULT_LOG_FILENAME = 'incoming.log'


twitter_followed = signal('twitter-followed')
twitter_mentioned = signal('twitter-mentioned')


app = Flask(__name__)


def respond_no_content(f):
    """Decorate a callable so that a ``204 No Content`` response is
    returned after it is executed.
    """
    @wraps(f)
    def wrapper(*args, **kwargs):
        f(*args, **kwargs)
        return Response(status=204)
    return wrapper


@app.route('/twitter/followed', methods=['POST'])
@respond_no_content
def followed():
    data = request.get_json()
    log_incoming_request_data(data)

    screen_name = data['screen_name']
    name = data['name']

    twitter_followed.send(
        None,
        screen_name=screen_name,
        name=name)


@app.route('/twitter/mentioned', methods=['POST'])
@respond_no_content
def mentioned():
    data = request.get_json()
    log_incoming_request_data(data)

    screen_name = data['screen_name']
    name = data['name']
    url = data['url']

    twitter_mentioned.send(
        None,
        screen_name=screen_name,
        name=name,
        url=url)


def log_incoming_request_data(data):
    delimiter_line = '-' * 40
    log_message = delimiter_line + '\n' + pformat(data)
    app.logger.warn(log_message)


def parse_args():
    """Setup and apply the command line arguments parser."""
    parser = ArgumentParser()

    parser.add_argument(
        '--debug',
        dest='debug',
        action='store_true',
        default=False,
        help='debug mode')

    parser.add_argument(
        '--host',
        dest='host',
        default=DEFAULT_HOST,
        help='the host to listen on [default: {}]'.format(DEFAULT_HOST),
        metavar='HOST')

    parser.add_argument(
        '--port',
        dest='port',
        type=int,
        default=DEFAULT_PORT,
        help='the port to listen on [default: {:d}]'.format(DEFAULT_PORT),
        metavar='PORT')

    return parser.parse_args()


def configure_logging(filename):
    handler = FileHandler(filename, encoding='utf-8')
    handler.setFormatter(Formatter('%(asctime)s %(funcName)s %(message)s'))
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)


if __name__ == '__main__':
    args = parse_args()

    configure_logging(DEFAULT_LOG_FILENAME)

    app.run(host=args.host,
            port=args.port,
            debug=args.debug)
