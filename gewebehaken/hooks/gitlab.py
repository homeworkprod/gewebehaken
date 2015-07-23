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

from enum import Enum

from blinker import signal
from flask import abort, Blueprint, request

from ..util import get_all_or_400, get_or_400, log_incoming_request_data, \
                   respond_no_content


gitlab_issue         = signal('gitlab-issue')
gitlab_merge_request = signal('gitlab-merge-request')
gitlab_note          = signal('gitlab-note')
gitlab_push          = signal('gitlab-push')
gitlab_tag_push      = signal('gitlab-tag-push')


EventType = Enum('EventType', 'issue merge_request note push tag_push')


EVENT_TYPE_VALUES_AND_OBJECT_KINDS_TO_EVENT_TYPES = {
    ('Issue Hook'        , 'issue'        ): EventType.issue,
    ('Merge Request Hook', 'merge_request'): EventType.merge_request,
    ('Note Hook'         , 'note'         ): EventType.note,
    ('Push Hook'         , 'push'         ): EventType.push,
    ('Tag Push Hook'     , 'tag_push'     ): EventType.tag_push,
}


EVENT_TYPES_TO_SIGNALS = {
    EventType.issue:         gitlab_issue,
    EventType.merge_request: gitlab_merge_request,
    EventType.note:          gitlab_note,
    EventType.push:          gitlab_push,
    EventType.tag_push:      gitlab_tag_push,
}


blueprint = Blueprint('gitlab', __name__)


@blueprint.route('/gitlab', methods=['POST'])
@respond_no_content
def triggered():
    data = request.get_json()
    log_incoming_request_data(data)

    event_type = determine_event_type(data)
    signal = determine_signal(event_type, data)

    signal.send(None, **data)


def determine_event_type(data):
    event_type_value = request.headers.get('X-Gitlab-Event')
    object_kind = get_or_400(data, 'object_kind')

    key = (event_type_value, object_kind)

    try:
        return EVENT_TYPE_VALUES_AND_OBJECT_KINDS_TO_EVENT_TYPES[key]
    except KeyError:
        abort(400, 'Unknown event type.')


def determine_signal(event_type, data):
    return EVENT_TYPES_TO_SIGNALS[event_type]
