# -*- coding: utf-8 -*-

"""
Gewebehaken
~~~~~~~~~~~

Twitter web hooks

:Copyright: 2015 `Jochen Kupperschmidt <http://homework.nwsnet.de/>`_
:License: MIT, see LICENSE for details.
"""

from blinker import signal
from flask import abort, Blueprint, request

from ..util import log_incoming_request_data, respond_no_content


twitter_followed = signal('twitter-followed')
twitter_mentioned = signal('twitter-mentioned')


blueprint = Blueprint('twitter', __name__, url_prefix='/twitter')


@blueprint.route('/followed', methods=['POST'])
@respond_no_content
def followed():
    data = request.get_json()
    log_incoming_request_data(data)

    screen_name = get_or_400(data, 'screen_name')
    name = get_or_400(data, 'name')

    twitter_followed.send(
        None,
        screen_name=screen_name,
        name=name)


@blueprint.route('/mentioned', methods=['POST'])
@respond_no_content
def mentioned():
    data = request.get_json()
    log_incoming_request_data(data)

    screen_name = get_or_400(data, 'screen_name')
    name = get_or_400(data, 'name')
    url = get_or_400(data, 'url')

    twitter_mentioned.send(
        None,
        screen_name=screen_name,
        name=name,
        url=url)


def get_or_400(data, key):
    try:
        return data[key]
    except KeyError:
        abort(400, 'Missing key: ' + key)
