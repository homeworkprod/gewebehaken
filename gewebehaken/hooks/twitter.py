# -*- coding: utf-8 -*-

"""
Gewebehaken
~~~~~~~~~~~

Twitter web hooks

:Copyright: 2015 `Jochen Kupperschmidt <http://homework.nwsnet.de/>`_
:License: MIT, see LICENSE for details.
"""

from blinker import signal
from flask import Blueprint, request

from ..util import log_incoming_request_data, respond_no_content


twitter_followed = signal('twitter-followed')
twitter_mentioned = signal('twitter-mentioned')


blueprint = Blueprint('blueprint', __name__)


@blueprint.route('/twitter/followed', methods=['POST'])
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


@blueprint.route('/twitter/mentioned', methods=['POST'])
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
