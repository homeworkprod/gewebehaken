"""
Gewebehaken
~~~~~~~~~~~

Twitter_ web hooks

These hooks are designed to work with requests sent via the Zapier_
service. The corresponding "zaps" must be configured to send a JSON
request body with at least the fields defined in the view functions
below.

.. _Twitter: https://twitter.com/
.. _Zapier: https://zapier.com/

:Copyright: 2015-2022 Jochen Kupperschmidt
:License: MIT, see LICENSE for details.
"""

from blinker import signal
from flask import Blueprint, request

from ..util import get_all_or_400, log_incoming_request_data, respond_no_content


twitter_followed = signal('twitter-followed')
twitter_mentioned = signal('twitter-mentioned')


blueprint = Blueprint('twitter', __name__, url_prefix='/twitter')


@blueprint.route('/followed', methods=['POST'])
@respond_no_content
def followed():
    data = request.get_json()
    log_incoming_request_data(data)

    keys = {'screen_name', 'name', 'target_account_screen_name'}
    fields = get_all_or_400(data, keys)

    twitter_followed.send(None, **fields)


@blueprint.route('/mentioned', methods=['POST'])
@respond_no_content
def mentioned():
    data = request.get_json()
    log_incoming_request_data(data)

    keys = {'screen_name', 'name', 'url', 'target_account_screen_name'}
    fields = get_all_or_400(data, keys)

    twitter_mentioned.send(None, **fields)
