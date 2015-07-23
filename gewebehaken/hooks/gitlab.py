# -*- coding: utf-8 -*-

"""
Gewebehaken
~~~~~~~~~~~

Gitlab_ web hooks

These hooks are designed to work with requests sent by GitLab_
instances.

The hooks can be configured – and tested – in GitLab_ per project
via "Settings → Web Hooks".

.. _GitLab: https://gitlab.com/

:Copyright: 2015 `Jochen Kupperschmidt <http://homework.nwsnet.de/>`_
:License: MIT, see LICENSE for details.
"""

from blinker import signal
from flask import abort, Blueprint, request

from ..util import get_all_or_400, log_incoming_request_data, respond_no_content


gitlab_issue         = signal('gitlab-issue')
gitlab_merge_request = signal('gitlab-merge-request')
gitlab_note          = signal('gitlab-note')
gitlab_push          = signal('gitlab-push')
gitlab_tag_push      = signal('gitlab-tag-push')


EVENT_TYPES_TO_SIGNALS = {
    'Issue Hook':         gitlab_issue,
    'Merge Request Hook': gitlab_merge_request,
    'Note Hook':          gitlab_note,
    'Push Hook':          gitlab_push,
    'Tag Push Hook':      gitlab_tag_push,
}


blueprint = Blueprint('gitlab', __name__)


@blueprint.route('/gitlab', methods=['POST'])
@respond_no_content
def triggered():
    data = request.get_json()
    log_incoming_request_data(data)

    signal = find_signal_for_event_type()
    signal.send(None, **data)


def find_signal_for_event_type():
    event_type = request.headers.get('X-Gitlab-Event')
    try:
        return EVENT_TYPES_TO_SIGNALS[event_type]
    except KeyError:
        abort(400, 'Unknown event type.')
