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

from gewebehaken.app import create_app
from gewebehaken.cli import parse_args


DEFAULT_LOG_FILENAME = 'incoming.log'


if __name__ == '__main__':
    args = parse_args()

    app = create_app(log_filename=DEFAULT_LOG_FILENAME)

    app.run(host=args.host,
            port=args.port,
            debug=args.debug)
