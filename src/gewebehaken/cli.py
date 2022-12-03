"""
Gewebehaken
~~~~~~~~~~~

Command-line interface

:Copyright: 2015-2022 Jochen Kupperschmidt
:License: MIT, see LICENSE for details.
"""

from argparse import ArgumentParser

from .app import create_app


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
        help='debug mode',
    )

    parser.add_argument(
        '--host',
        dest='host',
        default=DEFAULT_HOST,
        help=f'the host to listen on [default: {DEFAULT_HOST}]',
        metavar='HOST',
    )

    parser.add_argument(
        '--port',
        dest='port',
        type=int,
        default=DEFAULT_PORT,
        help=f'the port to listen on [default: {DEFAULT_PORT:d}]',
        metavar='PORT',
    )

    parser.add_argument(
        '--logfile',
        dest='logfile',
        help='logfile to write incoming webhook requests to',
        metavar='LOGFILE',
    )

    return parser.parse_args()


def main():
    args = parse_args()
    app = create_app(log_filename=args.logfile)
    app.run(host=args.host, port=args.port, debug=args.debug)
