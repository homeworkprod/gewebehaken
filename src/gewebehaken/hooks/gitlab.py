"""
Gewebehaken
~~~~~~~~~~~

Gitlab_ web hooks

These hooks are designed to work with requests sent by GitLab_
instances.

The hooks can be configured – and tested – in GitLab_ per project
via "Settings → Web Hooks".

.. _GitLab: https://gitlab.com/

:Copyright: 2015-2022 Jochen Kupperschmidt
:License: MIT, see LICENSE for details.
"""

from enum import Enum

from blinker import signal
from flask import abort, Blueprint, request

from ..util import (
    get_or_400,
    log_incoming_request_data,
    respond_no_content,
)


gitlab_commit_note        = signal('gitlab-commit-note')
gitlab_issue              = signal('gitlab-issue')
gitlab_issue_note         = signal('gitlab-issue-note')
gitlab_merge_request      = signal('gitlab-merge-request')
gitlab_merge_request_note = signal('gitlab-merge-request-note')
gitlab_push               = signal('gitlab-push')
gitlab_snippet_note       = signal('gitlab-snippet-note')
gitlab_tag_push           = signal('gitlab-tag-push')


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
    EventType.push:          gitlab_push,
    EventType.tag_push:      gitlab_tag_push,
}


NOTEABLE_TYPES_TO_SIGNALS = {
    'commit':       gitlab_commit_note,
    'issue':        gitlab_issue_note,
    'mergerequest': gitlab_merge_request_note,
    'snippet':      gitlab_snippet_note,
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
    if event_type is EventType.note:
        obj_attrs = get_or_400(data, 'object_attributes')
        noteable_type = get_or_400(obj_attrs, 'noteable_type').lower()
        try:
            return NOTEABLE_TYPES_TO_SIGNALS[noteable_type]
        except KeyError:
            abort(400, 'Unknown noteable type.')

    return EVENT_TYPES_TO_SIGNALS[event_type]
