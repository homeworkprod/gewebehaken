# -*- coding: utf-8 -*-

"""
Gewebehaken
~~~~~~~~~~~

Command-line interface

:Copyright: 2015 `Jochen Kupperschmidt <http://homework.nwsnet.de/>`_
:License: MIT, see LICENSE for details.
"""

from argparse import ArgumentParser


DEFAULT_HOST = '127.0.0.1'
DEFAULT_PORT = 5000


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
